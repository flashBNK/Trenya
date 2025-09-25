from django.db import models


class Goal(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Цель'
        verbose_name_plural = 'Цели'


class Exercise(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=100)
    technique = models.TextField(blank=True)
    muscle_group = models.CharField(max_length=50, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    sets = models.IntegerField()
    reps = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнения'


class Workout(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=100)
    plan = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='workouts')
    exercise = models.ManyToManyField(Exercise, related_name='workouts')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Тренировка'
        verbose_name_plural = 'Тренировки'