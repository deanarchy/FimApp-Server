from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('Email address must be filled')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('Email address must be filled')

        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        primary_key=True,
    )
    
    first_name = models.CharField(
        verbose_name='first name',
        max_length=255,
    )

    last_name = models.CharField(
        verbose_name='last name',
        max_length=255,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin
    

class Budget(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    
    free_amount = models.FloatField()
    dob = models.DateField()

    def __str__(self):
        return self.user.email

    
class Category(models.Model):
    name = models.CharField(max_length=255)
    amount = models.FloatField()
    budget = models.ForeignKey(
        Budget,
        on_delete=models.CASCADE,
        related_name='categories',
    )
        
    def __str__(self):
        return self.name


    class Meta:
        ordering = ['budget', 'amount']
        verbose_name_plural = 'categories'
    
