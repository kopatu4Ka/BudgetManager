from database import add_transaction, delete_transaction, clear_db, get_transactions

def main():
    while True:
        print("\nВыберите действие:")
        print("1. Добавить транзакцию")
        print("2. Удалить транзакцию")
        print("3. Показать все транзакции")
        print("4. Очистить все транзакции")
        print("5. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            amount = float(input("Сумма: "))
            category = input("Категория: ")
            type_ = input("Тип (Доход/Расход): ").strip()
            date = input("Дата (ГГГГ-ММ-ДД): ")
            add_transaction(amount, category, type_, date)
            print("Транзакция добавлена!")

        elif choice == "2":
            trans_id = int(input("Введите ID транзакции для удаления: "))
            delete_transaction(trans_id)
            print("Транзакция удалена!")

        elif choice == "3":
            get_transactions()

        elif choice == "4":
            clear_db()
            print("История транзакций была очищена!")

        elif choice == "5":
            print("Выход из программы...")
            break
        else:
            print("Ошибка: выберите корректный номер.")


if __name__ == "__main__":
    main()