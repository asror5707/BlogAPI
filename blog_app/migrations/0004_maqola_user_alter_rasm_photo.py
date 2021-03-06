# Generated by Django 4.0 on 2022-01-28 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('blog_app', '0003_alter_rasm_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='maqola',
            name='user',
            field=models.ForeignKey(default=1000, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rasm',
            name='photo',
            field=models.FileField(upload_to='static/media/'),
        ),
    ]
