from requests import put, get

ret put(
    'http://localhost:5000/todo1',
    data={'data': 'Remember the milk please'}
    )
print("PUT(todo1): {}".format(re.json()))

ret = get('http://localhost:5000/todo1')
print("GET(todo1): {}".format(re.json()))

ret put(
    'http://localhost:5000/todo2',
    data={'data': 'Change my brakepads please'}
    )
print("PUT(todo2): {}".format(re.json()))

ret = get('http://localhost:5000/todo2')
print("GET(todo2): {}".format(re.json()))