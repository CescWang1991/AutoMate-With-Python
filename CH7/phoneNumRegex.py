import re

phoneNumRegexNoGroup = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')    #has no groups
phoneNumRegexGroup = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')   #has groups
ng = phoneNumRegexNoGroup.findall('Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.')
hg = phoneNumRegexGroup.findall('Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.')
print(ng)
print(hg)
