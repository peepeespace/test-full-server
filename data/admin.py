from django.contrib import admin

from data.models import ControlState, ToolState

admin.site.register([ControlState, ToolState])