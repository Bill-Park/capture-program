from __future__ import print_function
import os
import bill
import json

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


def delete_file(file_id, isteam = False) :
    
    deleted_file = DRIVE.files().delete(fileId=file_id,
                                        supportsTeamDrives=isteam).execute()
    print(deleted_file)


def make_file_test(file_name) :
    make_folder_metadata = {
        'name': file_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }

    maked_folder = DRIVE.files().create(body=make_folder_metadata).execute()

    print('Make folder: %s (%s)' % (maked_folder.get('name'), maked_folder.get('id')))


def get_file_id(file_title) :
    query = "name contains '{}'".format(file_title)
    response = DRIVE.files().list(q=query,
                                  spaces='drive',
                                  fields='files(id, name)').execute()

    for exist_folder in response.get('files', []):
        # Process change
        if exist_folder.get('name') == file_title :
            print('Found folder: %s (%s)' % (exist_folder.get('name'), exist_folder.get('id')))
            return exist_folder.get('id')


#make_file_test('12345')
while True :
    id = get_file_id('1gb.jpg')
    print(id)
    if id is not None :
        delete_file(id)
    else :
        break