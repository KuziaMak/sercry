from server import PortAddr
import unittest


class MainTest(unittest.TestCase):

    def test_portaddr(self):
        self.assertEqual(PortAddr(),[7777,''])


if __name__ == '__main__':
    unittest.main()