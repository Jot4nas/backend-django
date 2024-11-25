from django.db import models
from uuid import uuid4
from django.contrib.auth.hashers import make_password, check_password

class Register(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length= 80, unique=True)
    password = models.CharField(max_length= 180)
    create_at = models.DateField(auto_now_add= True)

    def set_password(self, raw_password): 
        self.password = make_password(raw_password) 
        
    def check_password(self, raw_password): 
        return check_password(raw_password, self.password)

