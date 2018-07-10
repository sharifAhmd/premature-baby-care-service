from django.contrib import admin                                #Default django model for admin
from problemandsolution.models import problemandsolution        #Imported newly made django model



#For viewing the models in the admin panel , all the models have to be register here.
admin.site.register(problemandsolution)
