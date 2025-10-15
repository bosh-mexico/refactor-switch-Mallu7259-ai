import unittest
from payment_service import checkout, PaymentMode, process_creditcard, process_googlepay, process_paypal
from unittest.mock import patch

class TestCheckOut(unittest.TestCase):

    @patch('payment_service.process_googlepay')
    @patch('builtins.print')
    def test_google_pay_handler(self, mock_print, mock_process_googlepay):
        amt = 100
        checkout(PaymentMode.GOOGLEPAY, amt)
        mock_process_googlepay.assert_called_once_with(amt)

    @patch('payment_service.process_creditcard')
    @patch('builtins.print')
    def test_credit_card_handler(self, mock_print, mock_process_credit):
        amt = 150
        checkout(PaymentMode.CREDITCARD, amt)
        mock_process_credit.assert_called_once_with(amt)

    @patch('payment_service.process_paypal')
    @patch('builtins.print')
    def test_paypal_handler(self, mock_print, mock_process_payal):
        amt = 200
        checkout(PaymentMode.PAYPAL, amt)
        mock_process_payal.assert_called_once_with(amt)
    
    @patch('builtins.print')
    def test_default_handler(self, mock_print):
        amt=100
        checkout(PaymentMode.UNKNOWN, amt)
        mock_print.assert_called_once_with("Invalid payment mode selected!")

if __name__ == "__main__":
    unittest.main()
