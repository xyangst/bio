from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    '''any user on buried'''
    backgroundImage = models.URLField(
        blank=True, null=True, default="")
    # stats
    views = models.PositiveIntegerField(default=0)
    # files
    pfpImage = models.URLField(blank=True, null=True, default="")
    bio = models.TextField(blank=True, null=True, max_length=500, default="")
    songLink = models.URLField(blank=True, null=True, default="")
    # customization
    displayName = models.TextField(blank=True, null=True, default="")
    textColor = models.CharField(max_length=7, default="#FFFFFF")

    # settings (boolean mostly)
    showViewCount = models.BooleanField(default=True)
    showSnowFlakes = models.BooleanField(default=False)
    showCard = models.BooleanField(default=False)


class SocialPlatform(models.Model):
    '''all platforms users are able to link to'''
    baseUrl = models.URLField(blank=True, null=True)
    platform = models.CharField(max_length=255)
    faClass = models.CharField(max_length=255)
    objects = models.Manager()
    isCopy = models.BooleanField(default=False)

    def __str__(self):
        return str(self.platform)


class SocialUser(models.Model):
    '''link between platform and user'''
    objects = models.Manager()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='socials')
    platform = models.ForeignKey(SocialPlatform, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str((self.platform.baseUrl or '') + self.name)

    class Meta:
        # Add this line to enforce the unique constraint
        unique_together = ('user', 'platform')


class UniqueLink(models.Model):
    '''one off link to a personal site from a user'''
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='links')
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=255)
