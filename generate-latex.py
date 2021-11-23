import os

import pandas as pd


def main():
    #fname = 'Wedding Invitation List - 12_12_2021 - Sheet1.csv'
    fname = 'updates.csv'
    df = pd.read_csv(fname)
    template = open('ticket-template.jinja2').read()
    name_splits = [name.split() for name in df['Name']]
    latex_lines = []
    for name_tuple in name_splits:
        latex_lines.append(r'\confpin{}{}')
        latex_lines.append(r'\confpin{}{}')
        latex_lines.append(r'\confpin{}{}')
        match name_tuple:
            case (first_name, last_name):
                latex_lines.append(r'\confpin{' + first_name + '}{' + last_name + '}')
            case (first_name,):
                latex_lines.append(r'\confpin{' + first_name + '}{}')
        latex_lines.append(r'\newpage\ticketreset')
    open('ticket-latex.tex', 'w+').write(template.replace('latex_lines', "\n".join(latex_lines)))
    os.system('latexmk -pdf')


if __name__ == "__main__":
    main()