from django.conf.urls import url

from posts.views import PostView

urlpatterns = [
    url(r'^post/', PostView.as_view(), name='post')
]