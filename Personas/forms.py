from django import forms

class PersonaFormulario(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    nacionalidad=forms.CharField()
    ranking=forms.IntegerField()

class TorneoFormulario(forms.Form):
    nombre=forms.CharField()
    sitio=forms.CharField()
    year=forms.IntegerField()
    partidaN=forms.IntegerField()
    humano=forms.CharField()
    maquina=forms.CharField()
    partidaR=forms.CharField()
    ganador=forms.CharField()

class CampeonesFormulario(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    periodo=forms.CharField()