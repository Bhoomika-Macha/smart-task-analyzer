from django.test import TestCase
from datetime import date, timedelta
from .scoring import calculate_task_score

class TaskScoringTests(TestCase):

    def test_overdue(self):
        task = {
            "title": "A",
            "due_date": (date.today() - timedelta(days=1)).isoformat(),
            "importance": 5,
            "estimated_hours": 2,
            "dependencies": []
        }
        score = calculate_task_score(task)
        self.assertTrue(score >= 100)

    def test_quick(self):
        task = {
            "title": "B",
            "due_date": (date.today() + timedelta(days=2)).isoformat(),
            "importance": 5,
            "estimated_hours": 1,
            "dependencies": []
        }
        self.assertTrue(calculate_task_score(task) > 75)

    def test_dependencies(self):
        t1 = {
            "title": "A",
            "due_date": (date.today() + timedelta(days=5)).isoformat(),
            "importance": 5,
            "estimated_hours": 3,
            "dependencies": []
        }
        t2 = {
            "title": "B",
            "due_date": (date.today() + timedelta(days=5)).isoformat(),
            "importance": 5,
            "estimated_hours": 3,
            "dependencies": [1,2,3]
        }
        self.assertTrue(calculate_task_score(t2) < calculate_task_score(t1))
