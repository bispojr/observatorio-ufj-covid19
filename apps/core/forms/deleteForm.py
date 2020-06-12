from django import forms

class DeleteBoletimEpidemiologicoForm(forms.Form):
    cidade = forms.CharField(max_length=256)
    data_atualizacao = forms.DateTimeField()