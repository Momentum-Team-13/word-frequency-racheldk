import re
text = "How long, how long must we sing this song? How long?"
# new_text = text.split(" ")
# print(new_text)
# re.search('long', text)
# print(re.search('long', text))

for word in text:
    print(re.search('[owl]', text))
    