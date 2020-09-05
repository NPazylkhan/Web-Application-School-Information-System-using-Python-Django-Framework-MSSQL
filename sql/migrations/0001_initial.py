# Generated by Django 2.1.13 on 2019-11-24 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.IntegerField(auto_created=True, db_column='Id', primary_key=True, serialize=False)),
                ('firstname', models.CharField(db_column='FirstName', max_length=50)),
                ('lastname', models.CharField(db_column='LastName', max_length=50)),
                ('year', models.IntegerField(db_column='Year')),
            ],
            options={
                'db_table': 'Person',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='sql.Person')),
                ('image', models.ImageField(upload_to='images/')),
            ],
            options={
                'db_table': 'Image',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('positionid', models.ForeignKey(db_column='positionId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='sql.Person')),
                ('position', models.CharField(blank=True, max_length=20, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=15, null=True)),
                ('telephone', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'position',
            },
        ),
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('department', models.ForeignKey(db_column='department', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='sql.Person')),
                ('corp', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'workers',
            },
        ),
        migrations.CreateModel(
            name='Depart',
            fields=[
                ('id', models.ForeignKey(db_column='Id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='sql.Position')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('aim', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'depart',
            },
        ),
        migrations.AddField(
            model_name='workers',
            name='id',
            field=models.ForeignKey(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, to='sql.Depart'),
        ),
    ]
