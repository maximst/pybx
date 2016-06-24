# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 13:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pbx', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ivr',
            name='end_content_type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='end_content_type', to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='ivr',
            name='end_object_id',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='ivr',
            name='key0_content_type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='key0_content_type', to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='ivr',
            name='key1_content_type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='key1_content_type', to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='ivr',
            name='key1_object_id',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='ivr',
            name='key2_content_type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='key2_content_type', to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='ivr',
            name='key2_object_id',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='ivr',
            name='key3_content_type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='key3_content_type', to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='ivr',
            name='key3_object_id',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='ivr',
            name='key4_content_type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='key4_content_type', to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='ivr',
            name='key4_object_id',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='ivr',
            name='key5_content_type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='key5_content_type', to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='ivr',
            name='key5_object_id',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='ivr',
            name='key6_content_type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='key6_content_type', to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='ivr',
            name='key6_object_id',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='ivr',
            name='key7_content_type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='key7_content_type', to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='ivr',
            name='key7_object_id',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='ivr',
            name='key8_content_type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='key8_content_type', to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='ivr',
            name='key8_object_id',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='ivr',
            name='key9_content_type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='key9_content_type', to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='ivr',
            name='key9_object_id',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='queue',
            name='content_type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='queue',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
    ]