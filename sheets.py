import csv
import os

import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


def get_service_sacc():

    # Авторизация в Google Sheets
    creds_json = os.path.dirname(__file__) + "/creds.json"
    scopes = ['https://www.googleapis.com/auth/spreadsheets']

    creds_service = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes).authorize(httplib2.Http())
    return build('sheets', 'v4', http=creds_service)

def get_data_from_google_sheets(sheet_id, ranges):
    service = get_service_sacc()
    sheet = service.spreadsheets()


    resp = sheet.values().batchGet(spreadsheetId=sheet_id, ranges=ranges).execute()
    print(resp)

    # Загрузка данных из Google Sheets в файл
    # with open("data.csv", "w", newline='', encoding='utf-8') as f:
    #     datawriter = csv.writer(f, delimiter=',')
    #     datawriter.writerows(resp["valueRanges"][0]["values"])


    print("Загрузка данных из Google Sheets завершена")

if __name__ == '__main__':
    sheet_id = "1E3w-YesqOOyxti2tN-DL-0VWbyas0aHzLzjKgh-JN-A"
    ranges = ["УрокиДетали"]
    get_data_from_google_sheets(sheet_id, ranges)
