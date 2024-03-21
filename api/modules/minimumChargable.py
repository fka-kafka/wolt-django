distanceCharge: float | int = 0
surcharge: float | int = 0
maxDeliveryFee: int = 15
total: float | int = 0
deliveryFee: float | int | bool = 0

# Function based logic
# def minimumChargable(cart_value: int,
#                      distance: int,
#                      items: int,
#                      day: str,
#                      hour: int):
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
#         total = ((surcharge + distanceCharge + (10 - cart_value))) * 1.2
#     else:
#         total = surcharge + distanceCharge + (10 - cart_value)

#     if total > maxDeliveryFee:
#         deliveryFee = False
#         return deliveryFee
#     else:
#         deliveryFee = total
#         return deliveryFee


# Class based logic
class MinCharge:
    def __init__(self, cart_value: int, distance: int, items: int, day: str, hour: int) -> None:
        # Assertions placed purely for educational purposes
        assert type(cart_value) == int, f"Cart value {cart_value} is invalid."
        assert type(distance) == int, f"Distance {distance} is invalid."
        assert type(items) == int, f"Items {items} is invalid."
        assert type(day) == str, f"Day {day} is invalid."
        assert type(hour) == int, f"Hour {hour} is invalid."

        self.__cart_value = cart_value
        self.__distance = distance
        self.__items = items
        self.__day = day
        self.__hour = hour

    @property
    def cart_value(self):
        return self.__cart_value

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
            distanceCharge = 2 + (round((self.__distance - 1000) / 1000) * 2)
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
            return ((self.__surcharge() + self.__distance_charge() + (10 - self.__cart_value))) * 1.2
        else:
            return (self.__surcharge() + self.__distance_charge() + (10 - self.__cart_value))

    def deliveryFee(self):
        total = self.__sum_total()
        deliveryFee = False if total > maxDeliveryFee else total
        return deliveryFee
