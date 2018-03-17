import requests

res = requests.get('https://www.youtube.com/watch?v=xRAZq1I7wYg')
try:
    res.raise_for_status()
    print(type(res))
    print(res.status_code)
    print(len(res.text))
    playFile = open('Youtube.html', 'wb')
    for chunk in res.iter_content(200000):
        playFile.write(chunk)
    playFile.close()
except Exception as exc:
    print('There was a problem: %s' % (exc))
