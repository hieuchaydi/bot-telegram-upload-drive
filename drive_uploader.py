import os
import requests
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from io import BytesIO
from datetime import datetime

SCOPES = ['https://www.googleapis.com/auth/drive']
TOKEN_FILE = 'token.json'

def authenticate():
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_console()
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
    return creds

def get_or_create_folder(service, name):
    query = f"name='{name}' and mimeType='application/vnd.google-apps.folder'"
    results = service.files().list(q=query, spaces='drive', fields='files(id)').execute()
    items = results.get('files', [])
    if items:
        return items[0]['id']
    file_metadata = {'name': name, 'mimeType': 'application/vnd.google-apps.folder'}
    folder = service.files().create(body=file_metadata, fields='id').execute()
    return folder.get('id')

def save_image_to_drive(file_url, filename):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    folder_name = datetime.now().strftime("%Y-%m-%d")
    folder_id = get_or_create_folder(service, folder_name)

    response = requests.get(file_url)
    file_data = BytesIO(response.content)

    file_metadata = {'name': filename, 'parents': [folder_id]}
    media = MediaIoBaseUpload(file_data, mimetype='image/jpeg')

    uploaded_file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

    service.permissions().create(fileId=uploaded_file['id'], body={'type': 'anyone', 'role': 'reader'}).execute()

    return f"https://drive.google.com/file/d/{uploaded_file['id']}/view"

def save_video_to_drive(file_url, filename):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    folder_name = datetime.now().strftime("%Y-%m-%d")
    folder_id = get_or_create_folder(service, folder_name)

    response = requests.get(file_url)
    file_data = BytesIO(response.content)

    file_metadata = {'name': filename, 'parents': [folder_id]}
    media = MediaIoBaseUpload(file_data, mimetype='video/mp4')

    uploaded_file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

    service.permissions().create(fileId=uploaded_file['id'], body={'type': 'anyone', 'role': 'reader'}).execute()

    return f"https://drive.google.com/file/d/{uploaded_file['id']}/view"