from django.db import models

# Create your models here.
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
