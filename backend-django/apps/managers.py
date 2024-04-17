from django.db import models


class ProxyUserManager(models.Manager):
    def get_queryset(self):
        return super(ProxyUserManager, self).get_queryset().filter(is_superuser=False, is_staff=False)