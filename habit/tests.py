from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from habit.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@mail.com")
        self.habit = Habit.objects.create(user=self.user, place="Дом", action="Зарядка")
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        url = reverse("habit:habit-detail", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place"), self.habit.place)
        self.assertEqual(data.get("action"), "Зарядка")

    def test_habit_create(self):
        url = reverse("habit:habit-list")
        data = {
            "user": self.user.pk,
            "place": "Где угодно",
            "action": "Пить 2л. воды",
            "periodicity": 1,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_update(self):
        url = reverse("habit:habit-detail", args=(self.habit.pk,))
        data = {
            "user": self.user.pk,
            "place": "Где угодно",
            "action": "Пить 2л. воды",
            "periodicity": 1,
        }
        response = self.client.patch(url, data=data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place"), "Где угодно")
        self.assertEqual(data.get("action"), "Пить 2л. воды")

    def test_habit_delete(self):
        url = reverse("habit:habit-detail", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_list(self):
        url = reverse("habit:habit-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
