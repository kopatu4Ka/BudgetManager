import flet as ft
from Test_Version import database


def build_ui(page: ft.Page):
    page.title = "Трекер расходов"

    amount_input = ft.TextField(label="Сумма", width=200)
    category_input = ft.TextField(label="Категория", width=200)
    type_dropdown = ft.Dropdown(
        label="Тип",
        options=[
            ft.dropdown.Option("Доход", "Доход"),
            ft.dropdown.Option("Расход", "Расход"),
        ],
        width=200
    )
    date_input = ft.TextField(label="Дата (ГГГГ-ММ-ДД)", width=200)

    transactions_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Сумма")),
            ft.DataColumn(ft.Text("Категория")),
            ft.DataColumn(ft.Text("Тип")),
            ft.DataColumn(ft.Text("Дата")),
            ft.DataColumn(ft.Text("Действие")),
        ],
        rows=[]
    )

    def load_transactions():
        transactions_table.rows.clear()
        transactions = database.get_transactions()
        for transaction in transactions:
            trans_id, amount, category, type_, date = transaction
            transactions_table.rows.append(
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(trans_id))),
                    ft.DataCell(ft.Text(str(amount))),
                    ft.DataCell(ft.Text(category)),
                    ft.DataCell(ft.Text(type_)),
                    ft.DataCell(ft.Text(date)),
                    ft.DataCell(ft.ElevatedButton("Удалить", on_click=lambda e, t_id=trans_id: delete_transaction(int(t_id)))),
                ])
            )
        page.update()

    def add_transaction(e):
        if amount_input.value and category_input.value and type_dropdown.value and date_input.value:
            database.add_transaction(
                float(amount_input.value),
                category_input.value,
                type_dropdown.value,
                date_input.value
            )
            amount_input.value = category_input.value = date_input.value = ""
            load_transactions()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Заполните все поля!"), open=True)
        page.update()

    def delete_transaction(trans_id):
        database.delete_transaction(trans_id)
        load_transactions()

    def clear_all(e):
        database.clear_db()
        load_transactions()

    add_button = ft.ElevatedButton("Добавить", on_click=add_transaction)
    clear_button = ft.ElevatedButton("Очистить все", on_click=clear_all)

    page.add(
        ft.Row([amount_input, category_input, type_dropdown, date_input]),
        ft.Row([add_button, clear_button]),
        transactions_table
    )

    load_transactions()
