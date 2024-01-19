from pytrovich.enums import NamePart, Gender, Case
from pytrovich.maker import PetrovichDeclinationMaker
import argparse
import datetime
from pathlib import Path
from numpy import nan
import pandas as pd
import os
import shutil

maker = PetrovichDeclinationMaker('rules.json')
# maker = PetrovichDeclinationMaker()
#
date_string = datetime.datetime.now().strftime('%Y-%m-%d')
parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("--name", default=None, type=str, help="Your name")


def FileExcel(file, list):     # читает файл excel
    src_file = Path.cwd() / file
    df = pd.read_excel(src_file, sheet_name=list, header=0, usecols='A:Z')
    return df


def fio(name):
    parts = name.split()
    return f'{parts[0]} {parts[1][0]}.{parts[2][0]}.'


def fio_1(name):
    parts = name.split()
    return f'{parts[0]}'


def fio_2(name):
    parts = name.split()
    return f' {parts[1][0]}.{parts[2][0]}.'


def fio_3(name): 
    parts = name.split()
    return f'{parts[1]} {parts[2]}'


# удалям файлы c расширениями
def del_file_on_extenshion():
    extensions = (".aux", ".out", ".bbl", ".bcf", ".blg", ".log", ".pytxcode", ".xml", ".synctex.gz")
# пройдемся по всем файлам в текущей директории и удаляем все файлы с нужными расширениями
    for file in os.listdir("."):
        for ext in extensions:
            if file.endswith(ext):
                os.remove(file)


dfu = FileExcel('meters.xlsx', 'Sheet1')   # в таблицу pandas читает файл реестра из таблицы Google

# Печать заголовков  файла  данных

# print(dfu.columns.tolist())


# Объединяем data frame
# merged = pd.merge(df1, df2, on='номер счетчика')


#  Выборка по немеру участка (1. Делаем номер участка индексом  2. По индексу выбираем данные из датафрейм. 3. Выводим н печать)
homesteads = [88]
#  Номера участков или список номеров

dfu.set_index('Дом', inplace=True)

for homestead in homesteads:
    card = dfu.loc[homestead]
# card.to_csv(r"Карточка участка  " + str(homestead) + ".csv", sep=';', index=True, header=False)
    Name = card['ФИО']   # с 0 по 3
    Fio = fio(Name)
# fio_hoo = maker.make(NamePart.LASTNAME, Gender.MALE, Case.GENITIVE, fio_1(Name)) + fio_2(Name)
    fio_hoo = maker.make(NamePart.LASTNAME, Gender.MALE, Case.ACCUSATIVE, fio_1(Name)) + fio_2(Name)
    fio_this = maker.make(NamePart.LASTNAME, Gender.MALE, Case.DATIVE, fio_1(Name)) + fio_2(Name)
    Street = card['Улица']
    Schetchik = card['Связной адрес']
    Licshet = card['Лиц.счёт']
    Namber = homestead
    print(f" Улица {Street}, участок {Namber}, Владелец {Name}, {Fio}, {str(Schetchik)}, {str(Licshet)}, {fio_hoo, fio_this}")
    fin = open("template.tex", "rt", encoding='Utf-8')
    fout = open('data' + str(homestead) + '.tex', "wt", encoding='utf-8')
    data = fin.read()
    data = data.replace('NAME', Name)
    data = data.replace('FIO', Fio)
    data = data.replace('FGENITIVE', fio_hoo)
    data = data.replace('FDATIVE', fio_this)
    data = data.replace('STREET', Street)
    data = data.replace('LAND_PLOT', str(homestead))
    data = data.replace('SCHETCHIK', str(Schetchik))
    data = data.replace('LICSHET', str(Licshet))
    # создание новой папки
    new_folder = "Участок  " + str(homestead) + " ограничение электроэнергии"
    # Создаем новую папку по имени участка
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    fin.close()
    data_tex = data
    fout.write(data_tex)
    fout.close()
    with open('start' + str(homestead) + '.tex', 'w', encoding='utf-8') as file:
        file.write('%% !TEX TS-program = xelatex\n')
        file.write('\\input{preamble}\n')
        file.write('\\input{data' + str(homestead) + '}\n')
        file.write('\\begin{document}\n')
        file.write('\\thispagestyle{empty}\n')
        file.write('\\input{pereopr}\n')
        file.write('\\input{program_py}\n')
        file.write('\\input{Заявка_в_Краснодарэнерго}\n')
        file.write('\\pagebreak\n')
        file.write('\\input{Уведомение_члену}\n')
        file.write('\\pagebreak\n')
        file.write('\\input{Уведомление_ТНС}\n')
        file.write('\\end{document}\n')

# shutil.copy(str('start' + str(homestead) + '.tex'), str(new_folder))
#  shutil.copy(str('data' + str(homestead) + '.tex'), str(new_folder))
# shutil.move('start' + str(homestead) + '.tex', str(new_folder))
# shutil.move(str('data' + str(homestead) + '.tex'), str(new_folder))


del_file_on_extenshion()
