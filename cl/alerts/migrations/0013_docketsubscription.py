# Generated by Django 3.1.7 on 2021-05-25 19:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0101_remove_indexes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alerts', '0012_abstract_datetime_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocketSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True, help_text='The moment when the item was created.')),
                ('date_modified', models.DateTimeField(auto_now=True, db_index=True, help_text='The last moment when the item was modified. A value in year 1750 indicates the value is unknown')),
                ('date_last_hit', models.DateTimeField(blank=True, help_text='The last date on which an email was received for the case.', null=True)),
                ('secret_key', models.CharField(help_text='A key to be used in links to access the alert without having to log in. Can be used for a variety of purposes.', max_length=40)),
                ('docket', models.ForeignKey(help_text='The docket that we are subscribed to.', on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='search.docket')),
                ('user', models.ForeignKey(help_text='The user that is subscribed to the docket.', on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('docket', 'user')},
            },
        ),
    ]