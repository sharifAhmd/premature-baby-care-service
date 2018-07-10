from django.db import models

class problemandsolution(models.Model):
    problemname = models.CharField(max_length=150, default='')
    problemdetails = models.CharField(max_length=500, default='')
    problemsignandsymptom = models.CharField(max_length=500, default='')
    solution = models.CharField(max_length=500, default='')
    youtubeurl  = models.URLField(blank=True)


    # For naming the objects to its own name.
    def __str__(self):
        return  self.problemname
