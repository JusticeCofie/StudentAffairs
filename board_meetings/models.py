from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _

class Meeting(models.Model):
    class Status(models.IntegerChoices):
        SPECIAL = 1, 'Special'
        REGULAR = 2, 'Regular'
    

    description = models.CharField(max_length=255, help_text='Meeting Description')
    document = models.FileField(upload_to='meetings/documents/')
    publish = models.DateTimeField(_("Published Date"),blank=True, null=True, default=timezone.now)
    status = models.PositiveIntegerField(choices=Status.choices, blank=True, null=True)

    class Meta:
        verbose_name = _('Meeting')
        verbose_name_plural = _('Meetings')
        ordering = ['-publish',]

    def __str__(self):
        return self.description