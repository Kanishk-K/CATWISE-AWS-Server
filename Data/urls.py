from django.urls import path

from . import views

app_name = 'Data'
urlpatterns = [
    path('', views.index, name='index'),
    path('CSV/',views.render_csv,name="csv"),
    path('NewEntry/',views.add_data,name='add_data'),
    path('ViewEntry/<int:id>/',views.view_data,name="view_data"),
    path('EditEntry/<int:id>/',views.edit_data,name="edit_data"),
    path('DeleteEntry/<int:id>/',views.delete_data,name="delete_data"),
]