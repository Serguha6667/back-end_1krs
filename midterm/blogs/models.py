from django.db import models

# Create your models here.
class Bloq (models.Model):
    title = models. CharField(max_Length=255, nUll=False)
    description = models. CharField (max_length=255, null=True)
    owner = models. CharField(max_Length=255, null=False)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return 'ID: {}, Name: {}'.format(self.id, self.name)

