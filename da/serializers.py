from rest_framework import serializers
from .models import Member, Spell
from django.contrib.auth import get_user_model
import django.contrib.auth.password_validation as validations
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
User = get_user_model()

class MemberSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Member
        fields = ('id', 'name', 'age', 'picture', 'house',)
    
class SpellSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Spell
        fields = ('id', 'spell','type','use', 'effect', )
        # fields='__all__'

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):

        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError({'password_confirmation': 'Passwords do not match'})

        # try:
        #     validations.validate_password(password=password)
        # except ValidationError as err:
        #     raise serializers.ValidationError({'password': err.messages})

        data['password'] = make_password(password)
        return data

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirmation',)







# # code below is original - do not change or remove
# class MemberSerializer(serializers.HyperlinkedModelSerializer):
#     spells = serializers.HyperlinkedRelatedField(
#         view_name = 'spell_detail',
#         # many = True,
#         read_only = True
#     )

#     class Meta:
#         model = Member
#         fields = ('id', 'name', 'age', 'picture', 'house',
#         'spells'
#         )
    
# class SpellSerializer(serializers.HyperlinkedModelSerializer):
#     # members = serializers.HyperlinkedRelatedField(
#     #     view_name = 'member_detail',
#     #     many = True,
#     #     read_only = True
#     #     lookup_field = 'members'
#     # )
#     members = MemberSerializer(many=True)
    
#     class Meta:
#         model = Spell
#         fields = ('id', 'spell','type','use', 'effect', 'members')
#         # fields='__all__'


















# class MemberSerializer(serializers.ModelSerializer):
#     spells = serializers.PrimaryKeyRelatedField(
#         queryset = Spell.objects.all(),
#         many = True,
#         # read_only = True
#     )

#     class Meta:
#         model = Member
#         fields = ('id', 'name', 'age', 'picture', 'house', 'spells')
    
# class SpellSerializer(serializers.ModelSerializer):
#     members = MemberSerializer(
#         # view_name = 'member_detail',
#         many = True,
#         read_only = True
#     )

#     class Meta:
#         model = Spell
#         fields = ('id', 'spell','type','use', 'effect', 'members')
