# Generated by Django 2.1.4 on 2019-04-12 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_auto_20190412_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project')),
            ],
        ),
        migrations.RemoveField(
            model_name='issue',
            name='label',
        ),
        migrations.AddField(
            model_name='issue',
            name='label',
            field=models.ManyToManyField(to='project.Label'),
        ),
    ]
