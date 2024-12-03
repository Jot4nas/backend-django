from rest_framework import serializers
from ..models import CustomUser
from allauth.account.adapter import get_adapter
from dj_rest_auth.registration.serializers import RegisterSerializer

#End point para JSON
# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ('pk', 'email', 'username', 'email_verified', 'lastName')



# profile/serializers.py


class CustomRegisterSerializer(RegisterSerializer):
    email = serializers.EmailField(required=True)
    lastName = serializers.CharField(required=True)
    nickName = serializers.CharField(required=True)

    def validate_email(self, email):
        allowed_domain = 'aluno.unb.br'
        domain = email.split('@')[1]
        if domain != allowed_domain:
            raise serializers.ValidationError('Utilize o email da UnB.')
        return email
    
    def save(self, request):
        user = super().save(request)

        user.lastName = self.data.get('lastName')
        user.nickName = self.data.get('nickName')
        user.save
        return user

