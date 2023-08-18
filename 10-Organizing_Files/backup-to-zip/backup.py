#!/usr/bin/env python3

'''
backup.py
Backing Up a Folder into a ZIP File
'''

import argparse
import shutil
import zipfile
from pathlib import Path


def get_parser():
    parser = argparse.ArgumentParser(
        description='Back Up a folder into a ZIP file')
    parser.add_argument('path')
    return parser


def is_archive(path, arc_format='zip'):
    return Path.is_file(path) and path.suffix == f'.{arc_format}'


def get_archive_number(path):
    stem = path.stem
    return stem.split('-')[-1]


def get_archive_base_stem(path):
    stem = path.stem
    return stem[:stem.rfind('-')]


def get_last_archive_number(name, arc_format='zip'):
    archives = filter(lambda path: is_archive(path, arc_format),
                      Path.iterdir(Path.cwd()))
    name_relevant_archives = \
        filter(lambda path: get_archive_base_stem(path) == name, archives)
    name_relevant_archives_numbers = list(map(
        get_archive_number, name_relevant_archives))

    if name_relevant_archives_numbers:
        return int(max(name_relevant_archives_numbers))
    return 0


def get_new_archive_name(name, arc_format='zip'):
    last_archive_number = get_last_archive_number(name)

    new_archive_number = last_archive_number + 1
    return f'{name}-{new_archive_number}.{arc_format}'


def get_full_dir_path(filename):
    file_path = Path(filename)
    if Path.is_absolute(file_path):
        return file_path
    return Path.cwd() / filename


def zip_path(path):
    path_name = path.name
    print(path_name)

    new_name = get_new_archive_name(path_name)
    print(new_name)

    new_zip = zipfile.ZipFile(new_name, 'w')
    if Path.is_file(path):
        new_zip.write(path_name, compress_type=zipfile.ZIP_DEFLATED)
    else:
        print('DIRECTORY!')
    new_zip.close()


def main():
    parser = get_parser()
    path_name = parser.parse_args().path

    path = get_full_dir_path(path_name)

    if not Path.exists(path):
        print(f'Error: {path_name} does not exist')
        exit(2)

    zip_path(path)


if __name__ == '__main__':
    main()
