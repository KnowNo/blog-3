import unittest
from mock import * # Mock, MagicMock, patch, create_autospec


# Use patch will automatically restore your function
# directly change your function by Mock object will perminent change it - hence
#   follow up test will fail

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

class TestMock(unittest.TestCase):

    def setUp(self):
        self.old_add = add
        self.old_sub = sub
        self.assertEqual(10, add(1, 9))

    def tearDown(self):
        global add, sub
        sub = self.old_sub
        add = self.old_add

    def test_mock(self):
        global add
        add = Mock(return_value = 100)
        self.assertEqual(100, add(1, 9))

    def test_mock_side_effect(self):
        global add
        add = Mock(return_value = 100)

        add.side_effect = lambda a, b: a - b
        self.assertEqual(-8, add(1, 9))

    def test_magic_mock(self):
        global add
        add = MagicMock()
        add.__str__.return_value = "I am magic"

        self.assertEqual("I am magic", str(add))

    @patch('libraries.test_mock.add') # TODO
    @patch('libraries.test_mock.sub')
    def test_patch(self, mock_sub, mock_add):
        mock_sub.return_value = 0
        mock_add.return_value = 0

        self.assertEqual(0, sub(1, 9))

        self.assertTrue(not mock_add.called)
        self.assertTrue(mock_sub.called)


    def test_auto_spec(self):
        global add
        add = create_autospec(add, return_value=100)
        self.assertEqual(100, add(1, 9))
        self.assertTrue(add.called)

        with self.assertRaises(TypeError):
            add(1, 2, 3)


