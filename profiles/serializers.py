from rest_framework import serializers
from .models import Profile


# Serializer takend and modified from walkthrough project
class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'about', 'maker_or_eater', 'image', 'favourite_pizza',
        ]
