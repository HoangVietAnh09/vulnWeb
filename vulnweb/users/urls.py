from django.urls import path
from . import views
app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('ssti/', views.ssti, name='ssti'),
    path('save/', views.save_info, name='save'),
    path('regist/', views.regist_info, name='regist'),
    path('success/',views.success, name='success')

]