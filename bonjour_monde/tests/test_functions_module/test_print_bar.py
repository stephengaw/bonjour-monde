from unittest import TestCase
from unittest.mock import patch
import io

import bonjour_monde


class TestPrint_bar(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_bar(self, mock_stdout):

        bonjour_monde.functions_module.print_bar()

        self.assertEqual(mock_stdout.getvalue(), 'bar\n')
