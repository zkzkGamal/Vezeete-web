from django.urls import path , include
from . import views
app_name = 'accounts'

urlpatterns = [
    path('doctors/',views.doctors_list,name = 'doctors_list'),
    path('doctors/<slug:slug>/',views.doctors_detail ,name = 'doctors_detail'),
    path('login/',views.doctor_login,name = 'login'),
    path('myProfile/',views.doc_Porfile,name = 'myProfile'),
]