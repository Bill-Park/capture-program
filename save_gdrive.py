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


def upload2drive(file_title) :
    file_path = None
    file_name = None

    if '/' in file_title :
        file_path = file_title
        file_name = file_title.split('/')[-1]
        print(file_name)
    else :
        if isinstance(file_title, str) :
            file_name = file_title
            file_path = os.path.join(bill.cap_dir, file_title)

    print(file_path)

    metadata = {'name': file_name,
                'parents': [bill.dir_id],
                'mimeType': None
                }
    '''
    https: // drive.google.com / file / d / 0
    B_CtpwiAk5hIbkdfWmJvNUdabk0 / view?usp = sharing
    https: // drive.google.com / file / d / 0
    B_CtpwiAk5hIT1dQMVhxYnE0YTg / view?usp = sharing

    https: // drive.google.com / file / d / 0
    B_CtpwiAk5hIczc1Rk1SN3NhUzQ / view?usp = sharing
    https: // drive.google.com / file / d / 0
    B_CtpwiAk5hIOW91akpLUEEzc2M / view?usp = sharing
    '''
    res = DRIVE.files().create(body=metadata, media_body=file_path).execute()
    if res:
        print('Uploaded "%s" (%s)' % (file_name, res['mimeType']))

    return res['id']

def name2id(folder_name) :
    query = "mimeType='application/vnd.google-apps.folder'"
    response = DRIVE.files().list(q=query,
                                  spaces='drive',
                                  fields='nextPageToken, files(id, name)').execute()

    for exist_folder in response.get('files', []) :
        # Process change
        print('Found file: %s (%s)' % (exist_folder.get('name'), exist_folder.get('id')))
        if exist_folder.get('name') == folder_name :
            return exist_folder.get('id')

    make_folder_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }

    maked_folder = DRIVE.files().create(body=make_folder_metadata,
                                fields='id').execute()

    return maked_folder

    #query = "mimeType != 'application/vnd.google-apps.folder' and trashed = false and ('user1@test.org' in readers or 'group1@test.org' in readers) and fullText contains 'example string'"
    #puts
    #drive.list_files(q: query)mimeType='application/vnd.google-apps.folder'
    '''
    query = "mimeType='application/vnd.google-apps.folder'"
    response = DRIVE.files().list(q=query).execute()
    print(response)
    for file in response.get('files', []):
        # Process change
        print ('Found file: %s (%s)' % (file.get('name'), file.get('mimeType')))
    '''

    #page_token = response.get('nextPageToken', None)
    #print(page_token)





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
