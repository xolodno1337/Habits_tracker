from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from habit.models import Habit
from habit.paginations import CustomPagination
from habit.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()

    def get_permissions(self):
        if self.action in ['create', 'list', 'retrieve']:
            self.permission_classes = (IsAuthenticated,)
        elif self.action in ['update', 'destroy']:
            self.permission_classes = (IsOwner, IsAuthenticated)
        return super().get_permissions()

    def get_queryset(self):
        """ Возвращает список привычек для текущего пользователя и все опубликованные привычки. """

        user = self.request.user
        user_habits = Habit.objects.filter(user=user)
        published_habits = Habit.objects.filter(is_published=True)
        return user_habits | published_habits
