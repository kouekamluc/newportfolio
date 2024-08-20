
from django.db import models

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Skill Categories"

class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    description = models.TextField(blank=True)
    proficiency = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1-5 scale
    icon = models.CharField(max_length=50, blank=True, help_text="Font Awesome class name")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-proficiency', 'name']