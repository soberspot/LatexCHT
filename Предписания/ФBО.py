username = "Фамилия Имя Отчество"

usernamelist = username.split(' ')
print(f'{usernamelist[0]}  {usernamelist[1][0:1]}. {usernamelist[2][0:1]}.')


def fio(name):
    parts = name.split()
    return f'{parts[0]} {parts[1][0]}.{parts[2][0]}.'

def text_fio(text):
    return ', '.join(map(fio, map(str.strip, text.split(','))))

print(fio('Жуковский Иван Петрович'))
print(text_fio('Сидоров Николай Петрович, Петрова Марина Николаевна'))