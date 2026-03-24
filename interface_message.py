import flet as ft
from backend_message import send_message, validate, chat

def message_page (page: ft.Page, user_name, onLogout):
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

    # Кнопка ВЫХОД - Выйти с учетной записи
    button_exit = ft.IconButton(
        ft.Icons.EXIT_TO_APP,
        icon_color = ft.Colors.WHITE,
        on_click=lambda e: onLogout()
    )

    # Поле ввода сообщение
    message_input = ft.TextField(
        hint_text="Cообщение...",
        bgcolor= "#17212B",
        border=ft.InputBorder.UNDERLINE,
        focused_border_color="#64B9FF",
        expand=True,

        on_change = lambda e: validate(e, button_message)
    )

    # Кнопка отправить сообщение
    button_message = ft.IconButton(
        ft.Icons.SEND,
        disabled=True,
    )

    header = ft.Row(
        [
            ft.Text(
                "Чат",
                size=26,
                color = ft.Colors.WHITE,
                weight=ft.FontWeight.W_500
            ),
            ft.Container(expand=True),
            button_exit          
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    
    button_message.on_click = lambda e: send_message(message_input)

    # Пример отображение сообщение
    chat("Я", "Привет! Как дела? ыавываыва ываы ваыва ываываыва ываа", page, message_list)
    chat("Анна", "Привет! Все хорошо! А у тебя? dfssdf sdfsdfsdf sdfsdfsdf sdfsdfs fsdfs ddffsdsfd", page, message_list)
    chat("Я", "Привет! Как дела?", page, message_list)


    
    return ft.Column(
        [
            header,
            ft.Container(height=10),
            message_list,
            ft.Row(
                [message_input, button_message]
            )
        ],
            expand=True
        )
    