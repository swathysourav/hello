
from django.urls import path
from . import views
from .views import  PostDetailView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('',views.list_view,name='movie-home'),
     path('review/',views.Review_view,name='rate-review'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/<int:pk>/review',views.review_form,name='post-review'),
     # path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/new',views.upload_form,name='post-create'),
    path('post/<int:pk>/update',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name='post-delete'),
    path('search/',views.SearchResult,name='post-search'),

]
