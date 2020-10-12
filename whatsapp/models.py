from django.db import models
from django.contrib.auth.models import Group
from django.urls import reverse


class ChatGroup(Group):
    """" Extends the group models to add more information """
    description  = models.TextField(blank=True,help_text="the description")
    mute_notifications  = models.TextField(blank=True,help_text="disable thr group")
    icon  = models.ImageField(helper_text="Group Icon" blank=True,upload_to="icons")
    date_created  = models.DateField(auto_now_add=True)
    date_modified  = models.DateField(auto_now==True)

    def get_absolute_url(self):
        return reverse('chat:room',args=[str(self.id)])

