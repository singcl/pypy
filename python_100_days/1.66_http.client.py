import http.client
conn  = http.client.HTTPSConnection('imcoco.top')
# conn.request('GET', '/')
conn.request('GET', '/home')
r1 = conn.getresponse()
data = r1.read()
print(r1.status, r1.reason)
print(data)
conn.close()
