import flet as ft
from backend import send_message, validate, chat

def main (page: ft.Page):
    page.title = "Чат - Мобильная версия"
    page.bgcolor = "#0E1621" # Фон приложения
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH

    # Устанавливаем мобильный вид (имитация телефона)
    page.window.width = 380
    page.window.height = 700
    page.window.resizable = False

    # Список сообщений
    message_list = ft.ListView(
        expand=True,
        auto_scroll=True,
        spacing=8,
    )

    # Кнопка отправить сообщение
    button_message = ft.IconButton(
        ft.Icons.SEND,
        disabled=True,
        on_click=send_message
    )

    # Поле ввода сообщение
    message_input = ft.TextField(
        hint_text="Cообщение...",
        bgcolor= "#17212B",
        border=ft.InputBorder.UNDERLINE,
        focused_border_color="#64B9FF",
        on_change = lambda e: validate(e, button_message),
        expand=True
    )

    # Пример отображение сообщение
    chat("Анна", "Привет! Как дела? ыавываыва ываы ваыва ываываыва ываа", page, message_list)
    chat("Я", "Привет! Все хорошо! А у тебя? dfssdf sdfsdfsdf sdfsdfsdf sdfsdfs fsdfs ddffsdsfd", page, message_list)


    page.add(
        ft.Column(
            [
                ft.Row(
                    ft.Text(value="Семейный чат", size=26, weight=ft.FontWeight.W_500),
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Container(height=10),
                message_list,
                ft.Row(
                    [message_input, button_message]
                )
            ],
            expand=True
        )
    )

# Запуск приложения
ft.app(target=main)