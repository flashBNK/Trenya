from django.shortcuts import render, get_object_or_404
from .models import Workout, Exercise, Goal

def index(request):
    context = {'title': 'Главная',}
    return render(request, 'main/index.html', context)



def workout_list(request, goal_slug=None):
    workouts = Workout.objects.all()
    goals = Goal.objects.all()

    goal = None
    if goal_slug:
        goal = get_object_or_404(Goal, slug=goal_slug)
        workouts = workouts.filter(goal=goal)

    context = {'title': 'Trenya',
               'workouts': workouts,
               'goals': goals,
               'goal': goal,}

    return render(request, 'main/workout/workout_list.html', context)

def workout_detail(request, id, slug):
    workout = get_object_or_404(Workout, id=id, slug=slug)
    related_workout = Workout.objects.filter(goal=workout.goal).exclude(id=workout.id)[:4]

    return render(request, 'main/workout/workout_detail.html', {'workout': workout,
                                                                'related_workouts': related_workout})
