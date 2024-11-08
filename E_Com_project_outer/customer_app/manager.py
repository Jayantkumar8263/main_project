from django.contrib.auth.base_user import BaseUserManager

class custom_userManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Please enter your email if not create one')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if not password:
            raise ValueError('Superuser must have a password')
        
        user = self.create_user(email, password, **extra_fields)
        user.save(using=self._db)
        return user