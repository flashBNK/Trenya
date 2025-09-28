from django.db import models
from django.urls import reverse


class Goal(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Цель'
        verbose_name_plural = 'Цели'

    def get_absolute_url(self):
        return reverse("main:workout_list_by_goal", args=[self.slug])


class Exercise(models.Model):
    EXERCISE_TYPE_CHOICES = [
        ('reps', 'Повторения'),
        ('time', 'Время'),
    ]

    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    technique = models.TextField(blank=True)  # описание техники
    muscle_group = models.CharField(max_length=50, db_index=True)  # группа мышц
    image = models.ImageField(upload_to='workouts/%Y/%m/%d', blank=True)

    sets = models.IntegerField()  # количество подходов
    exercise_type = models.CharField(max_length=10, choices=EXERCISE_TYPE_CHOICES, default='reps')
    reps = models.IntegerField(blank=True, null=True)  # повторения
    duration = models.IntegerField(blank=True, null=True, help_text="В секундах")  # время

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнения'


class Workout(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=100)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='workouts')
    exercise = models.ManyToManyField(Exercise, related_name='workouts')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    duration = models.IntegerField(default=30)
    difficulty = models.CharField(
        max_length=50,
        choices=[('easy', 'Легкая'), ('medium', 'Средняя'), ('hard', 'Тяжелая')],
        default='easy'
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Тренировка'
        verbose_name_plural = 'Тренировки'

    def get_absolute_url(self):
        return reverse("main:workout_detail", args=[self.id, self.slug])