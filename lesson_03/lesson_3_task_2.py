from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15", "+79111234567"),
    Smartphone("Samsung", "Galaxy S24", "+79222345678"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79333456789"),
    Smartphone("Google", "Pixel 8", "+79444567890"),
    Smartphone("Huawei", "P60 Pro", "+79555678901")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
    