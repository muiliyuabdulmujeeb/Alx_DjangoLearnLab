from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser

# Create your models here.

class BlogUserManager(BaseUserManager):
    """The custom user manager to be used to extend the user creation functionality below"""

    def create_user(self, first_name, last_name, email, password, username=None, bio="", **extra_fields):
        """For creating a user, first_name, last_name, username, email and password must be provided upon sign up. bio can be added later"""

        if not first_name:
            raise ValueError("First name must be provided for signup")
        if not last_name:
            raise ValueError("Last mane must be provided for signup")
        if not email:
            raise ValueError("Provide a valid email address for signup")
        if not password:
            raise ValueError("input a password for account security")
        
        email= self.normalize_email(email= email)
        user = self.model(
            first_name= first_name,
            last_name= last_name,
            username= username,
            bio= bio,
            **extra_fields
        )
        user.set_password(password)
        user.save(using= self._db)
        return user
    
    def create_superuser(self, first_name, last_name, email, password, username=None, bio="", **extra_fields):
        """For creating a user, first_name, last_name, username, email and password must be provided upon sign up. bio can be added later"""

        user = self.create_user(
            first_name= first_name,
            last_name= last_name,
            email= email,
            password= password,
            username= username,
            bio= bio,
            **extra_fields
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using= self._db)
        return user
    

class BlogUser(AbstractUser):
    first_name= models.CharField(max_length= 50)
    last_name= models.CharField(max_length= 50)
    email= models.EmailField(max_length= 80, unique= True)
    username= models.CharField(max_length= 15, unique= True)
    bio= models.TextField()

    objects = BlogUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS= ["first_name", "last_name", "username"]

    def __str__(self):
        return self.username