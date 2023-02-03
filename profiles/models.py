from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    PIZZA_MAKER = 'Pizza Maker'
    PIZZA_EATER = 'Pizza Eater'
    PIZZA_MAKER_OR_PIZZA_EATER_CHOICES = [
        (PIZZA_EATER, 'Pizza Eater'),
        (PIZZA_MAKER, 'Pizza Maker'),
    ]
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=150, blank=True)
    about = models.TextField(
        max_length=350, default="All about me", blank=True
    )
    maker_or_eater = models.CharField(
        choices=PIZZA_MAKER_OR_PIZZA_EATER_CHOICES,
        max_length=15,
        default=PIZZA_EATER
    )
    image = models.ImageField(
        upload_to='images/', default='../profile-icon_pqik1e'
    )
    favourite_pizza = models.CharField(
        max_length=25, default="Margherita", blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s Profile"


# Function taken from walkthrough project
def create_profile(sender, instance, created, **kwargs):
    ''' Ensure a profile is created for each user created '''
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
