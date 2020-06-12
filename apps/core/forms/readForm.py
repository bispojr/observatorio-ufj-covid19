from django import forms
from ..models import BoletimEpidemiologico

class ReadBoletimEpidemiologicoForm(forms.Form):
    cidade = forms.CharField(max_length=256)
    data_atualizacao = forms.DateTimeField()