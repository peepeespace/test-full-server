from django.urls import path

from data.views import ControlStateList, ToolStateList

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('controlstate/', ControlStateList.as_view()),
    path('toolstate/', ToolStateList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)