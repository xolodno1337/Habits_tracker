from rest_framework.routers import SimpleRouter
from habit.views import HabitViewSet
from habit.apps import HabitConfig

app_name = HabitConfig.name

router = SimpleRouter()
router.register("", HabitViewSet)

urlpatterns = []

urlpatterns += router.urls
