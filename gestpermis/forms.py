from django import forms

class CandidatForm(forms.Form):
    date = forms.CharField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    lieu = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))