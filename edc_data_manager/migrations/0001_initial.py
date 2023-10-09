# Generated by Django 3.1.4 on 2022-09-19 12:07

import _socket
import datetime
from django.db import migrations, models
import django.db.models.deletion
import django_crypto_fields.fields.encrypted_text_field
import django_revision.revision_field
import edc_base.model_fields.hostname_modification_field
import edc_base.model_fields.userfield
import edc_base.model_fields.uuid_auto_field
import edc_base.utils
import edc_data_manager.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataActionItem',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('subject_identifier', models.CharField(max_length=50, verbose_name='Subject Identifier')),
                ('slug', models.CharField(db_index=True, default='', editable=False, help_text='a field used for quick search', max_length=250, null=True)),
                ('subject', models.CharField(max_length=100, verbose_name='Issue Subject')),
                ('action_date', models.DateField(default=datetime.date.today, verbose_name='Action date')),
                ('comment', django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(blank=True, help_text=' (Encryption: AES local)', max_length=500)),
                ('display_on_dashboard', models.BooleanField(default=True)),
                ('issue_number', models.IntegerField(default=0, help_text='System auto field. Issue ref number.')),
                ('action_priority', models.CharField(choices=[('normal', 'Normal'), ('Medium', 'Medium'), ('high', 'High')], default='Normal', max_length=35)),
                ('assigned', models.CharField(max_length=50, verbose_name='Assign to')),
                ('status', models.CharField(choices=[('open', 'Open'), ('stalled', 'Stalled'), ('resolved', 'Resolved'), ('closed', 'Closed')], default='open', help_text="Only data managers or study physicians can 'close' an action item", max_length=35, verbose_name='Status')),
                ('subject_type', models.CharField(choices=[('infant', 'Infant'), ('maternal', 'Maternal'), ('subject', 'Subject')], default='subject', max_length=10)),
                ('site', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='sites.site')),
            ],
            bases=(edc_data_manager.models.ModelDiffMixin, models.Model),
        ),
    ]
