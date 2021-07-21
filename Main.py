import os
import sys
import requests


url = "https://primerose.xyz/register"

data = {
'_token': 'TTasay95nGjLIRl4mBeo5EXOwBnfFTy2PCdbpnC6',
'name': 'DuEnAbee',
'surname': 'DuEnAbe',
'birthday': '1989-11-11',
'email': 'DuEnAbe@yahoo.com',
'password': 'DuEnAbe',
'password_confirmation': 'DuEnAbe',
}
while True:
    SocialRP_Snegle_Security = requests.post(url, data=data).text
    print(SocialRP_Snegle_Security)
    print("Succesfully Created an Account")
