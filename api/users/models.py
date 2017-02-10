from django.contrib.auth.models import User

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    public = models.BooleanField(default=True)

    class __str__():
        return self.user.username
