from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    # path('test',views.test,name='test'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('all_post/', views.SeePostView.as_view(), name='see_post'),
]
