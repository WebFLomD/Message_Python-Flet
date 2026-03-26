import flet as ft
from datetime import datetime

# Валидация для ввода сообщение
# Включаем кнопку, если есть текст, иначе выключаем
def validate(e, button):
    if e.control.value:
        button.disabled = False
    else:
        button.disabled = True
    
    # Обновляем страницу
    e.page.update()

# Отображение чата
""" Параметры:

    - user_name: имя отправителя ("Я" или имя собеседника)
    - text_chat: текст сообщения
    - date_str: дата и время сообщения
    - message_list: ListView куда добавлять сообщение
    - page: страница для обновления
"""
def chat(user_name, text_chat, date_str, message_list, page):
    
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
        date_str,
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
    page.update()

# Отправляет сообщение в БД и отображает его
def sendMessage(messageInput, currentChatUserId, currentChatUserName, messageList, page, db):
    messageText = messageInput.value.strip()
    if not messageText or not currentChatUserId:
        return

    # Отправляем в БД
    if db.sendMessage(currentChatUserId, messageText):
        # Очищаем поле ввода
        messageInput.value = ""

        # Добавляем сообщение в чат
        currentTime = datetime.now().strftime("%d/%m/%y %H:%M")
        chat("Я", messageText, currentTime, messageList, page)

        # Обновляем страницу
        page.update()

# Загружаем сообщенние в Чат
def loadMessages(otherUserId, messageList, db, page):
    messages = db.getMessage(otherUserId)
    messageList.controls.clear()

    for msg_id, from_id, to_id, message_text, date, from_name, to_name in messages:
        # Определяем, чье сообщение
            if from_id == db.currentUserId:
                user_display = "Я"
            else:
                user_display = from_name
            
            # Форматируем дату
            if isinstance(date, datetime):
                date_str = date.strftime("%d/%m/%y %H:%M")
            else:
                date_str = str(date)[:16]
            
            # Добавляем сообщение в список
            chat(user_display, message_text, date_str, messageList, page)
        
    page.update()