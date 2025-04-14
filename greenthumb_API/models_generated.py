# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Events(models.Model):
    event_id = models.IntegerField(db_column='eventID', primary_key=True)  # Field name made lowercase.
    userplant_id = models.ForeignKey('Userplants', models.DO_NOTHING, db_column='userPlantID')  # Field name made lowercase.
    recurrence_id = models.ForeignKey('Recurrence', models.DO_NOTHING, db_column='recurrenceID')  # Field name made lowercase.
    init_date = models.DateField(db_column='initDate')  # Field name made lowercase.
    care_type = models.CharField(db_column='careType', max_length=50)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    interval = models.IntegerField()
    complete = models.IntegerField()
    overdue = models.IntegerField()
    
    def __str__(self):
        return f"{self.care_type} for {self.userplant_id} on {self.init_date}"

    class Meta:
        managed = False
        db_table = 'Events'


class Recurrence(models.Model):
    recurrence_id = models.IntegerField(db_column='recurrenceID', primary_key=True)  # Field name made lowercase.
    recurrence_type = models.IntegerField(db_column='recurrenceType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Recurrence'


class Schedule(models.Model):
    schedule_id = models.IntegerField(db_column='scheduleID', primary_key=True)  # Field name made lowercase.
    event_id = models.ForeignKey(Events, models.DO_NOTHING, db_column='eventID')  # Field name made lowercase.
    scheduled_date = models.DateField(db_column='scheduledDate')  # Field name made lowercase.
    scheduled_time = models.TimeField(db_column='scheduledTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Schedule'


class User(models.Model):
    user_id = models.IntegerField(db_column='userID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=100)
    phone_number = models.CharField(unique=True, max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User'


class Userplants(models.Model):
    userplant_id = models.IntegerField(db_column='userPlantID', primary_key=True)  # Field name made lowercase.
    user_id = models.ForeignKey(User, models.DO_NOTHING, db_column='userID')  # Field name made lowercase.
    plant_id = models.ForeignKey('Baseplant', models.DO_NOTHING, db_column='plantID')  # Field name made lowercase.
    nickname = models.CharField(unique=True, max_length=50, blank=True, null=True)
    root_date = models.DateField(db_column='rootDate')  # Field name made lowercase.
    use_default_img = models.IntegerField(db_column='useDefaultImg')  # Field name made lowercase.
    current_ph = models.FloatField(db_column='currentPH', blank=True, null=True)  # Field name made lowercase.
    current_moisture = models.FloatField(db_column='currentMoisture', blank=True, null=True)  # Field name made lowercase.
    current_lux = models.FloatField(db_column='currentLUX', blank=True, null=True)  # Field name made lowercase.
    current_temp = models.FloatField(db_column='currentTemp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserPlants'


class Baseplant(models.Model):
    plant_id = models.IntegerField(db_column='plantID', primary_key=True)  # Field name made lowercase.
    common_name = models.CharField(unique=True, max_length=50)
    binomial_name = models.CharField(max_length=50, blank=True, null=True)
    light_description = models.CharField(max_length=150, blank=True, null=True)
    light_lvl = models.IntegerField(blank=True, null=True)
    water_req = models.CharField(max_length=160, blank=True, null=True)
    water_schedule = models.CharField(max_length=15)
    soil_and_drainage = models.CharField(max_length=150, blank=True, null=True)
    ideal_ph = models.FloatField(blank=True, null=True)
    temperament = models.CharField(max_length=200, blank=True, null=True)
    growth_height = models.CharField(max_length=50, blank=True, null=True)
    propagation = models.CharField(max_length=150, blank=True, null=True)
    toxicity = models.CharField(max_length=15, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    common_problems = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'baseplant'


class Defaultimgs(models.Model):
    default_id = models.IntegerField(db_column='defaultID', primary_key=True)  # Field name made lowercase.
    plant_id = models.ForeignKey(Baseplant, models.DO_NOTHING, db_column='plantID')  # Field name made lowercase.
    bucket_url = models.CharField(db_column='bucketURL', unique=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'defaultImgs'


class Userimgs(models.Model):
    img_id = models.IntegerField(db_column='imgID', primary_key=True)  # Field name made lowercase.
    userplant_id = models.ForeignKey(Userplants, models.DO_NOTHING, db_column='userPlantID')  # Field name made lowercase.
    bucket_url = models.CharField(db_column='bucketURL', unique=True, max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userImgs'
