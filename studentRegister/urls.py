from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.student_form,name='student_insert'),
   path('<int:id>/',views.student_form,name='student_update'),
   path('delete/<int:id>/',views.student_delete,name='student_delete'),
   path('list/',views.student_list,name='student_list')
]