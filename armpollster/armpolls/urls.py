from django.urls import path

from armpolls import views

app_name = 'armpolls'

urlpatterns = [
    path('', views.index , name='index'),
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/results', views.results, name='results'),
]