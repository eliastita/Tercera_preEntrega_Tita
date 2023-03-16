from django import forms

class CursoForm(forms.Form):
    name = forms.CharField(max_length=50)
    idc = forms.IntegerField(min_value=1000)
