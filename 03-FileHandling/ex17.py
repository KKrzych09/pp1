import re
tekst = "To be, or not to be, that is the question"
print(len(re.findall("[aeiouy]", tekst)))