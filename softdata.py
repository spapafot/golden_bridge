import requests

SERIAL_NUMBER = "01104263844820"
URL = f"http://{SERIAL_NUMBER}.oncloud.gr/s1services"
login_params = {
  "service": "login",
  "username": "",
  "password": "",
  "appId": "",
}

login_response = requests.get(url=URL, params=login_params).text

auth_params = {
    "service": "authenticate",
    "clientID": "",
    "COMPANY": "",
    "BRANCH": "",
    "MODULE": "",
    "REFID": ""
}

get_params = {
    "service": "getData",
    "clientID": "",
    "appId": "",
    "OBJECT": "CUSTOMER",
    "FORM": "",
    "KEY": "",
    "LOCATEINFO": "CUSTOMER:CODE,NAME,AFM;CUSEXTRA:VARCHAR02,DATE01"
}

set_params = {
    "service": "setData",
    "clientID": "",
    "appId": "",
    "OBJECT": "CUSTOMER",
    "KEY": "47",
    "data": {
        "CUSTOMER": [
            {
                "CODE": "100",
                "NAME": "Soft One Technologies S.A.",
                "AFM": "999863881",
                "IRSDATA": "IV Athens",
                "EMAIL": "johng@softone.gr",
                "WEBPAGE": "www.softone.gr",
                "PHONE01": "+302109484797",
                "PHONE02": "+302108889999",
                "FAX": "9484094",
                "ADDRESS": "6 Poseidonos street",
                "ZIP": "17674",
                "DISTRICT": "Kallithea",
                "DISCOUNT": 10,
                "REMARKS": "Hello World!"
            }
        ],
        "CUSEXTRA": [
            {
                "VARCHAR01": "Extra 1",
                "VARCHAR02": "Extra 2"
            }
        ]
    }
}