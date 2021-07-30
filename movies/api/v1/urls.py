from django.urls import path

from . import views

app_name = 'v1'

urlpatterns = [
    path("movie/", views.MovieListView.as_view()),
    path("movie/<int:pk>/", views.MovieDetailView.as_view())
]
