from address import Address
from mailing import Mailing

to_addr = Address("101000", "Москва", "Тверская", "12", "45")
from_addr = Address("630000", "Новосибирск", "Ленина", "5", "12")

shipment = Mailing(to_addr, from_addr, 350, "RA123456789RU")

print(
    f"Отправление {shipment.track} из "
    f"{shipment.from_address.index}, "
    f"{shipment.from_address.city}, "
    f"{shipment.from_address.street}, "
    f"{shipment.from_address.house} - "
    f"{shipment.from_address.apartment} в "
    f"{shipment.to_address.index}, "
    f"{shipment.to_address.city}, "
    f"{shipment.to_address.street}, "
    f"{shipment.to_address.house} - "
    f"{shipment.to_address.apartment}. "
    f"Стоимость {shipment.cost} рублей."
)
