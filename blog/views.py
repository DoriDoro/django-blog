from django.core.mail import send_mail
from django.db.models import Count
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView
from taggit.models import Tag

from blog.forms import EmailPostForm, CommentForm
from blog.models import Post


class PostListView(ListView):
    model = Post
    paginate_by = 5
    template_name = "post/list.html"
    context_object_name = "posts"

    def get_queryset(self):
        queryset = Post.published.all()
        tag_slug = self.kwargs.get("tag_slug")
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            queryset = queryset.filter(tags__in=[tag])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_slug = self.kwargs.get("tag_slug")
        if tag_slug:
            context["tags"] = get_object_or_404(Tag, slug=tag_slug)
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "post/detail.html"
    context_object_name = "post"

    def get_object(self):
        return get_object_or_404(
            Post,
            status=Post.Status.PUBLISHED,
            slug=self.kwargs["slug"],
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.filter(active=True)
        context["form"] = CommentForm()
        context["similar_posts"] = self._get_similar_posts()
        return context

    def _get_similar_posts(self):
        post_tags_ids = self.object.tags.values_list("id", flat=True)
        similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(
            id=self.object.id
        )
        similar_posts = similar_posts.annotate(same_tags=Count("tags")).order_by(
            "-same_tags", "-publish"
        )[:4]
        return similar_posts


def post_share(request, post_id):
    post = get_object_or_404(Post, pk=post_id, status=Post.Status.PUBLISHED)
    sent = False

    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            post_url = request.build_absolute_url(post.get_absolute_url())
            subject = (
                f"{cleaned_data['name']} ({cleaned_data['email']})"
                f"recommends you read {post.title}"
            )
            message = (
                f"Read {post.title} at {post_url}\n\n"
                f"{cleaned_data['name']}'s comments: {cleaned_data['comments']}"
            )
            send_mail(
                subject=subject,
                message=message,
                from_email=None,
                recipient_list=[cleaned_data["to"]],
            )
            sent = True

    else:
        form = EmailPostForm()

    return render(
        request, "post/share.html", {"post": post, "form": form, "sent": sent}
    )


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(
        request, "post/comment.html", {"post": post, "form": form, "comment": comment}
    )
