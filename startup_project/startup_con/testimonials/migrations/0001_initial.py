# Generated by Django 4.1.2 on 2022-10-31 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='testimonial/%Y/%m/%d/')),
                ('description', models.TextField()),
                ('avaiable', models.BooleanField(default=True)),
            ],
        ),
    ]
