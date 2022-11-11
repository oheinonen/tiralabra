import unittest
from summa import Laskin


class TestLaskin(unittest.TestCase):
    def test_yksi_summa_oikein(self):
        laskin = Laskin()
        res = laskin._laske_summa(10, 19)

        self.assertEqual(res, 29)
