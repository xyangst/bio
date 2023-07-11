from django.contrib import admin

# Register your models here.
from bio.models import User, SocialPlatform, SocialUser

admin.site.register(User)
admin.site.register(SocialPlatform)
admin.site.register(SocialUser)
