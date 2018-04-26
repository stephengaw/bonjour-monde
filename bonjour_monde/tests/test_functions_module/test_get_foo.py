from unittest import TestCase

import bonjour_monde


class TestGet_foo(TestCase):
    def test_get_foo(self):

        self.assertEqual(bonjour_monde.functions_module.get_foo(), 'foo')
