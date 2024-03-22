distanceCharge: float | int = 0
surcharge: float | int = 0
maxDeliveryFee: int = 15
total: float | int = 0
deliveryFee: float | int  = 0

# Function based logic
# def chargableAmount(distance: int,
#                     items: int,
#                     day: str,
#                     hour: int):
#     if distance <= 1000:
#         distanceCharge = 2
#     elif (((distance - 1000) % 500) == 0 and distance != 0):
#         distanceCharge = 2 + (((distance - 1000) / 500) * 2)
#     elif (round((distance - 1000) / 1000) > (distance - 1000) / 1000):
#         distanceCharge = 2 + (round((distance - 1000) / 1000) * 2)
#     else:
#         distanceCharge = 2 + (round((distance - 1000) / 1000) * 2) + 1

#     if (5 <= items < 12):
#         surcharge = (items - 4) * 0.5
#     elif items > 12:
#         surcharge = ((items - 4) * 0.5) + 1.2
#     else:
#         surcharge = 0

#     if (day == "Friday" and 15 <= hour <= 18):
#         total = (surcharge + distanceCharge) * 1.2
#     else:
#         total = surcharge + distanceCharge

#     if total > maxDeliveryFee:
#         print(total)
#         deliveryFee = False
#         return deliveryFee
#     else:
#         deliveryFee = total
#         return deliveryFee

# Class based logic


class ChargableAmt:
    def __init__(self, distance: int, items: int, day: str, hour: int) -> None:
        # Assertions placed purely for educational purposes. Type checking done in views.py
        assert type(distance) == int, f"Distance {distance} is invalid."
        assert type(items) == int, f"Items {items} is invalid."
        assert type(day) == str, f"Day {day} is invalid."
        assert type(hour) == int, f"Hour {hour} is invalid."

        self.__distance = distance
        self.__items = items
        self.__day = day
        self.__hour = hour

    @property
    def distance(self):
        return self.__distance

    @property
    def items(self):
        return self.__items

    @property
    def day(self):
        return self.__day

    @property
    def hour(self):
        return self.__hour

    def __distance_charge(self):
        if self.__distance <= 1000:
            distanceCharge = 2
        elif (((self.__distance - 1000) % 500) == 0 and self.__distance != 0):
            distanceCharge = 2 + (((self.__distance - 1000) / 500) * 2)
        elif (round((self.__distance - 1000) / 1000) > (self.__distance - 1000) / 1000):
            distanceCharge = 2 + \
                (round((self.__distance - 1000) / 1000) * 2)
        else:
            distanceCharge = 2 + \
                (round((self.__distance - 1000) / 1000) * 2) + 1
        return distanceCharge

    def __surcharge(self):
        if (5 <= self.__items < 12):
            surcharge = (self.__items - 4) * 0.5
        elif self.__items > 12:
            surcharge = ((self.__items - 4) * 0.5) + 1.2
        else:
            surcharge = 0
        return surcharge

    def __sum_total(self):
        if (self.__day == "Friday" and 15 <= self.__hour <= 18):
            return ((self.__surcharge() + self.__distance_charge())) * 1.2
        else:
            return (self.__surcharge() + self.__distance_charge())

    def deliveryFee(self):
        total = self.__sum_total()
        deliveryFee = total
        return deliveryFee
