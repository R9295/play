from .models import Server, Hero, Role, UserProfile
from rest_framework.serializers import ModelSerializer
from django.core.exceptions import ValidationError
class ServerSerializer(ModelSerializer):
    class Meta:
        model = Server
        fields = '__all__'

class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class HeroSerializer(ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'

class UserProfileSerializer(ModelSerializer):
        
    def save(self, **kwargs):
        # check if user saving is the one actually saving it
        if self.context.get('request'):
            if self.context['request'].user != self.validated_data.get('user'):
                raise ValidationError("You do not have the permission to create or update resources")
        else:
            raise ValidationError("Login maybe?")
        return super().save(**kwargs)

    class Meta:
        model = UserProfile
        fields = '__all__'
