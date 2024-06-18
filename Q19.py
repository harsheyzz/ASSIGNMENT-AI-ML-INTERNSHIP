punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

string = "hey!!.. can i join you??"

empty_str = ""
for i in string:
   if i not in punctuations:
       empty_str  = empty_str  + i

print(empty_str )