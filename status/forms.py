from django import forms

from .models import Status


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = "__all__"

    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get("content")
        if len(content) > 255:
            raise forms.ValidationError("Maximum length limit is 255")
        else:
            return content

    def clean(self, *args, **kwargs):
        content = self.cleaned_data.get('content')
        image = self.cleaned_data.get('image')
        content = None if content == '' else content
        if content is None:
            raise forms.ValidationError("Content Field is required")
        return super().clean(*args, **kwargs)
