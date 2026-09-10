# CI webhook test

from django.test import TestCase
from .models import Employee


class EmployeeModelTest(TestCase):

    def test_employee_creation(self):
        employee = Employee.objects.create(
            name="Hrushikesh",
            email="hrushikesh@test.com",
            position="Backend Developer",
            date_hired="2026-09-09"
        )

        self.assertEqual(employee.name, "Hrushikesh")
        self.assertEqual(employee.email, "hrushikesh@test.com")
        self.assertEqual(employee.position, "Backend Developer")