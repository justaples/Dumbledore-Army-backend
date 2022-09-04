from django.shortcuts import render
from da.serializers import MemberSerializer, SpellSerializer
from .models import Member, Spell
from django.http import JsonResponse
from rest_framework import generics
# Create your views here.

class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class SpellList(generics.ListCreateAPIView):
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer
    
class SpellDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer