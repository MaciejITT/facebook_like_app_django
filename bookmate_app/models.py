from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Profile(models.Model):
    sexes = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Neither', 'Neither')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=200)
    sex = models.CharField(max_length=20, choices=sexes)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class FriendshipRelations(models.Model):
    status_list = (
        ('friend', 'friend'),
        ('unrelated', 'unrelated'),
        ('ignored', 'ignored'),
    )
    user = models.ForeignKey(User, related_name='invitation_sender', on_delete=models.CASCADE)
    user_friend = models.ForeignKey(User, related_name='invitation_receiver', on_delete=models.CASCADE)
    users_status = models.CharField(max_length=10, choices=status_list)
    relation_date = models.DateTimeField('relation_creation_date')

    def __str__(self):
        return self.user.username + '-' + self.user_friend.username + ': ' + self.users_status


class UsersInvitations(models.Model):
    invitation_status = (
        ('confirmed', 'confirmed'),
        ('rejected', 'rejected'),
        ('waiting', 'waiting'),
    )
    user = models.ForeignKey(User, related_name='user_invitation_sent', on_delete=models.CASCADE)
    user_invited = models.ForeignKey(User, related_name='user_invitation_receiver', on_delete=models.CASCADE)
    users_status = models.CharField(max_length=10, choices=invitation_status)
    relation_date = models.DateTimeField('relation_creation_date')

    def __str__(self):
        return self.user.username + '-' + self.user_invited.username + ': ' + self.users_status
