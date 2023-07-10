# Generated by Django 4.2.3 on 2023-07-06 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_alter_post_author'),
        ('users', '0005_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_posts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_posts', to='posts.post'),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
