# Generated by Django 2.2.4 on 2020-02-13 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0002_auto_20200212_0805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerinquiry',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='inquirydetail',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='knowledgebase',
            name='updated_at',
        ),
    ]
