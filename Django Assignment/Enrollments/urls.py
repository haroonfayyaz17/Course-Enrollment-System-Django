from django.urls import path
from .import views

urlpatterns = [
    path('enrollment/create', views.create.as_view(), name='create'),
    path('enrollment/', views.listView.as_view(), name='listView'),
    path('enrollment/<pk>', views.detailView.as_view(), name='detailView'),
    path('enrollment/update/<pk>', views.update.as_view(), name='update'),
    path('enrollment/delete/<pk>', views.delete.as_view(), name='delete'),
]
