from __future__ import print_function
import os
import bill

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

try :
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/drive.file'
store = file.Storage('storage.json')
creds = store.get()

if not creds or creds.invalid:
    print("make new storage data file ")
    flow = client.flow_from_clientsecrets('client_secret_drive.json', SCOPES)
    creds = tools.run_flow(flow, store, flags) \
            if flags else tools.run(flow, store)

DRIVE = build('drive', 'v3', http=creds.authorize(Http()))

FILES = (
    ('hello.txt', False),
)

def upload2drive(file_title, print_flag = False) :
    file_path = None
    file_name = None
    if '\\' in file_title :
        file_path = file_title
        file_name = file_title.split('\\')[-1]
    else :
        if isinstance(file_title, str) :
            file_name = file_title
            file_path = os.path.join(bill.cap_dir, file_title)
    print(file_path)
    '''
    metadata = {'title': file_title,
                "parents": [{"id": bill.dir_id}],
                }

    res = DRIVE.files().insert(body=metadata, media_body=file_path).execute()
    if res and print_flag :
        print('Uploaded "%s" (%s) id : %s' % (file_path, res['mimeType'], res['id']))
    '''

    metadata = {'name': file_name,
                'parents': [{"id": bill.dir_id}],
                'mimeType': None
                }

    res = DRIVE.files().create(body=metadata, media_body=file_name).execute()
    if res:
        print('Uploaded "%s" (%s)' % (file_name, res['mimeType']))

    return res['id']






'''
if res:
    MIMETYPE = 'application/pdf'
    res, data = DRIVE._http.request(res['exportLinks'][MIMETYPE])
    if data:
        fn = '%s.pdf' % os.path.splitext(filename)[0]
        with open(fn, 'wb') as fh:
            fh.write(data)
        print('Downloaded "%s" (%s)' % (fn, MIMETYPE))
'''

'''
for image in os.listdir(cap_dir) :
    image_dir = os.path.join(cap_dir, image)
    command_str = 'gdrive upload ' + image_dir + ' --share -p ' + dir_id
    print(command_str)
    system_echo = os.popen(command_str).read()
    image_id = system_echo.split()[3]
    base_url = 'https://drive.google.com/uc?id=' + image_id.strip()
    copytoclipboard(base_url)
    os.remove(image_dir)
'''
