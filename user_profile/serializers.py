from .models import Server, Hero, Role, UserProfile
from rest_framework.serializers import ModelSerializer, ValidationError,SlugRelatedField
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
    fav_servers = SlugRelatedField(
        many=True,
        queryset=Server.objects.all(),
        slug_field='name',
    )

    fav_roles = SlugRelatedField(
        many=True,
        queryset=Role.objects.all(),
        slug_field='name',
    )

    fav_heroes = SlugRelatedField(
        many=True,
        queryset=Hero.objects.all(),
        slug_field='name',
    )
    def validate_fav_servers(self, value):
        if len(value) > 3:
            raise ValidationError("Too many servers selected, maximum is 3")
        return value

    def validate_fav_heroes(self, value):
        if len(value) > 5:
            raise ValidationError("Too many heroes selected, maximum is 5")
        return value

    def validate_fav_roles(self, value):
        if len(value) > 3:
            raise ValidationError("Too many roles selected, maximum is 3")
        return value
    # check if the user is logged in
    def validate_user(self, value):
        if self.context.get('request'):
              if self.context['request'].user != value:
                raise ValidationError("You do not have the permission to create or this resource")
        else:
            raise ValidationError("Login?")
        return value
    class Meta:
        model = UserProfile
        fields = ('fav_servers', 'fav_heroes', 'id', 'fav_roles')
