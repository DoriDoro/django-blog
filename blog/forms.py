from django import forms
from django.contrib.auth import get_user_model

from blog.models import Comment, Post

UserModel = get_user_model()


class EmailPostForm(forms.Form):
    name = forms.CharField(
        max_length=25,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your name",
                "aria-label": "Your name",
            }
        ),
        label="",
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your Email Address",
                "aria-label": "Your Email Address",
            }
        ),
        label="Your Email Address",
    )
    to = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Email Address of receiver",
                "aria-label": "Email Address of receiver",
            }
        ),
        label="Receiver Email Address",
    )
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 6,
                "placeholder": "Your message ...",
                "aria-label": "Your message ...",
            }
        ),
        label="",
    )


class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["body"].widget.attrs.update(
            {
                "class": "form-control",
                "rows": 4,
                "placeholder": "Your comment",
                "aria-label": "Your comment",
            }
        )

    class Meta:
        model = Comment
        fields = ["body"]


class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=250,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter one word or two..."}
        ),
        label="",
    )


class PostCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Enter title",
                "aria-label": "Enter title",
            }
        ),
        self.fields["body"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Enter content",
                "aria-label": "Enter content",
            }
        ),
        self.fields["image"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Choose an image",
                "aria-label": "Choose an image",
            }
        ),
        self.fields["status"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Choose the status",
                "aria-label": "Choose the status",
            }
        ),
        self.fields["tags"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Enter tags",
                "aria-label": "Enter tags",
            }
        ),

    class Meta:
        model = Post
        fields = ["title", "body", "image", "status", "tags"]
        labels = {
            "title": "",
            "body": "",
            "image": "",
            "status": "",
            "tags": "",
        }
