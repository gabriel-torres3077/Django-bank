from django.db import models
from django.contrib.auth import models as auth_models
from .constants import GENDER_CHOICE 

class UserManager(auth_models.BaseUserManager):
    
    def create_user(self, email: str, cpf: str, first_name: str, last_name: str, password: str, **extra_fields) -> "User":
        if not email:
            raise ValueError("O Usuário deve ter um email")
        if not first_name:
            raise ValueError("O Usuário deve ter um nome")
        if not last_name:
            raise ValueError("O Usuário deve ter um sobrenome")
        if not cpf:
            raise ValueError("O Usuário deve ter um CPF")
        
        
        email=self.normalize_email(email)
        user = self.model(
            email = email,
            first_name = first_name,
            last_name = last_name,
            cpf = cpf,
            **extra_fields
            )
        
        user.set_password(password)

        user.save()

        return user
    
    def create_superuser(self, email: str, cpf: str, password: str, first_name: str, last_name: str, **extra_fields) -> "User":
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("O Administrador precisa ter o campo 'is_staff' como Verdadeiro")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("O Administrador precisa ter o campo 'is_superuser' como Verdadeiro")
        
        return self.create_user(
            email=email,
            cpf=cpf,
            password=password,
            first_name=first_name,
            last_name=last_name,
            **extra_fields, 
        )


# Create your models here.
class User(auth_models.AbstractUser):
    email = models.EmailField(verbose_name="Email", max_length=255, unique=True)
    cpf = models.CharField(verbose_name="CPF", max_length=11, unique=True)
    birth = models.DateField(verbose_name="Data de nascimento")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    phone = models.CharField(verbose_name="Telefone", max_length=11)
    password = models.CharField(max_length=255)
    first_name = models.CharField(verbose_name="Nome", max_length=255)
    last_name = models.CharField(verbose_name="sobrenome", max_length=255)
    username = None


    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "cpf", "birth", "phone", "gender"]

    def __str__(self):
        return self.email