import urllib.request


user = 'pythono'
message = 'Hello World!'
r = request.post("http://akipress.org", data={'user': user, 'massage': massage})
