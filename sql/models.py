# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each OneToOneField has `on_delete` set to the desired behavior.
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Person(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True, auto_created=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.

    class Meta:
        
        db_table = 'Person'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        
        db_table = 'auth_group'


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    codename = models.CharField(max_length=100)

    class Meta:
        
        db_table = 'auth_permission'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        
        db_table = 'auth_user'


class Depart(models.Model):
    id = models.ForeignKey('Position', models.DO_NOTHING, db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=20, blank=True, null=True)
    aim = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        
        db_table = 'depart'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()

    class Meta:
        
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        
        db_table = 'django_migrations'


class Position(models.Model):
    positionid = models.OneToOneField(Person, models.DO_NOTHING, db_column='positionId', primary_key=True)  # Field name made lowercase.
    position = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=15, blank=True, null=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        
        db_table = 'position'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class Workers(models.Model):
    id = models.ForeignKey(Depart, models.DO_NOTHING, db_column='id')
    department = models.ForeignKey(Person, models.DO_NOTHING, db_column='department', primary_key=True)
    corp = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        
        db_table = 'workers'


class Image(models.Model):
    id = models.OneToOneField(Person, models.DO_NOTHING, db_column='id', primary_key=True)  # Field name made lowercase.
    image = models.ImageField(upload_to='images/')

    class Meta:
        db_table = 'Image'