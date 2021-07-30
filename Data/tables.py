import django_tables2 as tables
from .models import CatWise
from django.urls import reverse
class CatWiseTable(tables.Table):
    class Meta:
        model = CatWise
        sequence = ("id","RA","DEC","w1mpro","w2mpro",)
        exclude = ("Note","WiseURL","created_at","last_modified","last_modified_date",)
        row_attrs = {
            "class" : 'clickable-row',
            "data-href" : lambda record : f"/data/ViewEntry/{record.pk}/"
        } 