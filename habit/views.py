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
        if self.action == 'create':
            self.permission_classes = (IsAuthenticated,)
        elif self.action == 'list':
            self.permission_classes = (IsAuthenticated,)
        elif self.action == 'update':
            self.permission_classes = (IsOwner, IsAuthenticated)
        elif self.action == 'retrieve':
            self.permission_classes = (IsAuthenticated,)
        elif self.action == 'destroy':
            self.permission_classes = (IsOwner, IsAuthenticated)

        return super().get_permissions()
