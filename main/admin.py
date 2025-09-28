from django.contrib import admin
from .models import Workout, Goal, Exercise

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['name', 'goal', 'created', 'updated']
    list_filter = ['created', 'updated', 'goal']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['name', 'muscle_group']
#    list_filter = ['available', 'created', 'updated', 'category']
#    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
