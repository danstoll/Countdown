def convert_icon_to_py(icon_path, output_path):
    with open(icon_path, 'rb') as icon_file:
        content = icon_file.read()
        with open(output_path, 'w') as output_file:
            output_file.write('icon_data = ' + str(list(content)))

convert_icon_to_py('timer_app.ico', 'timer_app.py')
