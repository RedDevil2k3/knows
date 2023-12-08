from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

class UserSearchForm(forms.Form):
    query = forms.CharField()