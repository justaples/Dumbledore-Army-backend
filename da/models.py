from django.db import models
from django.urls import reverse

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    picture = models.TextField()
    house = models.CharField(
        max_length=20,
        # choices=HOUSE,
        # default="Choose your houses"
        )
    # spells = models.ManyToManyField(Spell)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('member_detail', kwargs={'pk': self.id})

class Spell(models.Model):
    spell = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    use = models.CharField(max_length=50)
    effect = models.TextField()
    # members = models.ManyToManyField(Member, related_name='members', blank=True)

    def __str__(self):
        return self.spell

    def get_absolute_url(self):
        return reverse('detail', kwargs={'spell_id': self.id})






# code below is the original - do not change or remove

# # HOUSE =(
# #     ('Gryffindor', 'Gryffindor'),
# #     ('Ravenclaw', 'Ravenclaw'),
# #     ('Hufflepuff', 'Hufflepuff'),
# #     ('Slytherin', 'Slytherin'),
# # )

# class Member(models.Model):
#     name = models.CharField(max_length=50)
#     age = models.IntegerField()
#     picture = models.TextField()
#     house = models.CharField(
#         max_length=20,
#         # choices=HOUSE,
#         # default="Choose your houses"
#         )
#     # spells = models.ManyToManyField(Spell)

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse('member_detail', kwargs={'pk': self.id})

# class Spell(models.Model):
#     spell = models.CharField(max_length=50)
#     type = models.CharField(max_length=50)
#     use = models.CharField(max_length=50)
#     effect = models.TextField()
#     members = models.ManyToManyField(Member, related_name='members', blank=True)

#     def __str__(self):
#         return self.spell

#     def get_absolute_url(self):
#         return reverse('detail', kwargs={'spell_id': self.id})

        