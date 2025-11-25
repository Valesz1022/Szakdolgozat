from django import forms
from .models import Message
from team.models import Team
from django.contrib.auth import get_user_model

User = get_user_model()

class SendMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['team', 'recipient', 'content']

    def __init__(self, *args, teacher=None, **kwargs):
        super().__init__(*args, **kwargs)

        # Ha tanár, listázzuk a saját csapatait
        if teacher and teacher.is_staff:
            teams_qs = Team.objects.filter(teacher=teacher)
            self.fields['team'].queryset = teams_qs if teams_qs.exists() else Team.objects.none()
            # Ha van csapata, a recipient csak a csapattagok lehetnek
            if teams_qs.exists():
                students_qs = User.objects.filter(team_memberships__team__in=teams_qs).distinct()
                self.fields['recipient'].queryset = students_qs if students_qs.exists() else User.objects.none()
            else:
                self.fields['recipient'].queryset = User.objects.none()
        else:
            # Diákoknak üres queryset a formban (nem használják)
            self.fields['team'].queryset = Team.objects.none()
            self.fields['recipient'].queryset = User.objects.none()
