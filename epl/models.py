from django.db import models

# Create your models here.


class Team(models.Model):
    team_name = models.CharField(default='', max_length=100)
    team_name_kr = models.CharField(default='', max_length=100)
    nation = models.CharField(default='', max_length=10)
    stadium = models.CharField(default='', max_length=100)
    stadium_kr = models.CharField(default='', max_length=100)

    def __str__(self):
        # return "{},{},{},{},{},{}".format(self.team_id, self.team_name, self.team_name_kr, self.nation, self.stadium, self.stadium_kr)
        return self.team_name_kr
    def __unicode__(self):
        return self.team_name_kr
