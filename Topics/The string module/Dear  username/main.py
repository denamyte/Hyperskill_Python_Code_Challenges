from string import Template

t = Template('Dear $username! It was really nice to meet you. Hopefully, you have a nice day! See you soon, $username!')
print(t.substitute(username=input()))
