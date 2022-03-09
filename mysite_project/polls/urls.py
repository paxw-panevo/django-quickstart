from django.urls import path

from . import views

# This is used for namespacing purposes.
# https://docs.djangoproject.com/en/3.2/intro/tutorial03/#namespacing-url-names
app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.question_detail, name="detail"),
    path('<int:question_id>/results', views.question_results, name="results"),
    path('<int:question_id>/vote', views.question_vote, name="vote"),
]
