from django.urls import path
from . import views

urlpatterns = [
path("", views.index, name="index"),
path("delete/<int:id>", views.delete_student, name="deleted_student"),
path("update/<int:id>", views.update_student, name="updated_student"),
path("do-update/<int:id>", views.do_update_student, name="do_updated_student"),
 path('update-click-count/<int:student_id>/<str:subject>/', views.update_click_count, name='update_click_count'),
 path('update-longpress/<int:student_id>/<str:subject>/<int:circle>/', views.update_longpress, name='update_longpress'),
]