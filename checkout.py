from enum import Enum

# Define Payment Modes
class PaymentMode(Enum):
    PAYPAL = 1
    GOOGLEPAY = 2
    CREDITCARD = 3
    UNKNOWN = 99


# Checkout function
def checkout(mode: PaymentMode, amount: float):
    if amount <= 0:
        print("Invalid payment amount! Must be greater than 0.")
        return

    match mode:
        case PaymentMode.PAYPAL:
            print(f"Processing PayPal payment of ${amount:.2f}")
            # Add PayPal-specific logic here

        case PaymentMode.GOOGLEPAY:
            print(f"Processing GooglePay payment of ${amount:.2f}")
            # Add GooglePay-specific logic here

        case PaymentMode.CREDITCARD:
            print(f"Processing Credit Card payment of ${amount:.2f}")
            # Add Credit Card-specific logic here

        case _:
            print("Invalid payment mode selected!")


# Example manual run
if __name__ == "__main__":
    amount = 150.75

    checkout(PaymentMode.PAYPAL, amount)
    checkout(PaymentMode.GOOGLEPAY, amount)
    checkout(PaymentMode.CREDITCARD, amount)
    checkout(PaymentMode.UNKNOWN, amount)
    checkout(PaymentMode.PAYPAL, -10)  # Invalid amount example
