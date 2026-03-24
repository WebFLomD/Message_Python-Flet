import flet as ft

def main(page: ft.Page):
    page.title = "Чат"
    page.bgcolor = "#0E1621"
    page.window.width = 380
    page.window.height = 700
    page.window.resizable = False
    page.padding = 20
    
    # Храним информацию о пользователе
    current_user = None
    
    # ========== СТРАНИЦА АВТОРИЗАЦИИ ==========
    def auth_page():
        username_field = ft.TextField(
            label="Логин",
            hint_text="Введите логин",
            bgcolor="#17212B",
            focused_border_color="#64B9FF",
            border=ft.InputBorder.UNDERLINE,
            color=ft.Colors.WHITE,
            width=300
        )
        
        password_field = ft.TextField(
            label="Пароль",
            hint_text="Введите пароль",
            bgcolor="#17212B",
            focused_border_color="#64B9FF",
            border=ft.InputBorder.UNDERLINE,
            color=ft.Colors.WHITE,
            password=True,
            width=300
        )
        
        error_text = ft.Text("", color=ft.Colors.RED, size=12, visible=False)
        
        def login_click(e):
            nonlocal current_user
            if username_field.value and password_field.value:
                # Простая проверка
                if username_field.value == "admin" and password_field.value == "123":
                    current_user = username_field.value
                    # Переходим на страницу чата
                    page.clean()  # Очищаем страницу
                    page.add(chat_page())  # Добавляем страницу чата
                    page.update()
                else:
                    error_text.value = "Неверный логин или пароль"
                    error_text.visible = True
                    page.update()
            else:
                error_text.value = "Заполните все поля"
                error_text.visible = True
                page.update()
        
        return ft.Column(
            [
                ft.Text("Добро пожаловать!", size=24, weight=ft.FontWeight.BOLD, color="#64B9FF"),
                ft.Container(height=30),
                username_field,
                ft.Container(height=15),
                password_field,
                ft.Container(height=10),
                error_text,
                ft.Container(height=20),
                ft.ElevatedButton("Войти", on_click=login_click, bgcolor="#64B9FF", color=ft.Colors.WHITE, width=200),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True
        )
    
    # ========== СТРАНИЦА ЧАТА ==========
    def chat_page():
        messages_list = ft.ListView(expand=True, spacing=8, auto_scroll=True)
        
        message_input = ft.TextField(
            hint_text="Сообщение...",
            bgcolor="#17212B",
            border=ft.InputBorder.UNDERLINE,
            focused_border_color="#64B9FF",
            color=ft.Colors.WHITE,
            expand=True
        )
        
        send_btn = ft.IconButton(
            icon=ft.Icons.SEND_ROUNDED,
            icon_color="#64B9FF",
            disabled=True
        )
        
        def send_message(e):
            if message_input.value:
                new_message = ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(current_user, size=12, weight=ft.FontWeight.BOLD, color="#64B9FF"),
                            ft.Text(message_input.value, color=ft.Colors.WHITE, size=14),
                        ],
                        spacing=2
                    ),
                    bgcolor="#2B5278",
                    border_radius=10,
                    padding=10,
                    margin=ft.margin.only(left=50, bottom=5)
                )
                messages_list.controls.append(new_message)
                message_input.value = ""
                send_btn.disabled = True
                page.update()
        
        def validate_input(e):
            send_btn.disabled = not bool(message_input.value)
            page.update()
        
        message_input.on_change = validate_input
        send_btn.on_click = send_message
        
        def logout(e):
            # Возвращаемся на страницу авторизации
            page.clean()
            page.add(auth_page())
            page.update()
        
        return ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("Чат", size=20, weight=ft.FontWeight.BOLD, color="#64B9FF"),
                        ft.Container(expand=True),
                        ft.IconButton(icon=ft.Icons.LOGOUT, icon_color="#64B9FF", on_click=logout),
                    ]
                ),
                ft.Container(height=10),
                messages_list,
                ft.Row([message_input, send_btn], spacing=10)
            ],
            expand=True
        )
    
    # Запускаем со страницы авторизации
    page.add(auth_page())

ft.app(target=main)