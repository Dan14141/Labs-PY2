class Factory:

    #Базовый класс, представляющий завод.

    def __init__(self, name: str, location: str, employees: int, production_capacity: int):
        """
        Создание объекта класса "Factory":
            name (str): Название завода.
            location (str): Местоположение завода.
            employees (int): Количество сотрудников на заводе.
            production_capacity (int): Производственная мощность завода.
        """
        self.name = name
        self.location = location
        self.employees = employees
        self.production_capacity = production_capacity

        # Проверка типа данных для name
        if not isinstance(name, str):
            raise TypeError("Имя завода должно быть строкой.")
        # Проверка типа данных для location
        if not isinstance(location, str):
            raise TypeError("Местоположение завода должно быть строкой.")
        # Проверка типа данных для employees
        if not isinstance(employees, int):
            raise TypeError("Количество сотрудников должно быть целым числом.")
        # Проверка типа данных для production_capacity
        if not isinstance(production_capacity, int):
            raise TypeError("Производственная мощность должна быть целым числом.")

        # Проверка на отрицательные значения
        if employees < 0:
            raise ValueError("Количество сотрудников не может быть отрицательным.")
        if production_capacity < 0:
            raise ValueError("Производственная мощность не может быть отрицательной.")

    def __str__(self) -> str:
        """
        Метод возвращает строковое представление завода.
        """
        return f"Завод: {self.name}, Местоположение: {self.location}, Сотрудники: {self.employees}, Мощность: {self.production_capacity}"

    def __repr__(self) -> str:
        """
        Метод возвращает формальное
        строковое представление завода.
        """
        return f"Factory(name={self.name}, location={self.location}, employees={self.employees}, production_capacity={self.production_capacity})"

    def calculate_productivity(self) -> float:
        """
        Метод озвращает рассчитанную
        производительность завода
        """
        return self.production_capacity / self.employees


class Workshop(Factory):

    # Дочерний класс, представляющий один из цехов на заводе.

    def __init__(self, name: str, location: str, employees: int, production_capacity: int, workshop_type: str):
        """
        Создание объекта класса "Workshop":
            name (str): Название цеха.
            location (str): Местоположение цеха.
            employees (int): Количество сотрудников в цехе.
            production_capacity (int): Производственная мощность цеха.
            workshop_type (str): Тип цеха.
        """
        super().__init__(name, location, employees, production_capacity)
        self.workshop_type = workshop_type

        # Проверка типа данных для workshop_type
        if not isinstance(workshop_type, str):
            raise TypeError("Тип цеха должен быть строкой.")

        # Вызов конструктора родительского класса
        super().__init__(name, location, employees, production_capacity)
        self.workshop_type = workshop_type

    def __str__(self) -> str:
        """
        Метод возвращает строковое представление объекта.
        """
        return f"Цех: {self.name}, Тип: {self.workshop_type}, Местоположение: {self.location}, Сотрудники: {self.employees}, Мощность: {self.production_capacity}"

    def __repr__(self) -> str:
        """
        Метод Возвращает формальное
        строковое представление объекта.
        """
        return f"Workshop(name={self.name}, location={self.location}, employees={self.employees}, production_capacity={self.production_capacity}, workshop_type={self.workshop_type})"

    def calculate_productivity(self) -> float:
        """
        Метод возвращает рассчитанную
        производительность цеха с учётом его типа
        """
        # Перегрузка метода для учета типа цеха
        if self.workshop_type == "механический":
            return (self.production_capacity / self.employees) * 1.2  # Механические цеха обычно более производительны
        else:
            return self.production_capacity / self.employees

    def get_workshop_type(self) -> str:
        # Метод возвращает Тип цеха
        return self.workshop_type