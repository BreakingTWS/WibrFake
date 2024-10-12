from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
	username = models.CharField(max_length=255, unique=True)
	password = models.CharField(max_length=255)
	groups = models.ManyToManyField('auth.Group', related_name='usuario_groups')
	user_permissions = models.ManyToManyField('auth.Permissions', related_name='usuario_permissions')
	def __str__(self):
		return self.username
