from django.test import TestCase

from widgets.models import Widget


class ReprTest(TestCase):

    def test_hides_defaults(self):
        w = Widget()
        self.assertEqual("Widget()", repr(w))
        self.assertEqual('green', w.color)

        w = Widget(color='yellow')
        self.assertEqual("Widget(color='yellow')", repr(w))
