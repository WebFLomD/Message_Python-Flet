import flet as ft
from interface_auth import auth_page
from interface_message import message_page

def main(page: ft.Page):
    def show_message(user_name):
        page.clean()
        page.add(message_page(page, user_name, lambda: show_auth()))
        page.update()

    def show_auth():
        page.clean()
        page.add(auth_page(page, show_message))
        page.update()
    
    show_auth()

ft.app(target=main)