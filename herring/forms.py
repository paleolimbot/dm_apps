from django import forms
from django.core import validators
from . import models
from django.utils.safestring import mark_safe


class PortSampleForm(forms.ModelForm):
    class Meta:
        model = models.Sample
        fields = "__all__"
        exclude = ['old_id', 'season', "tests", "length_frequencies"]
        labels={
            'district':mark_safe("District (<a href='#' >search</a>)"),
            'vessel':mark_safe("Vessel CFVN (<a href='#' >add</a>)"),
        }
        widgets = {
            'remarks':forms.Textarea(attrs={'rows': '5'}),
            'sample_date':forms.DateInput(attrs={'type': 'date'}),
            'creation_date':forms.HiddenInput(),
            'created_by':forms.HiddenInput(),
            'last_modified_date':forms.HiddenInput(),
            'last_modified_by':forms.HiddenInput(),
            'sampling_protocol':forms.HiddenInput(),
            'latitude_n':forms.NumberInput(attrs={'placeholder':"dd.ddddd"}),
            'longitude_w':forms.NumberInput(attrs={'placeholder':"dd.ddddd"}),

        }

class LengthFrquencyWizardSetupForm(forms.Form):
    minimum_length = forms.FloatField(required=True,min_value=0, max_value=50, widget=forms.NumberInput(attrs={'placeholder': 'mulitple of 0.5 cm'}))
    maximum_length = forms.FloatField(required=True,min_value=0, max_value=50, widget=forms.NumberInput(attrs={'placeholder': 'mulitple of 0.5 cm'}))

    def clean_minimum_length(self):
        minimum_length = self.cleaned_data['minimum_length']
        if minimum_length % 0.5 > 0: #if length is not divisible by 0.5
            raise forms.ValidationError("Number must be a multiple of 0.5!")
        return minimum_length

    def clean_maximum_length(self):
        maximum_length = self.cleaned_data['maximum_length']
        if maximum_length % 0.5 > 0: #if length is not divisible by 0.5
            raise forms.ValidationError("Number must be a multiple of 0.5!")
        elif maximum_length < self.cleaned_data['minimum_length']:
            raise forms.ValidationError("Maxium length must be greater than or equal to minimum length!")
        return maximum_length

class LengthFrquencyWizardForm(forms.Form):
    count = forms.IntegerField(required=True, min_value=0, max_value=1000, widget=forms.NumberInput(attrs={'placeholder': 'Number of fish observed'}))
