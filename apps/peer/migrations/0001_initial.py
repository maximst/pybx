# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import apps.peer.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(default='', unique=True, max_length=80)),
                ('username', models.CharField(default='', max_length=80)),
                ('context', models.CharField(default='default', null=True, max_length=80)),
                ('callingpres', models.CharField(default='allowed_not_screened', choices=[('Allowed not screened', 'allowed_not_screened'), ('Allowed passed screen', 'allowed_passed_screen'), ('Allowed failed screen', 'allowed_failed_screen'), ('Allowed', 'allowed'), ('Prohib not screened', 'prohib_not_screened'), ('Prohib passed screen', 'prohib_passed_screen'), ('Prohib failed screen', 'prohib_failed_screen'), ('Prohib', 'prohib'), ('Unavailable', 'unavailable')], max_length=32)),
                ('deny', models.CharField(default=None, null=True, max_length=95)),
                ('permit', models.CharField(default=None, null=True, max_length=95)),
                ('secret', models.CharField(default=None, null=True, max_length=80)),
                ('md5secret', models.CharField(default=None, null=True, max_length=80)),
                ('remotesecret', models.CharField(default=None, null=True, max_length=250)),
                ('transport', models.CharField(default='udp', null=True, choices=[('TCP', 'tcp'), ('UDP', 'udp'), ('TCP and UDP', 'tcp,udp')], max_length=7)),
                ('host', models.CharField(default='dynamic', max_length=31)),
                ('nat', models.CharField(default='no', choices=[('Enable NAT', 'yes'), ('Disable NAT', 'no'), ('Never use NAT', 'never'), ('Route', 'route')], max_length=5)),
                ('type', models.CharField(default='friend', choices=[('User', 'user'), ('Peer', 'peer'), ('Friend', 'friend')], max_length=6)),
                ('amaflags', models.CharField(default=None, null=True, max_length=40)),
                ('callgroup', models.CharField(default=None, null=True, max_length=40)),
                ('callerid', models.CharField(default=None, null=True, max_length=80)),
                ('defaultip', models.GenericIPAddressField(default=None, null=True)),
                ('dtmfmode', models.CharField(default='auto', null=True, choices=[('rfc2833', 'rfc2833'), ('Info', 'info'), ('Short info', 'shortinfo'), ('Inband', 'inband'), ('Auto', 'auto')], max_length=9)),
                ('fromuser', models.CharField(default=None, null=True, max_length=80)),
                ('fromdomain', models.CharField(default=None, null=True, max_length=80)),
                ('insecure', models.CharField(default=None, null=True, max_length=40)),
                ('language', models.CharField(default=None, null=True, choices=[('Russian', 'ru'), ('English', 'en')], max_length=4)),
                ('mailbox', models.CharField(default=None, null=True, max_length=50)),
                ('pickupgroup', models.CharField(default=None, null=True, max_length=40)),
                ('qualify', models.CharField(default=None, null=True, max_length=40)),
                ('regexten', models.CharField(default=None, null=True, max_length=80)),
                ('rtptimeout', models.IntegerField(default=None, null=True, max_length=11)),
                ('rtpholdtimeout', models.IntegerField(default=None, null=True, max_length=11)),
                ('setvar', models.CharField(default=None, null=True, max_length=100)),
                ('disallow', models.CharField(default='all', null=True, max_length=100)),
                ('allow', models.CharField(default='g729;ilbc;gsm;ulaw;alaw', null=True, max_length=100)),
                ('fullcontact', models.CharField(default='', max_length=80)),
                ('ipaddr', models.GenericIPAddressField(default='')),
                ('port', models.PositiveIntegerField(default=5060, validators=[django.core.validators.MaxValueValidator(65535)])),
                ('defaultuser', models.CharField(default='', max_length=80)),
                ('subscribecontext', models.CharField(default=None, null=True, max_length=80)),
                ('directmedia', models.CharField(default='no', null=True, choices=[('Enable directmedia', 'yes'), ('Disable directmedia', 'no'), ('No NAT', 'nonat'), ('Update', 'update')], max_length=6)),
                ('trustrpid', models.CharField(default=None, null=True, choices=[('Enable trustrpid', 'yes'), ('Disable trustrpid', 'no')], max_length=3)),
                ('sendrpid', models.CharField(default=None, null=True, choices=[('Enable sendrpid', 'yes'), ('Disable sendrpid', 'no')], max_length=3)),
                ('progressinband', models.CharField(default=None, null=True, choices=[('Enable progressinband', 'yes'), ('Disable progressinband', 'no'), ('Never use progressinband', 'never')], max_length=5)),
                ('promiscredir', models.CharField(default=None, null=True, choices=[('Enable promiscredir', 'yes'), ('Disable promiscredir', 'no')], max_length=3)),
                ('useclientcode', models.CharField(default=None, null=True, choices=[('Enable clientcode', 'yes'), ('Disable clientcode', 'no')], max_length=3)),
                ('accountcode', models.CharField(default=None, null=True, max_length=40)),
                ('regseconds', models.IntegerField(default=0, max_length=11)),
                ('regserver', models.CharField(default=None, null=True, max_length=100)),
                ('useragent', models.CharField(default=None, null=True, max_length=100)),
                ('lastms', models.IntegerField(default=None, null=True, max_length=11)),
                ('callcounter', models.CharField(default=None, null=True, choices=[('Enable callcounter', 'yes'), ('Disable callcounter', 'no')], max_length=3)),
                ('busylevel', models.IntegerField(default=None, null=True, max_length=11)),
                ('allowoverlap', models.CharField(default=None, null=True, choices=[('Enable allowoverlap', 'yes'), ('Disable allowoverlap', 'no')], max_length=3)),
                ('allowsubscribe', models.CharField(default=None, null=True, choices=[('Enable allowsubscribe', 'yes'), ('Disable allowsubscribe', 'no')], max_length=3)),
                ('videosupport', models.CharField(default=None, null=True, choices=[('Enable videosupport', 'yes'), ('Disable videosupport', 'no')], max_length=3)),
                ('maxcallbitrate', models.PositiveIntegerField(default=None, null=True, max_length=11)),
                ('rfc2833compensate', models.CharField(default=None, null=True, choices=[('Enable rfc2833compensate', 'yes'), ('Disable rfc2833compensate', 'no')], max_length=3)),
                ('session_timers', models.CharField(default=None, max_length=9, null=True, choices=[('Accept', 'accept'), ('Refuse', 'refuse'), ('Originate', 'originate')], db_column='session-timers')),
                ('session_expires', models.IntegerField(default=None, max_length=11, null=True, db_column='session-expires')),
                ('session_minse', models.IntegerField(default=None, max_length=11, null=True, db_column='session-minse')),
                ('session_refresher', models.CharField(default=None, max_length=3, null=True, choices=[('UAC', 'uac'), ('UAS', 'uas')], db_column='session-refresher')),
                ('t38pt_usertpsource', models.CharField(default=None, null=True, max_length=40)),
                ('outboundproxy', models.CharField(default=None, null=True, max_length=40)),
                ('callbackextension', models.CharField(default=None, null=True, max_length=40)),
                ('registertrying', models.CharField(default=None, null=True, choices=[('Enable registertrying', 'yes'), ('Disable registertrying', 'no')], max_length=3)),
                ('timert1', models.IntegerField(default=None, null=True, max_length=11)),
                ('timerb', models.IntegerField(default=None, null=True, max_length=11)),
                ('qualifyfreq', models.IntegerField(default=None, null=True, max_length=11)),
                ('constantssrc', models.CharField(default=None, null=True, choices=[('Enable constantssrc', 'yes'), ('Disable constantssrc', 'no')], max_length=3)),
                ('contactpermit', models.CharField(default=None, null=True, max_length=40)),
                ('contactdeny', models.CharField(default=None, null=True, max_length=40)),
                ('usereqphone', models.CharField(default=None, null=True, choices=[('Enable usereqphone', 'yes'), ('Disable usereqphone', 'no')], max_length=3)),
                ('textsupport', models.CharField(default=None, null=True, choices=[('Enable textsupport', 'yes'), ('Disable textsupport', 'no')], max_length=3)),
                ('faxdetect', models.CharField(default=None, null=True, choices=[('Enable faxdetect', 'yes'), ('Disable faxdetect', 'no')], max_length=3)),
                ('buggymwi', models.CharField(default=None, null=True, choices=[('Enable buggymwi', 'yes'), ('Disable buggymwi', 'no')], max_length=3)),
                ('auth', models.CharField(default='md5', max_length=100)),
                ('fullname', models.CharField(default='', max_length=150)),
                ('trunkname', models.CharField(default=None, null=True, max_length=40)),
                ('cid_number', models.CharField(default=None, null=True, max_length=40)),
                ('mohinterpret', models.CharField(default=None, null=True, max_length=40)),
                ('mohsuggest', models.CharField(default=None, null=True, max_length=40)),
                ('parkinglot', models.CharField(default=None, null=True, max_length=40)),
                ('hasvoicemail', models.CharField(default=None, null=True, choices=[('Enable hasvoicemail', 'yes'), ('Disable hasvoicemail', 'no')], max_length=3)),
                ('subscribemwi', models.CharField(default=None, null=True, choices=[('Enable subscribemwi', 'yes'), ('Disable subscribemwi', 'no')], max_length=3)),
                ('vmexten', models.CharField(default=None, null=True, max_length=40)),
                ('autoframing', models.CharField(default=None, null=True, choices=[('Enable autoframing', 'yes'), ('Disable autoframing', 'no')], max_length=3)),
                ('rtpkeepalive', models.PositiveIntegerField(default=None, null=True, max_length=11)),
                ('call_limit', models.PositiveIntegerField(default=None, max_length=11, null=True, db_column='call-limit')),
                ('g726nonstandard', models.CharField(default=None, null=True, choices=[('Enable g726nonstandard', 'yes'), ('Disable g726nonstandard', 'no')], max_length=3)),
                ('ignoresdpversion', models.CharField(default=None, null=True, choices=[('Enable ignoresdpversion', 'yes'), ('Disable ignoresdpversion', 'no')], max_length=3)),
                ('allowtransfer', models.CharField(default=None, null=True, choices=[('Enable allowtransfer', 'yes'), ('Disable allowtransfer', 'no')], max_length=3)),
                ('dynamic', models.CharField(default=None, null=True, choices=[('Enable dynamic', 'yes'), ('Disable dynamic', 'no')], max_length=3)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model, apps.peer.models.PeerParamsMixin),
        ),
        migrations.AlterIndexTogether(
            name='subscriber',
            index_together=set([('ipaddr', 'port'), ('host', 'port')]),
        ),
    ]