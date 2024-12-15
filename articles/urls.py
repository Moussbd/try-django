from django.urls import path 

from .views import (
    article_list_view,
    article_detail_view,
    article_search_view,
    article_create_view
)

app_name = 'articles'

urlpatterns = [
    path('', article_list_view, name="list"),
    path('search/', article_search_view, name="search"),
    path('create/', article_create_view, name="create"),
    path('<int:id>/', article_detail_view, name="detail"),
]
