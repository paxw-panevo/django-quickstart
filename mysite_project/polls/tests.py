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

# TODO Try moving this helper function inside the test class?
def _create_question(question_text, *, pub_date_offset):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + timedelta(days=pub_date_offset)
    return Question.objects.create(question_text=question_text, pub_date=time)

class Question_Index_View_Tests(TestCase):


    def test_no_questions_should_display_appropriate_message(self):
        """If no questions exist, an appropriate message should be displayed."""
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_questions'], [])

    def test_past_question_should_be_listed_in_index(self):
        """
        Questions with a `pub_date` in the past are displayed on the
        index page.
        """
        question = _create_question("What's up?", pub_date_offset=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_questions'],
            [question],
        )

    def test_future_question_should_not_be_listed_in_index(self):
        """
        Questions with a `pub_date` in the past are displayed on the
        index page.
        """
        question = _create_question("What's up?", pub_date_offset=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_questions'],
            [],
        )
