from datetime import timedelta
from unittest import skip

from django.test import TestCase
from django.urls import reverse
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

    @skip("We'd need freezegun for this test.")
    def test_1_day_old_question_should_be_flagged_as_published_recently(self):
        """
        `was_published_recently()` should return `True` for questions whose
        `pub_date` is older than exactly 1 day.
        """

        # TODO: We need to use freezegun. When this runs, e.g.
        # test's now: Jan 2, 1am; test's pubdate: Jan 1, 1am
        # actual code's now: Jan 2, 1:01am (just an example, it'd be
        # ms difference); actual code's past day limit: Jan 1, 1:01am
        # given q: Jan 1, 1am; limit: Jan 1, 1:01am. Since given q is now OLDER
        # by the time actual function runs, it returns FALSE, thus failing
        # this test.
        given_older_pub_date = timezone.now() - timedelta(days=1)
        given_older_question = Question(pub_date=given_older_pub_date)

        actual_flag = given_older_question.was_published_recently()
        expected_flag = True
        self.assertIs(actual_flag, expected_flag)


    def test_older_question_should_not_be_flagged_as_published_recently(self):
        """
        `was_published_recently()` should return `False` for questions whose
        `pub_date` is older than 1 day.
        """
        given_older_pub_date = timezone.now() - timedelta(days=1, seconds=1)
        given_older_question = Question(pub_date=given_older_pub_date)

        actual_flag = given_older_question.was_published_recently()
        expected_flag = False
        self.assertIs(actual_flag, expected_flag)


class Question_Index_View_Tests(TestCase):


    def test_no_questions_should_display_appropriate_message(self):
        """If no questions exist, an appropriate message should be displayed."""
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_questions'], [])
