# Generated by Django 3.1.6 on 2021-08-21 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usrname', models.TextField(default='', max_length=50)),
                ('pasword', models.TextField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Barangay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tname', models.TextField(default='', max_length=50)),
                ('birthday', models.CharField(default='', max_length=10)),
                ('gender', models.TextField(default='', max_length=10)),
                ('address', models.CharField(default='', max_length=50)),
                ('cnumber', models.CharField(default=None, max_length=11)),
                ('email', models.CharField(default='', max_length=50)),
                ('usr', models.TextField(default='', max_length=50)),
                ('pas', models.TextField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Requirements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pname', models.TextField(default='', max_length=50)),
                ('swabresult', models.CharField(choices=[('Negative', 'negative'), ('Positive', 'positive')], default=None, max_length=50)),
                ('swabcertificate', models.FileField(null=True, upload_to='documents/')),
                ('RidtCard', models.CharField(max_length=100, null=True)),
                ('identificationCards', models.FileField(null=True, upload_to='documents/')),
                ('Rtranspo', models.CharField(max_length=100, null=True)),
                ('transportation', models.CharField(choices=[('Public', 'public'), ('Private', 'private')], default=None, max_length=50)),
                ('barangay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PList.barangay')),
            ],
        ),
    ]
