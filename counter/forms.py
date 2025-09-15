# counter/forms.py
from django import forms
from .models import FoodItemTemplate

class FoodItemTemplateForm(forms.ModelForm):
    class Meta:
        model = FoodItemTemplate
        fields = ['name', 'modifier', 'joules']

class FoodLogForm(forms.Form):
    template = forms.ModelChoiceField(
        queryset=FoodItemTemplate.objects.none(),
        label="Item"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['template'].queryset = FoodItemTemplate.objects.all().order_by('name')
