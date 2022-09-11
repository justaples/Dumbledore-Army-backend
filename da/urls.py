from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     # members
#     path('members/', views.MemberList.as_view(), name='member_list'),
#     path('members/<int:pk>/', views.MemberDetail.as_view(), name='member_detail'),


#     # spells
#     path('spells/', views.SpellList.as_view(), name='spell_list'),
#     path('spells/<int:pk>/', views.SpellDetail.as_view(), name='spell_detail'),
#     path('spells/create/', views.SpellCreate.as_view(), name='spell_create'),
#     path('spells/<int:pk>/update/', views.SpellUpdate.as_view(), name='spell_update'),
#     path('spells/<int:pk>/delete/', views.SpellDelete.as_view(), name='spell_delete'),
#     path('spells/<int:spell_id>/assoc_member/<int:member_id>/', views.SpellView.as_view(), name='SpellView'),

# ]





# code below is original - do not change or remove


urlpatterns = [
    path('members/', views.MemberList.as_view(), name='member_list'),
    path('members/<int:pk>/', views.MemberDetail.as_view(), name='member_detail'),
    path('spells/', views.SpellList.as_view(), name='spell_list'),
    path('spells/<int:pk>/', views.SpellDetail.as_view(), name='spell_detail'),
    path('register/', views.RegisterView.as_view(), name = 'register'),
    path('login/', views.LoginView.as_view(), name = 'login')
]
