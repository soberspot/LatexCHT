# импортируем модули
import datetime
import pylatex

# создаем документ latex
doc = pylatex.Document()

# определяем переменные из команд latex
data_begin = "01.04.2023"
fio = "Пепец Иван Иванович"

# вычисляем дату отключения как 27 дней после даты начала
data_begin_date = datetime.datetime.strptime(data_begin, "%d.%m.%Y")
data_otklucheniya_date = data_begin_date + datetime.timedelta(days=27)
data_otklucheniya = data_otklucheniya_date.strftime("%d.%m.%Y")

# добавляем команды latex в документ
doc.append(pylatex.Command("newcommand", arguments=["\\исх", "\\ldots"]))
doc.append(pylatex.Command("newcommand", arguments=["\\дата", data_begin]))
doc.append(pylatex.Command("newcommand", arguments=["\\zadolzhennost", "0"]))
doc.append(pylatex.Command("newcommand", arguments=["\\датапроверки", "\\rule{3cm}{0.1 mm}"]))
doc.append(pylatex.Command("newcommand", arguments=["\\датапредупреждения", "\\rule{3cm}{0.1 mm}"]))
doc.append(pylatex.Command("newcommand", arguments=["\\датаотключения", data_otklucheniya]))
doc.append(pylatex.Command("newcommand", arguments=["\\собственник", fio]))
doc.append(pylatex.Command("newcommand", arguments=["\\ФИО", "NAME"]))
doc.append(pylatex.Command("newcommand", arguments=["\\УЛИЦА", "\\ldots"]))
doc.append(pylatex.Command("newcommand", arguments=["\\УЧАСТОК", "\\ldots"]))
doc.append(pylatex.Command("newcommand", arguments=["\\адрес", "\\ldots"]))
doc.append(pylatex.Command("newcommand", arguments=["\\адресвснт", "\\rule{6cm}{0.1 mm}"]))
doc.append(pylatex.Command("newcommand", arguments=["\\датаограничения", "\\ldots"]))
doc.append(pylatex.Command("newcommand", arguments=["\\счетчик", "\\ldots"]))
doc.append(pylatex.Command("newcommand", arguments=["\\лс", "\\ldots"]))
doc.append(pylatex.Command("newcommand", arguments=["\\датапогашения", "\\ldots"]))
doc.append(pylatex.Command("newcommand", arguments=["\\датаотмены", "\\ldots"]))
doc.append(pylatex.Command("newcommand", arguments=["\\исхотмены", "\\ldots"]))

# генерируем файл latex
doc.generate_tex("шаблон.tex")