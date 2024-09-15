from django.contrib import admin
from habit.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('place', 'action', 'time')
