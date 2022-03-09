from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from .models import Question

class Question_Was_Published_Recently_Tests(TestCase):
    def test_future_question_should_not_be_flagged_as_published_recently(self):
        """
        `was_published_recently()` should return `False` for questions whose
        `pub_date` is in the future.
        """
        given_future_pub_date = timezone.now() + timedelta(days=30)
        given_future_question = Question(pub_date=given_future_pub_date)

        actual_flag = given_future_question.was_published_recently()
        expected_flag = False
        self.assertIs(actual_flag, expected_flag)
