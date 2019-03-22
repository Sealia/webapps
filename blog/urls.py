from django.urls import path

from . import views

app_name='blog'
urlpatterns = [

    path('', views.post_list_view, name='post_list_view'),
    path('category/<category_name>/', views.post_category_view, name="post_list_category"),
    path('post/<post_id>/', views.post_detail_view, name='post_detail_view'),
  
]
