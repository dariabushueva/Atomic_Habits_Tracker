from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('action', 'start', 'frequency', 'next_reminder_date', 'time_to_complete', 'place', 'user',
                    'related_habit', 'reward', 'is_public', 'is_pleasant')
    list_display_links = ('action', 'place', 'user')
