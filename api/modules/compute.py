from .amountChargable import ChargableAmt  # chargableAmount
from .minimumChargable import MinCharge  # minimumChargable
import datetime


def compute(
    cart_value: int,
    distance: int,
    items: int,
    time: str
):
    # deliveryFee: int | bool = 0
    date_object = datetime.datetime.fromisoformat(time[:-1])
    day = date_object.strftime('%A')
    hour = int(date_object.strftime('%H'))

    if (10 < cart_value < 200):
        # deliveryFee = chargableAmount(distance, items, day, hour)
        result = ChargableAmt(distance, items, day, hour)
        return result.deliveryFee()
    elif cart_value < 10:
        # deliveryFee = minimumChargable(cart_value, distance, items, day, hour)
        result = MinCharge(cart_value, distance, items, day, hour)
        return result.deliveryFee()
    else:
        return 0
