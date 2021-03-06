# Generated by Django 2.0 on 2020-01-10 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Queries', '0002_auto_20200110_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=255, verbose_name='email address')),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Contact Us',
            },
        ),
        migrations.AlterField(
            model_name='careerquery',
            name='address',
            field=models.TextField(blank=True),
        ),
    ]
