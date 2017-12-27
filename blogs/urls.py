from django.conf.urls import url

from blogs.views import BlogsView, BlogsPost, BlogsCreateView

urlpatterns = [
    url(r'^', BlogsView.as_view(), name='blogs'),
    url(r'^post/<int:pk>/', BlogsPost.as_view(), name='post_detail'),
    url(r'^post/new/', BlogsCreateView.as_view(), name='post_new'),
]