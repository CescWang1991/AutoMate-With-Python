import subprocess

calcProc = subprocess.Popen('C:\\Windows\\System32\\calc.exe')
print(calcProc.poll())
calcProc.wait()
print(calcProc.poll())

fileObj = open('hello.txt', 'w')
fileObj.write('Hello world!')
fileObj.close()
subprocess.Popen(['start', 'hello.txt'], shell=True)
