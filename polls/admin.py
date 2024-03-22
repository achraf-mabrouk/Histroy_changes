from django.contrib import admin
from .models import Poll
from simple_history.admin import SimpleHistoryAdmin


# Register your models here.
admin.site.register(Poll, SimpleHistoryAdmin)
