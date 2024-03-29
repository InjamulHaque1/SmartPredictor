# Generated by Django 4.2.5 on 2024-03-27 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_color_house'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('color_code', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='house',
            name='color',
        ),
        migrations.AddField(
            model_name='house',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='area',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Color',
        ),
        migrations.AddField(
            model_name='house',
            name='productCategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.category'),
        ),
    ]
