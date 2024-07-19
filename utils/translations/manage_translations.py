import subprocess
import sys

from translatable_files_list import TRANSLATABLE_FILES_LIST


def create_translate_file(files: list, locale: str):
    command = ['pylupdate6']
    command += files
    command += ['-ts', f'translations/{locale}.ts', '--verbose']

    try:
        subprocess.run(command, check=True)
        subprocess.run(['lrelease', f'translations/{locale}.ts'], check=True)
        print(f'Translation file created for {locale}')
    except subprocess.CalledProcessError as e:
        print(f'Error to execute pylupdate6: {e}')


def manage_translation_file(locale):
    if locale is not None:
        files = []
        for file in TRANSLATABLE_FILES_LIST:
            files.append(file)

        create_translate_file(files, locale)
    else:
        print("Unspecified locale")


if __name__ == '__main__':
    input_locale = sys.argv[1] if len(sys.argv) > 1 else None
    manage_translation_file(input_locale)
