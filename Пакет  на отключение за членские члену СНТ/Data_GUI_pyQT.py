# Импортируем модуль для работы с оконным интерфейсом
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

# Создаем приложение
app = QApplication([])

# Создаем окно приложения
window = QWidget()
window.setWindowTitle("Запись в файл")
# Увеличиваем размер окна в два раза
window.resize(400, 200)

# Создаем метки и поля ввода для даты и суммы
date_label = QLabel("Дата образования задолженности:")
date_entry = QLineEdit()

sum_label = QLabel("Сумма долга:")
sum_entry = QLineEdit()

# Создаем функцию для записи в файл
def write_to_file():
    # Открываем файл в режиме дозаписи
    file = open("debt.txt", "a")
    # Получаем значения из полей ввода
    date = date_entry.text()
    sum = sum_entry.text()
    # Записываем значения в файл с разделителем ";"
    file.write(date + ";" + sum + "\n")
    # Закрываем файл
    file.close()
    # Очищаем поля ввода
    date_entry.clear()
    sum_entry.clear()

# Создаем кнопку для записи в файл
write_button = QPushButton("Записать в файл")
write_button.clicked.connect(write_to_file)

# Создаем вертикальный компоновщик для расположения виджетов
layout = QVBoxLayout()
layout.addWidget(date_label)
layout.addWidget(date_entry)
layout.addSpacing(10) # Добавляем промежуток между виджетами
layout.addWidget(sum_label)
layout.addWidget(sum_entry)
layout.addSpacing(10) # Добавляем промежуток между виджетами
layout.addWidget(write_button)

# Устанавливаем компоновщик для окна
window.setLayout(layout)

# Показываем окно на экране
window.show()

# Запускаем цикл обработки событий приложения
app.exec_()