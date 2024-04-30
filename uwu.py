after_empty_line: bool = False
packages: list[str] = []

with open('requirements.txt', 'r') as file:
    for line in file.readlines():
        if after_empty_line:
            packages.append(line.removesuffix('\n').split('==')[0])

        if line.removesuffix('\n') == 'EMPTY':
            after_empty_line = True

print(f'python -m pip install {" ".join(packages)}')
