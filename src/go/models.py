from django.db import models


class GoLink(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(unique=True, max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    hit_count = models.IntegerField(default=0)
    # TODO: Add owners support
    # owners = models.ManyToManyField('auth.User', related_name='redirects')

    def __str__(self):
        return self.short_url
