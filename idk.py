#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil

# Попытка включить цветной вывод
USE_COLOR = False
try:
    import colorama
    colorama.init()
    USE_COLOR = True
except Exception:
    USE_COLOR = False

class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    CYAN = "\033[36m"
    GREEN = "\033[32m"
    MAGENTA = "\033[35m"
    YELLOW = "\033[33m"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def boxed_text(lines, double=False):
    if double:
        tl, tr, bl, br, h, v = '╔','╗','╚','╝','═','║'
    else:
        tl, tr, bl, br, h, v = '┌','┐','└','┘','─','│'
    maxlen = max(len(line) for line in lines)
    top = tl + h*(maxlen + 2) + tr
    bottom = bl + h*(maxlen + 2) + br
    middle = [f"{v} {line.ljust(maxlen)} {v}" for line in lines]
    return [top] + middle + [bottom]

def center_lines(lines):
    width = shutil.get_terminal_size((80, 20)).columns
    return [line.center(width) for line in lines]

def print_menu():
    print("Красивая программа — вывод сообщения\n")
    print("1) Обычный вывод")
    print("2) В рамке (одинарной)")
    print("3) В рамке (двойной)")
    print("4) Цветной")
    print("5) Центрированный")
    print("0) Выход\n")

def get_lines():
    return [
        "Етот Код был создан для того чтобы Репозиторий не Удалили",
        "Надеюсь вам нравятца мои проекты"
    ]

def wait_key():
    input("\nНажми Enter чтобы вернуться в меню...")

def main():
    while True:
        clear()
        print_menu()
        choice = input("Выбери стиль (0-5): ").strip()
        if choice == '0':
            clear()
            print("До встречи 👋")
            break

        lines = get_lines()
        clear()

        if choice == '1':
            for l in lines:
                print(l)
        elif choice == '2':
            for l in boxed_text(lines, double=False):
                print(l)
        elif choice == '3':
            for l in boxed_text(lines, double=True):
                print(l)
        elif choice == '4':
            colors = [C.GREEN, C.MAGENTA, C.YELLOW]
            for i, l in enumerate(lines):
                color = colors[i % len(colors)]
                if USE_COLOR:
                    print(f"{C.BOLD}{color}{l}{C.RESET}")
                else:
                    print(l)
        elif choice == '5':
            for l in center_lines(lines):
                print(l)
        else:
            print("Неверный выбор!")

        wait_key()

if __name__ == "__main__":
    main()
