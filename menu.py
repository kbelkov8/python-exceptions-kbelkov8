from cards import(
    Card,
)


class Menu:
    """Класс пользовательского меню."""

    def __init__(self) -> None:
        """Конструктор класса мню."""

        self.__product = Card()

    def print_info(self) -> None:
        """Метод вывода информации меню пользователя."""

        print("\nВыберите действие карты: \n\n"
              "1) Ввести название товара.\n"
              "2) Ввести количество товара.\n"
              "3) Ввести поставщика товара.\n"
              "4) Ввести производителя товара.\n"
              "5) Ввести цену товара.\n"
              "6) Ввести местоположение товара.\n"
              "7) Ввести массу товара.\n"
              "8) Ввести год выпуска товара.\n"
              "9) Ввести номер товара.\n"
              "10) Указать категорию товара.\n"
              "11) Принять товар к учёту.\n"
              "12) Поставить товар на учёт.\n"
              "13) Списать товар с учёта.\n"
              "14) Просмотр название товара.\n"
              "15) Просмотр количество товара.\n"
              "16) Просмотр поставщика товара.\n"
              "17) Просмотр производителя товара.\n"
              "18) Просмотр цены товара.\n"
              "19) Просмотр местоположения товара.\n"
              "20) Просмотр массы товара.\n"
              "21) Просмотр года выпуска товара.\n"
              "22) Просмотр номера товара.\n"
              "23) Просмотр статуса товара.\n"
              "24) Просмотр категории товара.\n"
              "25) Выход\n\n"
        )

    def choose(self, choose: str) -> None:
        """Метод обработки выбранного пользовательского действия."""

        try:
            choose = int(choose)

        except ValueError:
            print("Введите число!")

        else:
            if 0 < choose < 25:
                match choose:
                    case 1:
                        self.__product.set_name(input("Введите название: "))
                    case 2:
                        self.__product.set_quantity(input("Введите количество товара: "))
                    case 3:
                        self.__product.set_provider(input("Введите поставщика товара: "))
                    case 4:
                        self.__product.set_manufacture(input("Введите производителя товара: "))
                    case 5:
                        self.__product.set_price(input("Введите цену товара: "))
                    case 6:
                        self.__product.set_location(input("Введите местоположение товара: "))
                    case 7:
                        self.__product.set_weight(input("Введите массу товара: "))
                    case 8:
                        self.__product.set_year(input("Введите год выпуска товара: "))
                    case 9:
                        self.__product.set_part_number(input("Введите номер товара: "))
                    case 10:
                        self.__product.set_category(input("Введите категорию товара: "))
                    case 11:
                        self.__product.set_status("принято к учёту")
                    case 12:
                        self.__product.set_status("состоит на учёте")
                    case 13:
                        self.__product.set_status("списано")
                    case 14:
                        print(self.__product.get_name())
                    case 15:
                        print(self.__product.get_quantity())
                    case 16:
                        print(self.__product.get_provider())
                    case 17:
                        print(self.__product.get_manufacture())
                    case 18:
                        print(self.__product.get_price())
                    case 19:
                        print(self.__product.get_location())
                    case 20:
                        print(self.__product.get_weight())
                    case 21:
                        print(self.__product.get_year())
                    case 22:
                        print(self.__product.get_part_number())
                    case 23:
                        print(self.__product.get_status())
                    case 24:
                        print(self.__product.get_category())
