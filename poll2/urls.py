from django.urls import path

from . import views

app_name = 'poll2'
urlpatterns = [
    # ex : /poll2/
    path('', views.IndexView.as_view(), name='index'),
    # ex : /poll2/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex : /poll2/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex : /poll2/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]