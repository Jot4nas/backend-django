from rest_framework import serializers
from ..models import CustomUser

#End point para JSON
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('pk', 'email', 'username', 'email_verified')


# profile/serializers.py
from rest_framework import serializers
from allauth.account.adapter import get_adapter
from dj_rest_auth.registration.serializers import RegisterSerializer

class CustomRegisterSerializer(RegisterSerializer):
    email = serializers.EmailField(required=True)

    def validate_email(self, email):
        allowed_domain = 'aluno.unb.br'
        domain = email.split('@')[1]
        if domain != allowed_domain:
            raise serializers.ValidationError('Utilize o email da UnB.')
        return email
