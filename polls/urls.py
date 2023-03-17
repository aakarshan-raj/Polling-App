from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('<int:question_id>/',views.details,name="details"),
    path('<int:question_id>/result/',views.result,name="result"),
    path('<int:question_id>/vote/',views.vote)
]
