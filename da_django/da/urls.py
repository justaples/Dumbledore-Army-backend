from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('members/', views.MemberList.as_view(), name='member_list'),
    path('members/<int:pk>/', views.MemberDetail.as_view(), name='member_detail'),
    path('spells/', views.SpellList.as_view(), name='spell_list'),
    path('spells/<int:pk>/', views.SpellDetail.as_view(), name='spell_detail'),
]
