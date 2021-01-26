import re
import os

text = open("./test_text.txt","r").read()

# text = re.sub(r"- ","-",text)
# text = re.sub(r"-(\r|\n)","",text)
# # text = re.sub(r"-\n","",text)
# text = re.sub(r"[-]{2,}"," ",text)
# # tokens = re.findall(r"(?![\w.-]+@[\w.-]+.[a-z]+)([a-z0-9\w-]+)", text.lower())
# tokens = re.findall(r"(?!\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b | [a-z0-9\w-]+))", text.lower())
# # (?(2)\w+@\w+\.[a-z]+|.+))

# # [a-z0-9_]@[a-z0-9_].[a-z] 

for i,y,z in os.walk("../../"):
    print(i,y,z)

# print(tokens)