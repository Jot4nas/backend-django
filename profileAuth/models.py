from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
  # Importe o modelo ProfileAuth

class RegisterManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("O email é obrigatório")
        if not username:
            raise ValueError("O username é obrigatório")
        user = self.model(email=email, username=username)
        user.set_password(password)  # Certifique-se de que a senha é tratada corretamente
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email, username, password)
        user.is_admin = True
        user.is_staff = True  # Atribuindo ao superusuário a permissão de staff
        user.save(using=self._db)
        return user


class Register(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=80, unique=True)
    create_at = models.DateField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = RegisterManager()

    USERNAME_FIELD = 'email'  # ou 'email', dependendo de qual você quer usar
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
