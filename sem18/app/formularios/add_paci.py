from django import forms

class Add_pac(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    fecha_nacimiento = forms.DateTimeField()
    sexo = forms.CharField(max_length=1)
    altura = forms.FloatField()