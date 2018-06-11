from rest_framework.serializers import ModelSerializer, SerializerMethodField,PrimaryKeyRelatedField
from authentication.models import User
from user_profile.serializers import UserProfileSerializer
from user_profile.models import UserProfile


class UserSerializer(ModelSerializer):
    dota_id = SerializerMethodField()
    profile = UserProfileSerializer()

    def get_dota_id(self, obj):
        return obj.dotaid

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.get(pk=instance.pk)
        if self.context.get('create'):
            profile = UserProfileSerializer.create(UserProfileSerializer(), validated_data=profile_data)
        if self.context.get('update'):
            profile = UserProfileSerializer.update(UserProfileSerializer(), instance=instance.profile, validated_data=profile_data)
        profile.save()
        user.profile = profile
        user.save()
        return user

    class Meta:
        model = User
        fields = [ 'pk', 'last_login', 'date_joined', 'profileurl', 'avatarfull', 'dota_id', 'profile']
