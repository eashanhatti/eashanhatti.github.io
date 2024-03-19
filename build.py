import os

for path, _, files in os.walk('.'):
    top = '.\\'
    for _ in range(path.count('\\')):
        top += '..\\'
    for file in files:
        if '.html' in file:
            os.system(f'rm {path}\\{file}')
        elif f'.md' in file:
            name, _ = os.path.splitext(file)
            if 'DRAFT' in name: continue
            os.system(f'pandoc {path}\\{name}.md -s --css {top}\\style.css --mathjax -o {path}\\{name}.html')