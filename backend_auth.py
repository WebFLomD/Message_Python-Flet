import flet as ft

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

def authUsers(username, password):
    if username == "123" and password == "123":
        return True
    return False

def clickAuth(usernameField, passwordField, textError, onSuccess, e):
    if authUsers(usernameField.value, passwordField.value):
        print("Успешный вход!")
        onSuccess(usernameField.value)
    else:
        textError.value = "Неверный логин или пароль"
        textError.visible = True
        e.page.update()