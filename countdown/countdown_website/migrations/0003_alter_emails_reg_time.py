# Generated by Django 4.1.1 on 2022-11-02 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countdown_website', '0002_emails_delete_eventcountdown'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emails',
            name='reg_time',
            field=models.TextField(),
        ),
    ]
