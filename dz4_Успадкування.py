class Phone:
    def __init__(self, phone_model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.phone_model = phone_model
    def call(self):
        print(f"Виконується дзвінок з моделі {self.phone_model})")
class Camera:
    def __init__(self, megapixels, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.megapixels = megapixels

    def take_photo(self):
        print(f"йоу фотографія збережена в галерею (камера {self.megapixels} МП)")
class Smartphone(Phone, Camera):
    def __init__(self, phone_model, megapixels, brand):
        self.brand = brand
        super().__init__(phone_model=phone_model, megapixels=megapixels)
    def show_all_features(self):
        print(f"Запуск функцій смартфона {self.brand} ({self.phone_model}, {self.megapixels} МП)")
        self.call()
        self.take_photo()
my_smartphone = Smartphone("iPhone 15", 48, "Apple")
my_smartphone.show_all_features()