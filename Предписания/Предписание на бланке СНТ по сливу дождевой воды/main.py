import os

with open('main.tex', 'w', encoding="utf-8") as f:
    f.write('%% !TEX TS-program = xelatex\n')
    f.write('\\input{preamble}\n')
    f.write('\\begin{document}\n')
    f.write('\\thispagestyle{empty}\n')
    f.write('\\input{pereopr}\n')
    f.write('\\input{../data}\n')
    f.write('\\input{бланкСНТ}\n')
    f.write('\\input{заголовок}\n')
    f.write('\\input{текст обращения}\n')
    f.write('\\end{document}')

    # os.system("xelatex.exe  -shell-escape  -synctex=1 -interaction=nonstopmode main.tex")
    # os.system("pythontex main.tex")
    # os.system("xelatex.exe  -shell-escape  -synctex=1 -interaction=nonstopmode main.tex")