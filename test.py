import quickstart
import httplib2
from apiclient import discovery
from apiclient import http
from googleapiclient

def drive_api() :
    credentials = quickstart.get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)
    result = service.files().list(pageSize=50).execute()
    items = result.get('files', [])
    for item in items :
        print(item)




file_metadata = { 'name' : 'photo.jpg' }
media = http.MediaFileUpload('files/photo.jpg',
                        mimetype='image/jpeg')
file = drive_service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()
print 'File ID: %s' % file.get('id')

if __name__ == '__main__':
    drive_api()
