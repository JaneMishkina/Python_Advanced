"""Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки."""
import pathlib
from pathlib import Path
import os


def sort_files_by_ext(path=None):
    if not path:
        path = Path().cwd()
    path = Path(path)
    files = Path(path).iterdir()
    os.chdir(path)

    for file in files:
        print(file.is_file(), Path(file.suffix) not in Path().iterdir())
        if (file.is_file()
                and Path(file.suffix) not in Path().iterdir()):
            os.mkdir(file.suffix)

        if file.is_file() and file.suffix != ".py":
            file.replace(f"{file.suffix}\\{file.name}")

#2 вариант
def sort_files():
    curr_path = pathlib.Path(os.getcwd())
    for file in curr_path.iterdir():
        if file.suffix == '.py':
            continue
        try:
            file.replace(f'{file.suffix}/{file.name}')
        except FileNotFoundError:
            os.mkdir(file.suffix)
            file.replace(f'{file.suffix}/{file.name}')

if __name__ == '__main__':
    sort_files()
