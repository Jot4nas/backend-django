from rest_framework import serializers
from account import models
import re

class RegisterSerializers(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only= True)
    
    class Meta:
        model = models.Register
        fields = ['email', 'username', 'password']

#Requisitos do email#

    def validate_email(self, value):
        domain = "aluno.unb.br"

        if not isinstance(value, str):
            raise serializers.ValidationError("Formato do email inválido.")
        
        #Verificação do domínio
        if not value.endswith(f"@{domain}"):
            raise serializers.ValidationError(f"O email deve pertencer ao domínio @{domain}.")
        
        return value
    
    def validate_password(self, value):
        #Verificação do tamanho mín
        if len(value) < 8:
            raise serializers.ValidationError("A senha deve conter no mínimo 8 caracteres.")
        #Verifica se possue numero
        if not re.search(r'\d', value):
            raise serializers.ValidationError("A senha deve conter ao menos um número.")
    
    def create(self, validated_data):
        email = validated_data.get('email')
        username = validated_data.get('username')

        if models.Register.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "Este endereço de email já está em uso." })
        
        if models.Register.objects.filter(username=username).exists():
            raise serializers.ValidationError({"username": "Este usuário já está em uso." }) 

        user = models.Register(
            email = validated_data['email'],
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])

        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance    

