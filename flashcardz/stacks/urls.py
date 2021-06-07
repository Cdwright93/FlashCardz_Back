from django.urls import path
from . import views

urlpatterns = [
    path('', views.StackList.as_view()),
    path('<int:pk>', views.StackDetail.as_view()),
]