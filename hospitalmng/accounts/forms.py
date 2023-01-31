from django import forms

class RegForm(forms.Form):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    username=forms.CharField(max_length=100)
    experience=forms.IntegerField()
    password=forms.CharField(max_length=100)
    email=forms.EmailField()
    def clean(self):
        cleaned_data=super().clean()
        first_name=cleaned_data.get('first_name')
        last_name=cleaned_data.get('last_name')
        experience=cleaned_data.get('experience')
        if first_name==last_name:
            msg='both can not be same'
            self.add_error('first_name',msg)
            self.add_error('last_name',msg)
        if experience<0:
            msg='invalid data'
            self.add_error('experience',msg)
class Logform(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)