from rest_framework import serializers
from profileAuth import models
import re

class RegisterSerializers(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = models.Register
        fields = ['email', 'username', 'password', 'id']

    def validate_email(self, value):
        domain = "aluno.unb.br"

        if not isinstance(value, str):
            raise serializers.ValidationError("Formato do email inválido.")
        
        # Verificação do domínio
        if not value.endswith(f"@{domain}"):
            raise serializers.ValidationError(f"O email deve pertencer ao domínio @{domain}.")
        
        return value
    
    def validate_password(self, value):
        # Verificação do tamanho mínimo
        if len(value) < 8:
            raise serializers.ValidationError("A senha deve conter no mínimo 8 caracteres.")
        # Verifica se possui número
        if not re.search(r'\d', value):
            raise serializers.ValidationError("A senha deve conter ao menos um número.")

        return value

    def create(self, validated_data):
        email = validated_data.get('email')
        username = validated_data.get('username')

        # Verificar se o email ou o username já estão em uso
        if models.Register.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "Este endereço de email já está em uso."})
        
        if models.Register.objects.filter(username=username).exists():
            raise serializers.ValidationError({"username": "Este usuário já está em uso."})

        # Criação do usuário
        user = models.Register(
            email=validated_data['email'],
            username=validated_data['username']
        )
        
        # Definindo a senha com o método set_password
        user.set_password(validated_data['password'])
        user.save()  # Chama o save normalmente

        return user



    # O método update é desnecessário se você não está tratando atualizações de forma customizada.
    # Caso deseje usá-lo, faça isso de forma completa e apenas se necessário.
    # def update(self, instance, validated_data):
    #     if 'password' in validated_data:
    #         instance.set_password(validated_data['password'])
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.save()
    #     return instance
