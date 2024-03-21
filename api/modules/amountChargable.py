distanceCharge: int = 0
surcharge: int = 0
maxDeliveryFee: int = 15
total: int = 0
deliveryFee: int | bool = 0


def chargableAmount(distance: int,
                    items: int,
                    day: str,
                    hour: int):
    if distance <= 1000:
        distanceCharge = 2
    elif (((distance - 1000) % 500) == 0 and distance != 0):
        distanceCharge = 2 + ((distance - 1000) / 500) * 2
    elif (round((distance - 1000) / 1000) > (distance - 1000) / 1000):
        distanceCharge = 2 + (round((distance - 1000) / 1000) * 2)
    else:
        distanceCharge = 2 + (round((distance - 1000) / 1000) * 2) + 1

    if (5 <= items < 12):
        surcharge = (items - 4) * 0.5
    elif items > 12:
        surcharge = ((items - 4) * 0.5) + 1.2
    else:
        surcharge = 0

    if (day == "Friday" and 15 <= hour <= 18):
        total = (surcharge + distanceCharge) * 1.2
    else:
        total = surcharge + distanceCharge

    if total > maxDeliveryFee:
        print(total)
        deliveryFee = False
        return deliveryFee
    else:
        deliveryFee = total
        return deliveryFee

