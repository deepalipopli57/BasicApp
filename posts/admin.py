from django.contrib import admin

# Register your models here.
from posts.models import PostModel

admin.site.register(PostModel)