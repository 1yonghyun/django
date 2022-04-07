from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'my-title form-control',
                'placeholder': 'Enter the title',
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'my-content form-control',
            }
        ),
        error_messages={
            'required': 'Please enter your content!!!',
        }
    )

    class Meta:
        model = Article
        fields = '__all__'