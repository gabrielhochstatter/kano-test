def save_to_file(filename, email, name, message):
    file = open(filename, 'a')

    formatted_string = f'\n{name} ({email}) sent: {message}'

    file.write(formatted_string)
    file.close()
