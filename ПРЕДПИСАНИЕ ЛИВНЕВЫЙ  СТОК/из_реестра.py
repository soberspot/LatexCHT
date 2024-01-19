import argparse
import datetime
from pathlib import Path
from numpy import nan
import pandas as pd
import re
import os
#
date_string = datetime.datetime.now().strftime('%Y-%m-%d')
parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("--name", default=None, type=str, help="Your name")


def FileExcel(file, list):     # читает файл excel
    src_file = Path.cwd() / file
    df = pd.read_excel(src_file, sheet_name=list, header=0, usecols='A:Z')
    return df


def _split_fio(df, strc):    # из полного ФИО собственника оставляет имя и отчество
    df[strc] = df[strc].str.split().str[1] + " " + df[strc].str.split().str[2]
    return (df[strc])


# Рекурсивная функция для удаления директории даже если она не пустая
def delete_directory(dir):
    for root, dirs, files in os.walk(dir, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)
        for directory in dirs:
            dir_path = os.path.join(root, directory)
            delete_directory(dir_path)
            os.rmdir(dir_path)


 # удалям файлы из расширений
def del_file_on_extenshion():
    extensions = (".aux", ".out", ".bbl", ".bcf", ".blg",  ".log", ".pytxcode", ".xml", ".synctex.gz")
# пройдемся по всем файлам в текущей директории и удаляем все файлы с нужными расширениями
    for file in os.listdir("."):
        for ext in extensions:
            if file.endswith(ext):
                os.remove(file)


dfu = FileExcel('РЕЕСТР СНТ ЮГТЕКС   2020.xlsx', 'Реестр')   # в таблицу pandas читает файл реестра из таблицы Google

# Печать заголовков  файла  данных

# print(dfu.columns.tolist())

#  Выборка по немеру участка (1. Делаем номер участка индексом  2. По индексу выбираем данные из датафрейм. 3. Выводим н печать)


homesteads = [590]                                #  Вишневая

dfu.set_index('Номер участка', inplace=True)

for homestead in homesteads:
    card = dfu.loc[homestead]
    # card.to_csv(r"Карточка участка  " + str(homestead) + ".csv", sep=';', index=True, header=False)
    Name = card['ФИО собственника']   # с 0 по 3
    Street = card['Улица']
    Namber = homestead
    print(Street, Namber, Name)
    fin = open("template.tex", "rt", encoding='Utf-8')
    fout = open('data' + str(homestead) + '.tex', "wt", encoding='utf-8')
    data = fin.read()
    data = data.replace('NAME', Name)
    data = data.replace('STREET', Street)
    data = data.replace('LAND_PLOT', str(homestead))
    fin.close()
    data_tex = data
    fout.write(data_tex)
    fout.close()
    with open('предписание' + str(homestead) + '.tex', 'w', encoding='utf-8') as file:
        file.write('%% !TEX TS-program = xelatex\n')
        file.write('\\input{preamble}\n')
        file.write('\\input{data' + str(homestead) + '}\n')
        file.write('\\begin{document}\n')
        file.write('\\thispagestyle{empty}\n')
        file.write('\\input{pereopr}\n')
        file.write('\\input{program_py}\n')
        file.write('\\input{заголовок}\n')
        file.write('\\input{текст предписания}\n')
        file.write('\\input{подпись}\n')
        file.write('\\end{document}\n')


del_file_on_extenshion()

# Удаляем директории, содержащие в названии "pythontex-files-"
dir_name_contains = "pythontex-files-предписание"
for root, dirs, files in os.walk('.', topdown=True):
    for dir in dirs:
        if dir_name_contains in dir:
            delete_directory(dir)


# Проходим циклом по списку и удаляем директории, содержащие "pythontex-files-"
for dir in dirs:
    # Проверка, является ли элемент директорией и содержит ли он "pythontex-files-"
    if os.path.isdir(dir) and "pythontex-files-предписание" in dir:
        try:
            os.rmdir(dir)
            print(f"Директория {dir} удалена успешно")
        except OSError as e:
            print(f"Ошибка удаления директории {dir}: {e}")