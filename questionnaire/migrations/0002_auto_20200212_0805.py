# Generated by Django 2.2.4 on 2020-02-12 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='knowledgebase',
            old_name='parrent_question',
            new_name='parent_question',
        ),
        migrations.AddField(
            model_name='subcategorymaster',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='questionnaire.CategoryMaster'),
        ),
    ]
