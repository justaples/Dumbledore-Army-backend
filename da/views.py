from django.shortcuts import render, redirect
from rest_framework.views import APIView
from da.serializers import MemberSerializer, SpellSerializer, MeetingSerializer
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Member, Spell, Meeting
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt
from .serializers import UserSerializer
User = get_user_model()
# Create your views here.

# # code below is original - don't change or remove 
# *---- Views for Members and Spells models ----*
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

class MeetingList(generics.ListCreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    
# class MeetingDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Spell.objects.all()
#     serializer_class = SpellSerializer

    

# *---- Serializers for JWT Token Auth ----*
class RegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration successful'})

        return Response(serializer.errors, status=422)


class LoginView(APIView):

    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise PermissionDenied({'message': 'Invalid credentials'})

    def post(self, request):

        email = request.data.get('email')
        password = request.data.get('password')

        user = self.get_user(email)
        if not user.check_password(password):
            raise PermissionDenied({'message': 'Invalid credentials'})

        token = jwt.encode({'sub': user.id}, settings.SECRET_KEY, algorithm='HS256')
        return Response({'token': token, 'message': f'Welcome back {user.username}!'})









# do not remove code below yet


# class SpellList(generics.ListAPIView):
#     queryset = Spell.objects.all()
#     serializer_class = SpellSerializer

# class SpellDetail(generics.RetrieveAPIView):
#     queryset = Spell.objects.all()
#     serializer_class = SpellSerializer

# class SpellCreate(CreateView):
#   model = Spell
#   fields = ['spell', 'type', 'use', 'effect', 'members']

# class SpellUpdate(UpdateView):
#   model = Spell
#   fields = ['spell', 'type', 'use', 'effect','members']

# class SpellDelete(DeleteView):
#   model = Spell
#   success_url = '/spells/'

# # def assoc_member(request, spell_id, member_id):
# #   Spell.objects.get(id=spell_id).members.add(member_id)
# #   return redirect('detail', spell_id=spell_id)

# class SpellView(APIView):
#     def post(self, request, spell_id, member_id):
#         Spell.objects.get(id=spell_id).members.add(member_id)
#         return redirect('detail', spell_id=spell_id)











    



