import threading, time
print('Start of program.')

def takeANap():
    time.sleep(2)
    print('Wake up!')

def takeAParam(str):
    time.sleep(5)
    print(str)

threadObj = threading.Thread(target=takeANap)
threadObj.start()

threadParam = threading.Thread(target=takeAParam, args=['NiHao'])
threadParam.start()

print('End of program.')
