from menu import(
    Menu,
)


def run():
    """Функция запуска программы."""

    product = Menu()

    choose = ""

    while choose != "25":
        product.print_info()

        choose = input("Выберите действие: ")

        product.choose(choose)

run()