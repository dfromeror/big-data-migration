""" from pydrive.auth import GoogleAuth

from pydrive.drive import GoogleDrive

#from google.colab import auth

from oauth2client.client import GoogleCredentials



gauth = GoogleAuth()

gauth.credentials = GoogleCredentials.get_application_default() """

from pydrive.drive import GoogleDrive


drive = GoogleDrive()


fileDownloaded = drive.CreateFile({'id':'1CHWAh4KQ3Mq9AJdY6a9mTSIn7HjYUtEY'})

fileDownloaded.GetContentFile('example.csv')

import pandas as pd

df = pd.read_csv('example.csv', delimiter=',' )

df.head()