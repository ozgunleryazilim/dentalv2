from django import forms
from page.models import BlogComment


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ('name', 'email', 'comment')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.keys():
            self.fields[field].widget.attrs.update({'class': 'form-control'})

        self.fields['name'].widget.attrs.update({'placeholder': self.fields['name'].label})
        self.fields['email'].widget.attrs.update({'placeholder': self.fields['email'].label})
        self.fields['comment'].widget.attrs.update({'placeholder': self.fields['comment'].label})
