from rest_framework.serializers import ModelSerializer
from .models import Invite


class InviteSerializer(ModelSerializer):
    class Meta:
        model = Invite
        fields = '__all__'
