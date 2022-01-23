from django import forms
from mypostapp.models import Post, Category
from pagedown.widgets import AdminPagedownWidget

# Admin forms
class AdminPostForm(forms.ModelForm):
    content = forms.CharField(
        widget=AdminPagedownWidget(),
        max_length=500)

    class Meta:
        model = Post
        fields = '__all__'

class AdminTagForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'