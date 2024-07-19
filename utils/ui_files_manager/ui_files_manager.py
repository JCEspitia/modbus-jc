import subprocess
import sys

from ui_dict import UI_DICT


def create_pyui_file(ui_file, py_file):
    command = ['pyuic6', ui_file, '-o', py_file]

    try:
        subprocess.run(command, check=True)
        print(f'File {ui_file} converted to {py_file}')
    except subprocess.CalledProcessError as e:
        print(f'Error to execute pyuic6: {e}')


def manage_ui_files(file=None):
    if file is None:
        # Convert all files
        for ui in UI_DICT.values():
            path = ui.get('path')
            ui_file = path + ui.get('ui_file')
            py_file = path + ui.get('py_file')

            create_pyui_file(ui_file, py_file)
    else:
        # Convert specific file
        ui = UI_DICT.get(file)
        path = ui.get('path')
        ui_file = path + ui.get('ui_file')
        py_file = path + ui.get('py_file')

        create_pyui_file(ui_file, py_file)


if __name__ == '__main__':
    specific_file = sys.argv[1] if len(sys.argv) > 1 else None
    manage_ui_files(specific_file)
