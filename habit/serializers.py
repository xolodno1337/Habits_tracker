from rest_framework.serializers import ModelSerializer
from habit.models import Habit
from habit.validators import ChoiceRewardValidator, TimeValidator, RelatedHabitValidator, PeriodicityValidator, \
    NoConnectionValidator


class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            ChoiceRewardValidator('related_habit', 'reward'),
            TimeValidator('time_to_complete'),
            RelatedHabitValidator('pleasant_habit', 'related_habit'),
            PeriodicityValidator('periodicity'),
            NoConnectionValidator('pleasant_habit', 'related_habit', 'reward')
        ]
