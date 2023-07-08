# Generated by Django 4.2.3 on 2023-07-08 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_videopart_start_time_videopart_stop_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videopart',
            name='video_id',
        ),
        migrations.AddField(
            model_name='videopart',
            name='video',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='video_parts', to='core.video'),
            preserve_default=False,
        ),
    ]