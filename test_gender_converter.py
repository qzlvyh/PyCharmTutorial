from unittest import TestCase

from gender_converter import aconverter_gender


class Test(TestCase):
    def test_converter_gender_M(self):
        expected = "MALE"
        actual = aconverter_gender("M")
        self.assertEqual(expected, actual)

    def test_converter_gender_F(self):
        expected = "FEMALE"
        actual = aconverter_gender("F")
        self.assertEqual(expected, actual)
#  self.fail()
