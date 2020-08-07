from django.contrib import admin
from .models import Profile, FriendshipRelations, UsersInvitations
# Register your models here.
admin.site.register(Profile)
admin.site.register(FriendshipRelations)
admin.site.register(UsersInvitations)
