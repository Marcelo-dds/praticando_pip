import keyboard
import time

# Pressiona tecla Win para abrir o menu iniciar
keyboard.press_and_release('win')
time.sleep(0.5)

# Digita "chrome"
keyboard.write('chrome')
time.sleep(0.5)

# Pressiona Enter para abrir o Chrome
keyboard.press_and_release('enter')
time.sleep(2)  # Aguarda o Chrome abrir

# Pressiona Ctrl+T para abrir nova aba
keyboard.press_and_release("ctrl+t")
time.sleep(0.5)

# Digita a URL
keyboard.write('https://www.google.com/')
time.sleep(0.2)

# Pressiona Enter
keyboard.press_and_release("enter")
