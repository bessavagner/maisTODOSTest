import unittest
from app.validation import CreditCardValidator


class TestCreditCardValidator(unittest.TestCase):

    def setUp(self):
        self.validator = CreditCardValidator()

    def test_is_valid_exp_date_valid(self):
        valid_exp_date = "12/2023"
        result = self.validator.is_valid_exp_date(valid_exp_date)
        self.assertTrue(result)

    def test_is_valid_exp_date_invalid(self):
        invalid_exp_date = "13/2023"
        result = self.validator.is_valid_exp_date(invalid_exp_date)
        self.assertFalse(result)

    def test_is_valid_holder_valid(self):
        valid_holder = "Luan Santos"
        result = self.validator.is_valid_holder(valid_holder)
        self.assertTrue(result)

    def test_is_valid_holder_invalid(self):
        invalid_holder = "L"
        result = self.validator.is_valid_holder(invalid_holder)
        self.assertFalse(result)

    def test_is_valid_card_number_valid(self):
        valid_card_number = "4111111111111111"
        result = self.validator.is_valid_card_number(valid_card_number)
        self.assertTrue(result)

    def test_is_valid_card_number_invalid(self):
        invalid_card_number = "1234"
        result = self.validator.is_valid_card_number(invalid_card_number)
        self.assertFalse(result)

    def test_get_brand_by_card_number(self):
        card_number = "4005519200000004"
        result = self.validator.get_brand_by_card_number(card_number)
        self.assertEqual(result, "visa")

    def test_is_valid_cvv_valid(self):
        valid_cvv = "123"
        result = self.validator.is_valid_cvv(valid_cvv)
        self.assertTrue(result)

    def test_is_valid_cvv_invalid(self):
        invalid_cvv = "12"
        result = self.validator.is_valid_cvv(invalid_cvv)
        self.assertFalse(result)

    def test_format_exp_date(self):
        exp_date = "12/2023"
        result = self.validator.format_exp_date(exp_date)
        self.assertEqual(result, "2023-12-31")


if __name__ == '__main__':
    unittest.main()
