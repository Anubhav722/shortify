from django import forms


class UrlForm(forms.Form):
    url = forms.URLField()


class UploadFileForm(forms.Form):
    file = forms.FileField()
