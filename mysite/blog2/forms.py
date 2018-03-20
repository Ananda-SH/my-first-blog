from django import forms

from .models import Registration

class RegisForm(forms.ModelForm):

    class Meta:
        model = Registration
        fields = ('name', 'number',)