class Card:
    """Класс карточек."""

    def __init__(self) -> None:
        """Конструктор класса Card."""

        self.__name = None
        self.__quantity = None
        self.__status = "в обработке"
        self.__provider = None
        self.__manufacture = None
        self.__price = None
        self.__location = None
        self.__weight = None
        self.__year = None
        self.__part_number = None
        self.__category = None

    def set_name(self, name: str) -> None:
        """Сеттер названия товара.

        Args:
             name: Название товара.
        """


        self.__name = name
        print("Принято")

    def set_quantity(self, quantity: str) -> None:
        """Сеттер количества товара.

        Args:
             quantity: Количество товара.
        """

        try:
            if int(quantity) >= 0:
                self.__quantity = quantity
                print("Принято")
            else:
                print("Введено некорректное значение!")

        except ValueError:
            print("Введено некорректное значение!")

    def set_status(self, status: str) -> None:
        """Сеттер состояния товара.

        Args:
             status: Состояние товара.
        """

        if status == "списано":
            if self.__status == "принято к учёту" or self.__status == "состоит на учёте":
                self.__status = status
                print("Успешно списано")
            else:
                print("Товар не числится на учёте")
        else:
            self.__status = status
            print("Статус успешно изменён")

    def set_provider(self, provider: str) -> None:
        """Сеттер поставщика товара.

        Args:
             provider: Поставщик товара.
        """

        self.__provider = provider
        print("Поставщик успешно указан")

    def set_manufacture(self, manufacture: str) -> None:
        """Сеттер производителя товара.

        Args:
             manufacture: Производитель товара.
        """

        self.__manufacture = manufacture
        print("Производитель успешно указан")

    def set_price(self, price: str) -> None:
        """Сеттер цены товара.

        Args:
             price: Цена товара.
        """

        try:
            if float(price) > 0:
                self.__price = price
                print("Цена успешно указана")
            else:
                print("Введено некорректное значение!")

        except ValueError:
            print("Введено некорректное значение")

    def set_location(self, location: str) -> None:
        """Сеттер местоположения товара.

        Args:
             location: Местоположение товара.
        """

        self.__location = location
        print("Местоположение успешно указано")

    def set_weight(self, weight: str) -> None:
        """Сеттер массы товара.

        Args:
             weight: Масса товара.
        """

        try:
            if float(weight) > 0:
                self.__weight = weight
                print("Масса успешно указана")
            else:
                print("Введено некорректное значение!")

        except ValueError:
            print("Введено некорректное значение")

    def set_year(self, year: str) -> None:
        """Сеттер года выпуска товара.

        Args:
             year: Год выпуска товара.
        """

        try:
            if 2000 <= int(year) <= 2026:
                self.__year = year
                print("Год успешно указан")
            else:
                print("Введено некорректное значение!")

        except ValueError:
            print("Введено некорректное значение!")

    def set_part_number(self, part_number: str) -> None:
        """Сеттер номера товара.

        Args:
             part_number: Номер товара.
        """

        self.__part_number = part_number
        print("Номер товара успешно указан")

    def set_category(self, category: str) -> None:
        """Сеттер категории товара.

        Args:
                category: Категория товара.
        """

        self.__category = category
        print("Категория товара успешно указана")

    def get_name(self) -> str:
        """Геттер названия товара.

        Returns:
                name: Название товара.
        """

        return self.__name

    def get_quantity(self) -> int:
        """Геттер количества товара.

        Returns:
                quantity: Количество товара.
        """

        return self.__quantity

    def get_status(self) -> str:
        """Геттер состояния товара.

        Returns:
                status: Состояние товара.
        """

        return self.__status

    def get_provider(self) -> str:
        """Геттер поставщика товара.

        Returns:
                provider: Поставщик товара.
        """

        return self.__provider

    def get_manufacture(self) -> str:
        """Геттер производителя товара.

        Returns:
                manufacture: Производитель товара.
        """

        return self.__manufacture

    def get_price(self) -> float:
        """Геттер цены товара.

        Returns:
                price: Цена товара.
        """

        return self.__price

    def get_location(self) -> str:
        """Геттер местоположения товара.

        Returns:
                location: Местоположение товара.
        """

        return self.__location

    def get_weight(self) -> float:
        """Геттер массы товара.

        Returns:
                weight: Масса товара.
        """

        return self.__weight

    def get_year(self) -> int:
        """Геттер года выпуска товара.

        Returns:
                year: Год выпуска товара.
        """

        return self.__year

    def get_part_number(self) -> str:
        """Геттер номера товара.

        Returns:
                part_number: Номер товара.
        """

        return self.__part_number

    def get_category(self) -> str:
        """Сеттер категории товара.

        Returns:
                category: Категория товара.
        """

        return self.__category
