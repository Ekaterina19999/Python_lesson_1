from address import Address
from mailing import Mailing


to_addr = Address("101000", "Москва", "Тверская", "12", "45")


from_addr = Address("630000", "Новосибирск", "Ленина", "5", "12")


shipment = Mailing(to_address=to_addr, from_address=from_addr, cost=350, track="RA123456789RU")


print(
    f"Отправление {shipment.track} из {shipment.from_address.index}, {shipment.from_address.city}, "
    f"{shipment.from_address.street}, {shipment.from_address.house} - {shipment.from_address.apartment} "
    f"в {shipment.to_address.index}, {shipment.to_address.city}, {shipment.to_address.street}, "
    f"{shipment.to_address.house} - {shipment.to_address.apartment}. "
    f"Стоимость {shipment.cost} рублей."
)
