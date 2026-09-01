from django import forms

class Post_form(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
    is_enbale = forms.BooleanField()
    publish_date = forms.DateField()