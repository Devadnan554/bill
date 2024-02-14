import requests
plate =  input("plate : ")
url =f'http://aladl.adnan-alharbi.com/bills/{plate}.html'


req = requests.get(url)

if req.status_code == 200:
    print(req.content)
else:
    print("not found")