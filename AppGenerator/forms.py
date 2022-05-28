from email.policy import default
from logging import PlaceHolder
from django import forms
from .models import Frontend, Backend

class FrontendForm(forms.Form):
    fChoices = tuple([("","Select Frontend stack")] + [(x.fName, x.fName) for x in Frontend.objects.all()])
    frontend = forms.ChoiceField(choices=fChoices, label="Frontend Framework", initial="")
