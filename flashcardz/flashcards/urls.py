from django.urls import path
from . import views

urlpatterns = [
    path('', views.CardList.as_view()),
    path('<int:pk>/', views.CardDetail.as_view()),
    path('stack/<int:stack_id>/', views.CardCollection.as_view()),
]
