import re

print("Extracting Emails using Regular Expressions\n")

given_text = "Contact us at support@example.com or at helpdesk@mysite.org."

pattern = r"[\w.+-]+@[\w-]+\.[\w.-]+"

print(re.findall(pattern,given_text))