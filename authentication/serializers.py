from rest_framework.serializers import ModelSerializer, SerializerMethodField
from authentication.models import User

class UsrSerializer(ModelSerializer):
    dota_id = SerializerMethodField()
    def get_dota_id(self, obj):
        return obj.dotaid

    class Meta:
        model = User
        fields = ['personaname', 'pk', 'last_login', 'date_joined', 'profileurl', 'avatarfull', 'dota_id']
