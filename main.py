# Chcek version --> pip -V
# download lib Request --> pip install requests
# download lib PrettyTable --> pip install PrettyTable || pip3 install PrettyTable

import requests

req = requests.get('https://tutsplus.com/')
req.encoding  # returns 'utf-8'
status = req.status_code  # returns 200

# print(status)

# req.elapsed  # returns datetime.timedelta(0, 1, 666890)
req.url  # returns 'https://tutsplus.com/'
req.history
print(req.url)


# r = requests.get('https://api.github.com/events')
# # r.text
# print(r.json())