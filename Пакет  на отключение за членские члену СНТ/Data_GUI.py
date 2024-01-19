# Импортируем модуль для работы с оконным интерфейсом
import tkinter as tk

# Создаем окно приложения
window = tk.Tk()
window.title("Запись в файл")
# Увеличиваем размер окна в два раза
window.geometry("400x200")

# Создаем метки и поля ввода для даты и суммы
date_label = tk.Label(window, text="Дата образования задолженности:")
date_label.grid(row=0, column=0)
date_entry = tk.Entry(window)
date_entry.grid(row=0, column=1)

# Добавляем пустую строку для увеличения расстояния
tk.Label(window).grid(row=1)

sum_label = tk.Label(window, text="Сумма долга:")
sum_label.grid(row=2, column=0)
sum_entry = tk.Entry(window)
sum_entry.grid(row=2, column=1)

# Добавляем пустую строку для увеличения расстояния
tk.Label(window).grid(row=3)

# Создаем функцию для записи в файл
def write_to_file():
    # Открываем файл в режиме дозаписи
    file = open("debt.txt", "a")
    # Получаем значения из полей ввода
    date = date_entry.get()
    sum = sum_entry.get()
    # Записываем значения в файл с разделителем ";"
    file.write(date + ";" + sum + "\n")
    # Закрываем файл
    file.close()
    # Очищаем поля ввода
    date_entry.delete(0, tk.END)
    sum_entry.delete(0, tk.END)

# Создаем кнопку для записи в файл
write_button = tk.Button(window, text="Записать в файл", command=write_to_file)
write_button.grid(row=4, column=0, columnspan=2)

# Запускаем цикл обработки событий окна
window.mainloop()