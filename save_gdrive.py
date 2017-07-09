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
    flow = client.flow_from_clientsecrets('client_secret_drive.json', SCOPES)
    creds = tools.run_flow(flow, store, flags) \
            if flags else tools.run(flow, store)

DRIVE = build('drive', 'v2', http=creds.authorize(Http()))

FILES = (
    ('hello.txt', False),
)

for filename, convert in FILES:
    metadata = {'title': filename,
                "parents": [{"id": bill.dir_id}],
                }
    #image_path = os.path.join(cap_dir, filename)
    res = DRIVE.files().insert(body=metadata, media_body=filename).execute()
    print(res['id'])
    if res:
        print('Uploaded "%s" (%s)' % (filename, res['mimeType']))
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
