from django import forms

class PersonaFormulario(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    nacionalidad=forms.CharField()
    ranking=forms.IntegerField()