from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.managers import ProxyUserManager


class Citizen(User):
    objects = ProxyUserManager()

    class Meta:
        proxy = True


class Job(models.Model):
    name = models.CharField(_("name"), max_length=150, unique=True)
    photo = models.ImageField(_('Photo'), null=True, blank=True, upload_to="jobs")

    class Meta:
        verbose_name = _("Job")
        verbose_name_plural = _("Jobs")

    def __str__(self):
        return self.name
