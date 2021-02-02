from django.urls import path
from .import views

urlpatterns = [
    path('course/create', views.create.as_view(), name='create'),
    path('course/', views.listView.as_view(), name='listView'),
    path('course/<pk>', views.detailView.as_view(), name='detailView'),
    path('course/update/<pk>', views.update.as_view(), name='update'),
    path('course/delete/<pk>', views.delete.as_view(), name='delete'),
]
