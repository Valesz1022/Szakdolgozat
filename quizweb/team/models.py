# team/models.py
from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher_teams')
    team_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.team_name} (Teacher: {self.teacher.username})"


class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team_memberships')

    def __str__(self):
        return f"{self.student.username} in {self.team.team_name}"
