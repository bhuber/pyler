from unittest import TestCase

from stripe_interview.store_closing_problem import compute_penalty, \
    find_best_closing_time, find_best_closing_time2


class Test(TestCase):
    def test_compute_penalty(self):
        self.assertEqual(3, compute_penalty("Y Y N Y", 0))
        self.assertEqual(2, compute_penalty("N Y N Y", 2))
        self.assertEqual(1, compute_penalty("Y Y N Y", 4))


class Test(TestCase):
    def test_find_best_closing_time(self):
        self.assertEqual(2, find_best_closing_time("Y Y N N"))
        self.assertEqual(2, find_best_closing_time2("Y Y N N"))
        self.assertEqual(0, find_best_closing_time("N N Y Y"))
        self.assertEqual(0, find_best_closing_time2("N N Y Y"))
        self.assertEqual(0, find_best_closing_time("N Y N Y"))
        self.assertEqual(0, find_best_closing_time2("N Y N Y"))
        self.assertEqual(2, find_best_closing_time("Y Y N Y"))
        self.assertEqual(2, find_best_closing_time2("Y Y N Y"))
        self.assertEqual(4, find_best_closing_time("Y Y Y Y"))
        self.assertEqual(4, find_best_closing_time2("Y Y Y Y"))
        self.assertEqual(0, find_best_closing_time(""))
        self.assertEqual(0, find_best_closing_time2(""))
