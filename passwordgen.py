import random
import string
import pyperclip
import ctypes

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def show_notification(password):
    ctypes.windll.user32.MessageBoxW(0, password, "Generated Password Has Been Copied", 0x40 | 0x1)
    pyperclip.copy(password)

password_length = 12
password = generate_password(password_length)
show_notification(password)
