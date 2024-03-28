from django.urls import path
from . import views

urlpatterns = [
    path('parsing/', views.ParsingView.as_view()),
    path('houses/', views.HouseListView.as_view()),
    path('bazar/', views.ItemListView.as_view()),
]