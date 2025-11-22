from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length= 200)
    author = models.CharField(max_length= 100)
    publication_year = models.IntegerField()

class CustomUserManager(BaseUserManager):

    #create user
    def create_user(self, username, first_name, last_name, email, date_of_birth, password, profile_photo=None):
        """ function to create a user"""

        if not username:
            raise ValueError("Username cannot be blank")
        if not first_name:
            raise ValueError("first_name cannot be blank")
        if not last_name:
            raise ValueError("last_name cannot be blank")
        if not email:
            raise ValueError("email cannot be blank")
        if not date_of_birth:
            raise ValueError("date_of_birth cannot be blank")
        
        if profile_photo:
            user = self.model(
                username= username,
                first_name= first_name,
                last_name= last_name,
                email= self.normalize_email(email= email),
                date_of_birth= date_of_birth,
                profile_photo= profile_photo
            )
        else:
            user = self.model(
                username= username,
                first_name= first_name,
                last_name= last_name,
                email= self.normalize_email(email= email),
                date_of_birth= date_of_birth
            )
        
        user.set_password(raw_password= password)
        user.save(using= self._db)
        return user
    
    #create super user
    def create_superuser(self, username, first_name, last_name, email, date_of_birth, password, profile_photo=None):
        """ function to call when a super user is to be created"""

        if profile_photo:
            user = self.create_user(
                username= username,
                first_name= first_name,
                last_name= last_name,
                email= email,
                date_of_birth= date_of_birth,
                password= password,
                profile_photo= profile_photo
            )
        else:
            user = self.create_user(
                username= username,
                first_name= first_name,
                last_name= last_name,
                email= email,
                date_of_birth= date_of_birth,
                password= password
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using= self._db)

        return user



class CustomUser(AbstractUser):
    date_of_birth= models.DateField()
    profile_photo= models.ImageField(blank= True)

    objects = CustomUserManager()


class Article(models.Model):
    title = models.CharField(max_length= 100)
    body = models.TextField()

    class Meta:
        permissions = [
            ("can_view", "can view articles"),
            ("can_create", "can create articles"),
            ("can_edit", "can edit articles"),
            ("can_delete", "can delete articles"),
        ]