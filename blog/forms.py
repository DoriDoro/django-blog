from django import forms
from django.contrib.auth import get_user_model

from blog.models import Comment


UserModel = get_user_model()


class EmailPostForm(forms.Form):
    name = forms.CharField(
        max_length=25,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your name"}
        ),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Your Email address"}
        )
    )
    to = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Email address of receiver"}
        )
    )
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={"class": "form-control", "rows": 6, "placeholder": "Your message"}
        ),
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
        widgets = {
            "body": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Your comment",
                }
            ),
        }


class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=250,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter a word or two..."}
        ),
        label="",
    )
