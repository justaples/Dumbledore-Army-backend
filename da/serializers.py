from rest_framework import serializers
from .models import Member, Spell

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    spells = serializers.HyperlinkedRelatedField(
        view_name = 'spell_detail',
        # many = True,
        read_only = True
    )

    class Meta:
        model = Member
        fields = ('id', 'name', 'age', 'picture', 'house',
        'spells'
        )
    
class SpellSerializer(serializers.HyperlinkedModelSerializer):
    members = serializers.HyperlinkedRelatedField(
        view_name = 'member_detail',
        many = True,
        read_only = True
    )

    class Meta:
        model = Spell
        fields = ('id', 'spell','type','use', 'effect', 'members')
        
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
