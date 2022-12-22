# Generated by Django 4.1.3 on 2022-12-21 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suggestions', '0020_remove_questionarymodel_diet_meal_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionarymodel',
            name='diet_meal_quantity',
            field=models.CharField(choices=[('ALWAYS', 'always on diet'), ('ONE', '1 time'), ('TWO', '2 times'), ('THREE', '3 times'), ('FOUR', '4 times'), ('NEVER', 'has no diet')], default=None, max_length=32),
        ),
        migrations.AddField(
            model_name='questionarymodel',
            name='on_a_diet',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], default=None, max_length=3),
        ),
        migrations.AddField(
            model_name='questionarymodel',
            name='phisical_exercises',
            field=models.CharField(choices=[('YES_MORE_2H', 'Yes, and more then 2 hours per week'), ('YES_LESS_2H', 'Yes, but less then 2 hours per week'), ('NO', 'No, I do not do any phisical exercises')], default=None, max_length=32),
        ),
        migrations.AddField(
            model_name='questionarymodel',
            name='physical_activity',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], default=None, max_length=3),
        ),
    ]
