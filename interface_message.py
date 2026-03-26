import flet as ft
from backend_message import sendMessage, validate, loadMessages
from database import db

def message_page (page: ft.Page, user_name, onLogout, user_id):
    page.title = "Чат - Мобильная версия"
    page.bgcolor = "#0E1621" # Фон приложения
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH

    # Устанавливаем мобильный вид (имитация телефона)
    page.window.width = 380
    page.window.height = 700
    page.window.resizable = False

    # Определяем собеседника
    if user_id == 1:  # Если текущий пользователь Алексей
        other_user_id = 2  # То собеседник Анна
        other_user_name = "Анна"
    else:  # Если текущий пользователь Анна
        other_user_id = 1  # То собеседник Алексей
        other_user_name = "Алексей"
    
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

        on_click=lambda e: sendMessage(
            message_input,
            other_user_id,
            other_user_name,
            message_list,
            page,
            db
        )
    )

    # Чат с пользователем
    header = ft.Row(
        [
            ft.Text(
                f"Чат с {other_user_name}",
                size=26,
                color = ft.Colors.WHITE,
                weight=ft.FontWeight.W_500
            ),
            ft.Container(expand=True),
            button_exit          
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    # Пример отображение сообщение
    # chat("Я", "Привет! Как дела? ыавываыва ываы ваыва ываываыва ываа", page, message_list)
    # chat("Анна", "Привет! Все хорошо! А у тебя? dfssdf sdfsdfsdf sdfsdfsdf sdfsdfs fsdfs ddffsdsfd", page, message_list)
    # chat("Я", "Привет! Как дела?", page, message_list)
    loadMessages(other_user_id, message_list, db, page)

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
    