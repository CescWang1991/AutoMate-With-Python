stringData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'

import json
jsonDataAsPythonValue = json.loads(stringData)
print(jsonDataAsPythonValue)
stringOfJsonData = json.dumps(jsonDataAsPythonValue)
print(stringOfJsonData)
