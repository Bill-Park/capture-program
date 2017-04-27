import os

def copytoclipboard(text) :
    command_copy = 'echo ' + text.strip() + ' | clip'
    os.system(command_copy)
    print(command_copy)

cap_dir = os.path.join('f:\\', 'blogging', 'capture')
dir_id = '0B_CtpwiAk5hIWm9BXzVGU21yWEU'

print(os.listdir(cap_dir))

for image in os.listdir(cap_dir) :
    image_dir = os.path.join(cap_dir, image)
    command_str = 'gdrive upload ' + image_dir + ' --share -p ' + dir_id
    print(command_str)
    system_echo = os.popen(command_str).read()
    image_id = system_echo.split()[3]
    base_url = 'https://drive.google.com/uc?id=' + image_id.strip()
    copytoclipboard(base_url)
    os.remove(image_dir)

print('end')