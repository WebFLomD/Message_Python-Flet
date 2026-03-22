import flet as ft

# Валидация для ввода сообщение
# Включаем кнопку, если есть текст, иначе выключаем
def validate(e, button_message):
    if e.control.value:
        button_message.disabled = False
    else:
        button_message.disabled = True
    
    # Обновляем страницу
    e.page.update()

# Отображение чата
def chat(user_name, text_chat, page, message_list):
    
    # Авто-адаптив сообщения по размеру
    if len(text_chat) < 20:
        msg_width = None
    elif len(text_chat) < 50:
        msg_width = 200
    else:
        msg_width = 300

    # Текст сообщения
    message_text = ft.Text(
        text_chat,
        size=14,
        color=ft.Colors.WHITE,
        max_lines=None, 
        expand=True if msg_width else False # expand только если ширина фиксированная
    )

    # Дата отправления сообщения
    date_chat = ft.Text(
        '13/02/26 10:00',
        color=ft.Colors.GREEN_200, 
        size=10
    )

    # Имя собеседника (только для чужих сообщений)
    username_text = ft.Text(
        user_name,
        color=ft.Colors.WHITE,
        size=16,
        weight=ft.FontWeight.BOLD
    )
    
    # Свое сообщение (синее, справа)
    if user_name == "Я": 
        message = ft.Container(
            content=ft.Column(
                [
                    message_text,
                    date_chat
                ],
                spacing=2,  # Отступ между ними
            ),
            bgcolor="#2B5278",  # Фон сообщения 
            
            border_radius=ft.BorderRadius.only( # Углы сообщения (Дизайн)
                top_left=12, 
                top_right=12, 
                bottom_left=12
            ),  
            padding=10,  # Внутренний отступ
            width=msg_width  # Ширина сообщения, работает через условие
        )
        
        # Выравниваем справа
        message_row = ft.Row(
            [ft.Container(expand=True), message],
            vertical_alignment=ft.CrossAxisAlignment.END
        )
    
    # Сообщение от собеседника (слева)
    else:
        message = ft.Container(
            content=ft.Column(
                [
                    username_text,
                    message_text,
                    date_chat
                ],
                spacing=2
            ),
            bgcolor="#1FA140",  # Фон сообщения собеседника
            border_radius=ft.BorderRadius.only( # Углы сообщения (Дизайн)
                top_left=12, 
                top_right=12, 
                bottom_right=12
            ),  
            padding=10,  # Внутренний отступ
            width=msg_width  # Ширина сообщения, работает через условие
        )
        
        # Выравниваем слева
        message_row = ft.Row(
            [message],
            vertical_alignment=ft.CrossAxisAlignment.START
        )

    # Добавляем сообщение в список
    message_list.controls.append(message_row)
    page.update()  # Исправлено: было page.page.update()

# Отправка сообщение
def send_message(e):
    print("+")