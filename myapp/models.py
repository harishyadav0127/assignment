from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CreateQueryModel(models.Model):
    # user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    query = models.TextField(max_length=50, blank=True, null=True)

    # response = models.TextField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.query


class CreateUserQueryModel(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    query = models.TextField(max_length=50, blank=True, null=True)
    response = models.TextField(max_length=50, blank=True, null=True)

    # created = models.DateTimeField(auto_now_add=True, null=True)

    def __unicode__(self):
        return unicode(self.user)
