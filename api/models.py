from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

def get_local_time():
    return timezone.localtime(timezone.now())

class Notification(models.Model):
    CHOICES = (
        ('LEAVE_APPROVED','Leave Approved'),
        ('LEAVE_CREATED','Leave Created'),
        ('LEAVE_REJECTED','Leave Rjected'),
        ('LEAVE_NEW','Leave New'),
        ('LEAVE_PENDING','Leave Pending'),
    )
    type = models.CharField(max_length=500, choices=CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    created = models.DateTimeField(default=get_local_time, editable=False)
    is_read = models.BooleanField(default=False)

    @classmethod
    def unread_count(obj, user, *args, **kwargs):
        return obj.objects.filter(user=user, is_read=False).count()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = get_local_time()
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.user.get_username() + " - " + self.type
    
    class Meta:
        ordering = ['-created']