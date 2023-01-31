from django import forms

class Opform(forms.Form):
    num1=forms.IntegerField()
    num2=forms.IntegerField()