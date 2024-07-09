from django.db import models

class User(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    profile_picture = models.URLField()
    date_joined = models.DateTimeField()

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

    class Meta:
        db_table = 'core_user'