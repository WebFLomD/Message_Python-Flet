import flet as ft
from backend_auth import validate, clickAuth

def auth_page(page: ft.Page, show_message):
    page.title = "Авторизация"
    page.bgcolor = "#0E1621"
    
    # Устанавливаем мобильный вид (имитация телефона)
    page.window.width = 380
    page.window.height = 700
    page.window.resizable = False

    def loginClick(e):
        clickAuth(username_field, password_field, textError, show_message, e)

    username_field = ft.TextField(
        label="Логин",
        color= "#FFFFFF",
        bgcolor= "#17212B",
        focused_border_color="#64B9FF",
        border=ft.InputBorder.OUTLINE,
        expand=True,

        on_change= lambda e: validate(e, [username_field, password_field], button_auth)
    )

    password_field = ft.TextField(
        label="Пароль",
        color= "#FFFFFF",
        bgcolor= "#17212B",
        focused_border_color="#64B9FF",
        border=ft.InputBorder.OUTLINE,
        expand=True,
        password=True,

        on_change= lambda e: validate(e, [username_field, password_field], button_auth)
    )

    button_auth = ft.ElevatedButton(
        "Войти",
        width=200,
        height=40,
        bgcolor="#008CFF",
        color=ft.Colors.WHITE,
        disabled = True,
        
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=3), 
            text_style=ft.TextStyle(
                size=18, 
                weight=ft.FontWeight.W_500
            ),
            mouse_cursor=ft.MouseCursor.CLICK
        ),

        on_click = loginClick
    )

    textError = ft.Text(
        value="", 
        color="#FF0000", 
        visible=False
    )

    return ft.Column(
        [
            ft.Container(height=190),
            ft.Text("Добро пожаловать!", size=24, weight=ft.FontWeight.BOLD),
            ft.Container(height=10),
            username_field,
            password_field,
            ft.Container(height=5),
            button_auth,
            textError
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )