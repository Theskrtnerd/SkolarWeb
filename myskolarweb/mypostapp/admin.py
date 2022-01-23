from django.contrib import admin
from mypostapp.forms import AdminPostForm, AdminTagForm
from mypostapp.models import Post, Category
# Register your models here.
@admin.register(Post)
class MyPostAdmin(admin.ModelAdmin):
    form = AdminPostForm
    
    class Meta:
        model = Post
@admin.register(Category)
class MyPostAdmin(admin.ModelAdmin):
    form = AdminTagForm
    
    class Meta:
        model = Category
    