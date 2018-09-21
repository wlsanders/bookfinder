# Generated by Django 2.1.1 on 2018-09-19 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20180919_0138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='tag',
        ),
        migrations.AddField(
            model_name='books',
            name='tag',
            field=models.ManyToManyField(to='books.Tags'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='tags',
            field=models.CharField(max_length=140),
        ),
    ]