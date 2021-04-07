from django import forms
from django.forms.models import ModelForm
from django.forms.widgets import TextInput
from .models import CatWise

class CatWiseForm(ModelForm):
    class Meta:
        model = CatWise
        fields = [
            'RaDEC',
            'RA',
            'DEC',
            'FoundInSearch',
            'AddDate',
            'w1mpro',
            'w1sigmpro',
            'w1snr_pm',
            'w2mpro',
            'w2sigmpro',
            'w2snr_pm',
            'PMRA',
            'sigPMRA',
            'PMDec',
            'sigPMDec',
            'SIMBAD',
            'GaiaDR2plx',
            'GaiaDR2PlxErr',
            'BYW',
            'GaiaCoMover',
            'OnSpitzerPrg',
            'JMag',
            'JMagErr',
            'JMagSrc',
            'CatWISESpec',
            'CatWISESpecSrc',
            'SpizerConsider',
            'Note'
        ]
    def __init__(self, *args, **kwargs):
        super(CatWiseForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs.update({
                'id':visible.field.label,
                'class':'form-control mb-2',
            })
        self.fields['AddDate'].widget.attrs.update({
            'class':'form-control mb-2 datepicker',
            'data-provide':'datepicker'
        })