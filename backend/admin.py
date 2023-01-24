from django.contrib import admin

# Register your models here.

from .models import EventHappened
from .models import UpcommingEvents
from .models import Team

admin.site.register(EventHappened)
admin.site.register(UpcommingEvents)
admin.site.register(Team)

