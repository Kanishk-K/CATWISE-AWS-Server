from import_export import resources
from .models import CatWise

class CatWiseResource(resources.ModelResource):

    class Meta:
        model = CatWise
        import_id_fields=[
            'id'
        ]