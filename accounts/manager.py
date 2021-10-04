from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """
        Creates a new user and saves name and password along with extra fields.
        """
        if not username:
            raise ValueError('Username is required')

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # I used this class to create simple User and setdefault is add default fields to extra_fields . . .
    # if we need login with email we have to declare email instead of username
    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    # I used this class to create Super User and setdefault is add default fields to extra_fields . . .
    # if we need login with email we have to declare email instead of username
    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username, password, **extra_fields)
