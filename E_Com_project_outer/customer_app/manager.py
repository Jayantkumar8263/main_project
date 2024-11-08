from django.contrib.auth.base_user import BaseUserManager

class custom_userManager(BaseUserManager):
    
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Please enter your email if not create one')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff',  True)
        extra_fields.setdefault('is_superuser',  True)
        
        if password is None:
            raise ValueError('superuser must have a passward')
        user = self.model(email, password, **extra_fields)
        return user