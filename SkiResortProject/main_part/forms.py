from django import forms


class AddJobTitle(forms.Form):
    job_title_name = forms.CharField(label='Должность', widget=forms.TextInput(attrs={'class': 'form-control'}))
    salary = forms.DecimalField(label='Заработная плата', widget=forms.TextInput(attrs={'class': 'form-control'}))