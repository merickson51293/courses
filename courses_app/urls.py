from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new_course', views.new_course),
    path('maybe_delete/<int:course_id>', views.maybe_delete),
    path('delete/<int:course_id>', views.delete_course)
]