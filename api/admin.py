from django.contrib import admin
# Import your Task model
from .models import Task

# Register it so it appears in the admin dashboard
admin.site.register(Task)
