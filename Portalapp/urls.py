from django.urls import path
from .views import  post_list, post_detail, tags_list

urlpatterns = [
    #path('c', CategoryListView.as_view(), name='base_view'),
    #path('category/<slug:slug>/', CategoryDetailView.as_view(), name = 'category_detail'),
    path('', post_list, name='post_list_url'),
    path('post/<str:slug>/', post_detail, name = 'post_detail_url'),
    path('tags/', tags_list, name='tags_list_url')
]
