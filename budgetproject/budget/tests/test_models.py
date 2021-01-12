from django.test import TestCase
from budget.models import Project,Category,Expense


class TestModels(TestCase):

    def setUp(self):
        self.project1 = Project.objects.create(
            # name=
        )

