from django.db import models


class ObservationItem(models.Model):
    id_obs = models.AutoField(primary_key=True)
    observation = models.TextField()
    created_date = models.DateField()


class SuggestedLink(models.Model):
    id_link = models.AutoField(primary_key=True)
    link = models.TextField()
    org_name = models.CharField(max_length=50);
