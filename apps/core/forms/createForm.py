from django import forms
from ..models import BoletimEpidemiologico

class CreateBoletimEpidemiologicoForm(forms.Form):
    cidade = forms.CharField(max_length=256)
    data_atualizacao = forms.DateTimeField()
    fonte_oficial = forms.URLField()
    confirmados = forms.IntegerField(required=False)
    recuperados = forms.IntegerField(required=False)
    obitos = forms.IntegerField(required=False)
    suspeitos = forms.IntegerField(required=False)
    investigados = forms.IntegerField(required=False)
    descartados = forms.IntegerField(required=False)
    monitorados = forms.IntegerField(required=False)
    notificados = forms.IntegerField(required=False)
    isolados = forms.IntegerField(required=False)
    internados = forms.IntegerField(required=False)
    enfermaria = forms.IntegerField(required=False)
    uti = forms.IntegerField(required=False)