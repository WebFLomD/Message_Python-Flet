import flet as ft
from database import db

# Валидация для ввода сообщение
# Включаем кнопку, если есть текст, иначе выключаем
def validate(e, allFields, button):
    if all(f.value for f in allFields):
        button.disabled = False
        button.bgcolor = "#2B5278"
    else:
        button.disabled = True
        button.bgcolor = "#008CFF" 
            
    # Обновляем страницу
    e.page.update()

# Проверка для авторизации
def authUsers(username, password):
    result = db.checkLogin(username, password)

    if result:
        return True, result  # success=True, name=имя
    else:
        return False, None  # success=False, name=None

def clickAuth(usernameField, passwordField, textError, onSuccess, e):
    success, userName = authUsers(usernameField.value, passwordField.value)
    
    if success:
        print(f"Успешный вход!")
        onSuccess(userName)
    else:
        textError.value = "Неверный логин или пароль"
        textError.visible = True
        e.page.update()