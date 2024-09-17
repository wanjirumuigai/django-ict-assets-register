from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='index'),
    path('assets/', views.assets, name='assets'),
    path('assets/delete/<int:pk>/', views.asset_delete, name='assets-delete'),
    path('assets/edit/<int:pk>/', views.asset_edit, name='assets-edit'),
    path('staff/view/<int:pk>/', views.staff_detail, name='staff-detail'),
    path('assets/list', views.all_assets, name='assets-list'),
    path('staff/', views.staff, name='staff'),
    path('desktops/', views.desktops, name='desktops'),
    path('laptops/', views.laptops, name='laptops'),
    path('licenses/', views.licenses, name='licenses'),
    path('obsolete/', views.obsolete, name='obsolete'),
    path('requests/', views.requests, name='requests'),
]

