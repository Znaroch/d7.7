from django.urls import path
# Импортируем созданное нами представление
from .views import NewsList, NewsDetail, NewsSearch, NewsCreate, NewsEdit, NewsDelete


urlpatterns = [
    path('', NewsList.as_view(), name ='post_list'),
    path('<int:pk>', NewsDetail.as_view(), name ='post_detail'),
    path('search/', NewsSearch.as_view(), name ='post_search'),
    path('create/', NewsCreate.as_view(), name='post_create'),
    path('<int:pk>/edit/', NewsEdit.as_view(), name='post_edit'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='post_delete'),
]