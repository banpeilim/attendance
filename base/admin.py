from django.contrib import admin
from .models import Flight
from .models import Review
from .models import Attendance
from .models import Queue

# Register your models here.

admin.site.register(Flight)
admin.site.register(Review)
admin.site.register(Attendance)
admin.site.register(Queue)