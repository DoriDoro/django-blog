from django.urls import path

from blog import views
from blog.feeds import LatestPostsFeed

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path("tag/<slug:tag_slug>/", views.PostListView.as_view(), name="post_list_by_tag"),
    path("create/", views.PostCreateView.as_view(), name="post_create"),
    path("<int:post_id>/share/", views.post_share, name="post_share"),
    path(
        "<int:post_id>/comment/", views.PostCommentView.as_view(), name="post_comment"
    ),
    path("latest/feed/", LatestPostsFeed(), name="post_feed"),
    path("search/", views.post_search, name="post_search"),
    path("about/", views.AboutMeView.as_view(), name="about_me"),
    # at the end because of the <slug>!!!
    path("<slug:slug>/", views.PostDetailView.as_view(), name="post_detail"),
]
