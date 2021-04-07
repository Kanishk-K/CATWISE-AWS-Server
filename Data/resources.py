from import_export import resources
from .models import CatWise

class CatWiseResource(resources.ModelResource):

    class Meta:
        model = CatWise
        exclude = (
            'VTan',
            'W1W2Diff',
            'W1W2DiffErr',
            'TotalPM',
            'TotalPMErr',
            'H_W2',
            'JW2Diff',
            'JW2DiffErr',
            'WiseURL',
            'created_at',
        )
        import_id_fields=[
            'id'
        ]