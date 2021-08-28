# Generated by Django 3.2.6 on 2021-08-27 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20210823_2212'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RegisteredUser',
        ),
        migrations.AddField(
            model_name='event',
            name='register',
            field=models.ManyToManyField(related_name='Registered_students', to='events.ClubUser'),
        ),
    ]