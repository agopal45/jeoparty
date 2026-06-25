input_file = "Questions/RedditSource/JEOPARDY_QUESTIONS1.json"

file_obj = open(input_file, mode='r')
content = file_obj.read()
file_obj.close()
print(file_obj.closed)
modified = content.replace(",", ",\n")
output2 = open("Questions/RedditSource/output2.json", mode='w')
output2.write(modified)

