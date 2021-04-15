from django.urls import path

from . import views

app_name = 'Administration'
urlpatterns = [
    path('', views.index, name='index'),
    path('login',views.login_request,name='login'),
    path('changepass',views.password_change_request,name="changepass"),
    path('logout',views.logout_request,name='logout'),
]