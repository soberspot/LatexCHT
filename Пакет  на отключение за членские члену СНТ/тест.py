# Импортируем модули для работы с файлами и оконным интерфейсом
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem

# Создаем приложение
app = QApplication([])

# Создаем окно приложения
window = QWidget()
window.setWindowTitle("Вывод из файла")

# Читаем файл с помощью pandas
data = pd.read_excel("РЕЕСТР СНТ ЮГТЕКС   2020.xls", sheet_name='Реестр')

# Получаем столбцы "ФИО" и "ДАТА" из данных
names = data["ФИО собственника"]
dates = data["Телефон"]

# Создаем таблицу для вывода данных
table = QTableWidget()
table.setColumnCount(2) # Устанавливаем два столбца
table.setRowCount(len(names)) # Устанавливаем количество строк равное количеству данных
table.setHorizontalHeaderLabels(["ФИО", "ДАТА"]) # Устанавливаем заголовки столбцов

# Заполняем таблицу данными
for i in range(len(names)):
    # Создаем элементы таблицы с данными из столбцов
    name_item = QTableWidgetItem(names[i])
    date_item = QTableWidgetItem(str(dates[i]))
    # Добавляем элементы в таблицу по индексам
    table.setItem(i, 0, name_item)
    table.setItem(i, 1, date_item)

# Показываем таблицу на экране
table.show()

# Запускаем цикл обработки событий приложения
app.exec_()