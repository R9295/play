from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Invite
from authentication.models import User

class InviteSerializer(ModelSerializer):
    user_from_slug = SerializerMethodField()
    user_to_slug = SerializerMethodField()

    def get_user_from_slug(self, obj):
        return User.objects.get(pk=obj.user_from.pk).personaname

    def get_user_to_slug(self, obj):
        return User.objects.get(pk=obj.user_to.pk).personaname

    class Meta:
        model = Invite
        fields = '__all__'
