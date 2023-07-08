from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=1028)

    def __str__(self) -> str:
        return self.title

class VideoPart(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='video_parts')
    start_time = models.IntegerField()
    stop_time = models.IntegerField()
    description = models.TextField(max_length=1028)

    def __str__(self) -> str:
        return f'{self.video} ({self.start_time} - {self.stop_time})'