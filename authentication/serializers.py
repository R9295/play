from rest_framework.serializers import ModelSerializer, SerializerMethodField
from authentication.models import User
from user_profile.serializers import UserProfileSerializer
from user_profile.models import UserProfile


class UserSerializer(ModelSerializer):
    dota_id = SerializerMethodField()
    profile = SerializerMethodField()

    def get_dota_id(self, obj):
        return obj.dotaid

    def get_profile(self, obj):
        try:
            profile = UserProfile.objects.get(user=obj)
            serializer = UserProfileSerializer(profile)
            return serializer.data
        except UserProfile.DoesNotExist:
            return 'None'

    class Meta:
        model = User
        fields = ['personaname', 'pk', 'last_login', 'date_joined', 'profileurl', 'avatarfull', 'dota_id', 'profile']
