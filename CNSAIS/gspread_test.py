from oauth2client.service_account import ServiceAccountCredentials
import gspread

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'cnsais-example-15b64aed76d8.json', scope)
gc = gspread.authorize(credentials)
gc1 = gc.open("gspread-test").worksheet('시트1')
gc2 = gc1.get_all_values()
print(gc2)
gc1.update_acell('B1', 'b1 updated')
