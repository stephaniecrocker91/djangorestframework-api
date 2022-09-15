from django.urls import path
from followers import views

urlpatterns = [
    path('followers/', views.LikeList.as_view()),
    path('followers/<int:pk>/', views.LikeDetail.as_view()),
]