import markdown
from django.conf import settings

from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy

from blog.models import Post


class LatestPostsFeed(Feed):
    title = settings.PROJECT_NAME
    link = reverse_lazy("blog:post_list")
    description = "New posts of my blog."

    def items(self):
        return Post.published.all()[:4]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords_html(markdown.markdown(item.body), 30)

    def item_pubdate(self, item):
        return item.publish
