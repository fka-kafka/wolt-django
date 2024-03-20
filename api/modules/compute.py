from .amountChargable import chargableAmount
from .minimumChargable import minimumChargable
import datetime


def compute(
    cartValue: int,
    distance: int,
    items: int,
    time: str
):
    deliveryFee: int | bool = 0

    dt_object = datetime.datetime.fromisoformat(time[:-1])
    day = dt_object.strftime('%A')
    hour = int(dt_object.strftime('%H'))

    print(hour, type(hour), day)

    if (10 << cartValue << 200):
        deliveryFee = chargableAmount(distance, items, day, hour)
        return deliveryFee
    elif cartValue < 10:
        deliveryFee = minimumChargable(cartValue, distance, items, day, hour)
        return deliveryFee
    else:
        return 0
