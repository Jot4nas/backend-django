from dj_rest_auth.registration.views import RegisterView
from profileAuth.API.serializers import RegisterSerializers  # Importando o seu serializer personalizado
from django.conf import settings
from django.http import HttpResponseRedirect


class CustomRegisterView(RegisterView):
    # Especifica o serializer que será usado
    serializer_class = RegisterSerializers

    def perform_create(self, serializer):
        # Garantir que o `request` seja passado corretamente para o `save`
        return serializer.save(request=self.request)
    
from allauth.account.signals import user_logged_in
from django.dispatch import receiver

@receiver(user_logged_in)
def user_logged_in_receiver(request, user, **kwargs):
    print(f'Usuário {user.email} logado e e-mail confirmado!')


# authentication/views.py
def email_confirm_redirect(request, key):
    return HttpResponseRedirect(
        f"{settings.EMAIL_CONFIRM_REDIRECT_BASE_URL}{key}/"
    )


def password_reset_confirm_redirect(request, uidb64, token):
    return HttpResponseRedirect(
        f"{settings.PASSWORD_RESET_CONFIRM_REDIRECT_BASE_URL}{uidb64}/{token}/"
    )
