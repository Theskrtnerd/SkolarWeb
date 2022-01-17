from django import forms
from mypostapp.models import Post
from pagedown.widgets import AdminPagedownWidget

# Admin forms
class AdminPostForm(forms.ModelForm):
    content = forms.CharField(
        widget=AdminPagedownWidget(),
        max_length=500)

    class Meta:
        model = Post
        fields = '__all__'