import pytest
from io import StringIO
from contextlib import redirect_stdout
from checkout import checkout, PaymentMode


@pytest.mark.parametrize("mode,expected_output", [
    (PaymentMode.PAYPAL, "Processing PayPal payment of $150.75"),
    (PaymentMode.GOOGLEPAY, "Processing GooglePay payment of $150.75"),
    (PaymentMode.CREDITCARD, "Processing Credit Card payment of $150.75"),
    (PaymentMode.UNKNOWN, "Invalid payment mode selected!"),
])
def test_checkout_modes(mode, expected_output):
    # Capture console output
    f = StringIO()
    with redirect_stdout(f):
        checkout(mode, 150.75)
    output = f.getvalue().strip()
    assert expected_output in output


def test_checkout_invalid_amount():
    f = StringIO()
    with redirect_stdout(f):
        checkout(PaymentMode.PAYPAL, -50)
    output = f.getvalue().strip()
    assert "Invalid payment amount" in output
