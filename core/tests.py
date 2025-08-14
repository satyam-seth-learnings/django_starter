from django.test import TestCase
from .models import Student
from datetime import date

# Create your tests here.

class StudentModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name="John",
            last_name="Doe",
        )

    def test_student_creation(self):
        """Test that a student instance is created correctly."""

        self.assertEqual(self.student.first_name, "John")
        self.assertEqual(self.student.last_name, "Doe")
        
    def test_str_method(self):
        """Test the __str__ method of the Student model."""
        
        self.assertEqual(str(self.student), "John Doe")