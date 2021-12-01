from django import forms
from django.forms.widgets import RadioSelect


class FirstForm(forms.Form):
    floorPlan = forms.ChoiceField(widget=RadioSelect(), choices=[('1bhk', '1 BHK')])