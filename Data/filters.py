from django.http import request
import django_filters
from django_filters import DateFilter, NumberFilter, BooleanFilter, CharFilter

from .models import CatWise

class CatWiseFilter(django_filters.FilterSet):
    RA_lte = NumberFilter(field_name="RA", lookup_expr="lte")
    RA_gte = NumberFilter(field_name="RA", lookup_expr="gte")
    DEC_lte = NumberFilter(field_name="DEC", lookup_expr="lte")
    DEC_gte = NumberFilter(field_name="DEC", lookup_expr="gte")
    FoundInSearch = CharFilter(field_name="FoundInSearch", lookup_expr="icontains")

    w1mpro_lte = NumberFilter(field_name="w1mpro", lookup_expr="lte")
    w1mpro_gte = NumberFilter(field_name="w1mpro", lookup_expr="gte")
    w1sigmpro_lte = NumberFilter(field_name="w1sigmpro", lookup_expr="lte")
    w1sigmpro_gte = NumberFilter(field_name="w1sigmpro", lookup_expr="gte")
    w1sigmpro_null = BooleanFilter(field_name="w1sigmpro", lookup_expr="isnull")
    w1snr_pm_lte = NumberFilter(field_name="w1snr_pm", lookup_expr="lte")
    w1snr_pm_gte = NumberFilter(field_name="w1snr_pm", lookup_expr="gte")
    w1snr_pm_null = BooleanFilter(field_name="w1snr_pm", lookup_expr="isnull")
    w2mpro_lte = NumberFilter(field_name="w2mpro", lookup_expr="lte")
    w2mpro_gte = NumberFilter(field_name="w2mpro", lookup_expr="gte")
    w2sigmpro_lte = NumberFilter(field_name="w2sigmpro", lookup_expr="lte")
    w2sigmpro_gte = NumberFilter(field_name="w2sigmpro", lookup_expr="gte")
    w2sigmpro_null = BooleanFilter(field_name="w2sigmpro", lookup_expr="isnull")
    w2snr_pm_lte = NumberFilter(field_name="w2snr_pm", lookup_expr="lte")
    w2snr_pm_gte = NumberFilter(field_name="w2snr_pm", lookup_expr="gte")
    w2snr_pm_null = BooleanFilter(field_name="w2snr_pm", lookup_expr="isnull")

    PMRA_lte = NumberFilter(field_name="PMRA", lookup_expr="lte")
    PMRA_gte = NumberFilter(field_name="PMRA", lookup_expr="gte")
    PMRA_null = BooleanFilter(field_name="PMRA", lookup_expr="isnull")
    sigPMRA_lte = NumberFilter(field_name="sigPMRA", lookup_expr="lte")
    sigPMRA_gte = NumberFilter(field_name="sigPMRA", lookup_expr="gte")
    sigPMRA_null = BooleanFilter(field_name="sigPMRA", lookup_expr="isnull")
    PMDec_lte = NumberFilter(field_name="PMDec", lookup_expr="lte")
    PMDec_gte = NumberFilter(field_name="PMDec", lookup_expr="gte")
    PMDec_null = BooleanFilter(field_name="PMDec", lookup_expr="isnull")
    sigPMDec_lte = NumberFilter(field_name="sigPMDec", lookup_expr="lte")
    sigPMDec_gte = NumberFilter(field_name="sigPMDec", lookup_expr="gte")
    sigPMDec_null = BooleanFilter(field_name="sigPMDec", lookup_expr="isnull")
    GaiaDR2plx_lte = NumberFilter(field_name="GaiaDR2plx", lookup_expr="lte")
    GaiaDR2plx_gte = NumberFilter(field_name="GaiaDR2plx", lookup_expr="gte")
    GaiaDR2plx_null = BooleanFilter(field_name="GaiaDR2plx", lookup_expr="isnull")
    GaiaDR2PlxErr_lte = NumberFilter(field_name="GaiaDR2PlxErr", lookup_expr="lte")
    GaiaDR2PlxErr_gte = NumberFilter(field_name="GaiaDR2PlxErr", lookup_expr="gte")
    GaiaDR2PlxErr_null = BooleanFilter(field_name="GaiaDR2PlxErr", lookup_expr="isnull")
    SIMBAD = BooleanFilter(field_name='SIMBAD')

    GaiaCoMover = BooleanFilter(field_name='GaiaCoMover')
    GaiaCoMover_null = BooleanFilter(field_name="GaiaCoMover", lookup_expr="isnull")
    BYW = CharFilter(field_name="BYW", lookup_expr="icontains")
    BYW_null = BooleanFilter(field_name="BYW", lookup_expr="isnull")
    OnSpitzerPrg = CharFilter(field_name="OnSpitzerPrg", lookup_expr="icontains")
    OnSpitzerPrg_null = BooleanFilter(field_name="OnSpitzerPrg", lookup_expr="isnull")

    JMag_lte = NumberFilter(field_name="JMag", lookup_expr="lte")
    JMag_gte = NumberFilter(field_name="JMag", lookup_expr="gte")
    JMag_null = BooleanFilter(field_name="JMag", lookup_expr="isnull")
    JMagErr_lte = NumberFilter(field_name="JMagErr", lookup_expr="lte")
    JMagErr_gte = NumberFilter(field_name="JMagErr", lookup_expr="gte")
    JMagErr_null = BooleanFilter(field_name="JMagErr", lookup_expr="isnull")
    SpizerConsider = BooleanFilter(field_name='SpizerConsider')
    SpizerConsider_null = BooleanFilter(field_name="SpizerConsider", lookup_expr="isnull")
    CatWISESpec = CharFilter(field_name="CatWISESpec", lookup_expr="icontains")
    CatWISESpec_null = BooleanFilter(field_name="CatWISESpec", lookup_expr="isnull")
    CatWISESpecSrc = CharFilter(field_name="CatWISESpecSrc", lookup_expr="icontains")
    CatWISESpecSrc_null = BooleanFilter(field_name="CatWISESpecSrc", lookup_expr="isnull")

    VTan_lte = NumberFilter(field_name="VTan", lookup_expr="lte")
    VTan_gte = NumberFilter(field_name="VTan", lookup_expr="gte")
    VTan_null = BooleanFilter(field_name="VTan", lookup_expr="isnull")
    JMag_lte = NumberFilter(field_name="JMag", lookup_expr="lte")
    JMag_gte = NumberFilter(field_name="JMag", lookup_expr="gte")
    JMag_null = BooleanFilter(field_name="JMag", lookup_expr="isnull")
    JMagErr_lte = NumberFilter(field_name="JMagErr", lookup_expr="lte")
    JMagErr_gte = NumberFilter(field_name="JMagErr", lookup_expr="gte")
    JMagErr_null = BooleanFilter(field_name="JMagErr", lookup_expr="isnull")
    JW2Diff_lte = NumberFilter(field_name="JW2Diff", lookup_expr="lte")
    JW2Diff_gte = NumberFilter(field_name="JW2Diff", lookup_expr="gte")
    JW2Diff_null = BooleanFilter(field_name="JW2Diff", lookup_expr="isnull")
    JW2DiffErr_lte = NumberFilter(field_name="JW2DiffErr", lookup_expr="lte")
    JW2DiffErr_gte = NumberFilter(field_name="JW2DiffErr", lookup_expr="gte")
    JW2DiffErr_null = BooleanFilter(field_name="JW2DiffErr", lookup_expr="isnull")
    W1W2Diff_lte = NumberFilter(field_name="W1W2Diff", lookup_expr="lte")
    W1W2Diff_gte = NumberFilter(field_name="W1W2Diff", lookup_expr="gte")
    W1W2DiffErr_lte = NumberFilter(field_name="W1W2DiffErr", lookup_expr="lte")
    W1W2DiffErr_gte = NumberFilter(field_name="W1W2DiffErr", lookup_expr="gte")
    W1W2DiffErr_null = BooleanFilter(field_name="W1W2DiffErr", lookup_expr="isnull")
    TotalPM_lte = NumberFilter(field_name="TotalPM", lookup_expr="lte")
    TotalPM_gte = NumberFilter(field_name="TotalPM", lookup_expr="gte")
    TotalPM_null = BooleanFilter(field_name="TotalPM", lookup_expr="isnull")
    TotalPMErr_lte = NumberFilter(field_name="TotalPMErr", lookup_expr="lte")
    TotalPMErr_gte = NumberFilter(field_name="TotalPMErr", lookup_expr="gte")
    TotalPMErr_null = BooleanFilter(field_name="TotalPMErr", lookup_expr="isnull")
    H_W2_lte = NumberFilter(field_name="H_W2", lookup_expr="lte")
    H_W2_gte = NumberFilter(field_name="H_W2", lookup_expr="gte")
    H_W2_null = BooleanFilter(field_name="H_W2", lookup_expr="isnull")

    class Meta:
        model = CatWise
        fields = {}
    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
                super(CatWiseFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
                for filter_ in self.filters.values():
                    filter_.field.widget.attrs.update({'class': 'form-control mb-2 align-self-end'})