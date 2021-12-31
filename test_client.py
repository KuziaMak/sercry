from client import PortAddr,Msg
import unittest


class MainTest(unittest.TestCase):

    def test_portaddr(self):
        self.assertEqual(PortAddr(),[7777,'localhost'])
    def test_Msg(self):
        self.assertEqual(type(Msg()),bytes)



if __name__ == '__main__':
    unittest.main()