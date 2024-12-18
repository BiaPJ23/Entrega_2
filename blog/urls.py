from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('list/', views.post_list, name='list_post'),
    path('<int:pk>/', views.post_detail, name='detail_post'),
    path('create/', views.post_create, name='create_post'),
    path('<int:pk>/edit/', views.post_update, name='edit_post'),
    path('<int:pk>/delete/', views.post_delete, name='delete_post'),
    path('<int:id>/add_comment/', views.add_comment, name='add_comment'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:id>/', views.category_detail, name='category_detail'),
]
