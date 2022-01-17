from django.contrib import admin
from mypostapp.forms import AdminPostForm
from mypostapp.models import Post
# Register your models here.
@admin.register(Post)
class MyPostAdmin(admin.ModelAdmin):
    form = AdminPostForm
    
    class Meta:
        model = Post
    