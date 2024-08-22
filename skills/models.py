
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)  # Add this line


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order', 'name']

        verbose_name_plural = "Skill Categories"

class Skill(models.Model):
    PROFICIENCY_BEGINNER = 1
    PROFICIENCY_INTERMEDIATE = 2
    PROFICIENCY_ADVANCED = 3
    PROFICIENCY_EXPERT = 4
    PROFICIENCY_MASTER = 5

    PROFICIENCY_CHOICES = [
        (PROFICIENCY_BEGINNER, 'Beginner'),
        (PROFICIENCY_INTERMEDIATE, 'Intermediate'),
        (PROFICIENCY_ADVANCED, 'Advanced'),
        (PROFICIENCY_EXPERT, 'Expert'),
        (PROFICIENCY_MASTER, 'Master'),
    ]

    name = models.CharField(max_length=100)
    category = models.ForeignKey(SkillCategory, related_name='skills', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    proficiency = models.IntegerField(
        choices=PROFICIENCY_CHOICES,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    years_of_experience = models.PositiveIntegerField(default=0)
    icon = models.CharField(max_length=50, blank=True, help_text="Font Awesome class name")

    class Meta:
        ordering = ['-proficiency', 'name']

    def __str__(self):
        return self.name
