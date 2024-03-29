# Generated by Django 4.2.5 on 2024-03-25 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('color_code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(null=True, upload_to='house_imgs')),
                ('spec', models.TextField()),
                ('price', models.PositiveBigIntegerField()),
                ('detail', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.color')),
            ],
        ),
    ]
