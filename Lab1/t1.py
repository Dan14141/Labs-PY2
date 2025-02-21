# TODO: Подробно описать три произвольных класса
import doctest

class Factory:
    def __init__(self, name: str, employees: int):
        """
        Создание объекта класса "Завод"
        :param name: Название завода
        :param employees: Количество сотрудников

        Примеры:
        >>> factory = Factory("SteelCorp", 500) # Инициализация объекта класса
        """
        if not isinstance(name, str):
            raise TypeError("Название завода должно быть строкой")
        if not isinstance(employees, int) or employees < 0:
            raise ValueError("Количество сотрудников должно быть неотрицательным целым числом")
        self.name = name
        self.employees = employees

    def is_operational(self) -> bool:
        """
        Проверяет, работает ли завод

        Примеры:
        >>> factory = Factory("SteelCorp", 500)
        >>> factory.is_operational()
        """

class School:
    def __init__(self, name: str, students: int):
        """
        Создание объекта класса "Школа"

        :param name: Название школы
        :param students: Количество учеников

        Примеры:
        >>> school = School("Greenwood High", 1200)
        """
        if not isinstance(name, str):
            raise TypeError("Название школы должно быть строкой")
        if not isinstance(students, int) or students < 0:
            raise ValueError("Количество учеников должно быть неотрицательным целым числом")
        self.name = name
        self.students = students

    def is_large_school(self) -> bool:
        """
        Проверяет, является ли школа крупной (более 1000 учеников)

        Примеры:
        >>> school = School("Greenwood High", 1200)
        >>> school.is_large_school()
        """

class University:
    def __init__(self, name: str, faculties: int):
        """
        Создание объекта класса "Университет"

        :param name: Название университета
        :param faculties: Количество факультетов

        Примеры:
        >>> university = University("MIT", 10)
        """
        if not isinstance(name, str):
            raise TypeError("Название университета должно быть строкой")
        if not isinstance(faculties, int) or faculties < 0:
            raise ValueError("Количество факультетов должно быть неотрицательным целым числом")
        self.name = name
        self.faculties = faculties

    def has_many_faculties(self) -> bool:
        """
        Проверяет, является ли университет многопрофильным (более 5 факультетов)

        Примеры:
        >>> university = University("MIT", 10)
        >>> university.has_many_faculties()
        """

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
