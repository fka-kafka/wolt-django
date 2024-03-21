from .amountChargable import chargableAmount
from .minimumChargable import MinCharge #minimumChargable
import datetime


def compute(
    cart_value: int,
    distance: int,
    items: int,
    time: str
):
    deliveryFee: int | bool = 0

    dt_object = datetime.datetime.fromisoformat(time[:-1])
    day = dt_object.strftime('%A')
    hour = int(dt_object.strftime('%H'))

    if (10 < cart_value < 200):
        deliveryFee = chargableAmount(distance, items, day, hour)
        return deliveryFee
    elif cart_value < 10:
        #deliveryFee = minimumChargable(cart_value, distance, items, day, hour)
        result = MinCharge(cart_value, distance, items, day, hour)
        return result.deliveryFee()
    else:
        return 0
