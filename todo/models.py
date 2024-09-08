from django.db import models
from django.utils.translation import gettext_lazy as _


class Task(models.Model):

    class TAGS(models.TextChoices):
        #(value, label):actual, displayed value
        PERSONAL = "Personal", _("personal")
        ERRAND = "Errand", _("errand")
        WORK = "Work", _("work")
        HOME = "Home", _("home")


    task = models.CharField(max_length=250)
    tag = models.CharField(
        max_length=8,
        choices=TAGS,
        default=TAGS.PERSONAL,
    )
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task
