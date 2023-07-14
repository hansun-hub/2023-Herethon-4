from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '댓글을 입력해주세요'})
    )
    content.label = ''

    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content':'댓글내용',
        }
        # fields = '__all__'
        # exclude = ('article', 'user',)
