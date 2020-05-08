from django import forms
from .models import StatusModel


class StatusModelForm(forms.ModelForm):
    class Meta:
        model = StatusModel
        fields = ['user', 'content', 'image']

    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data['content']
        content = None if content == '' else content
        if content is None:
            raise forms.ValidationError('Content is required')
        return content
