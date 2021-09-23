# This is a sample Python script.
import os
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class question(object):
    def __init__(self,body,answer):
        self.body = body
        self.answer = answer

def parse(text):
    path = text
    with open(text,"r", encoding='utf-8') as file:
        content = file.readlines()
    return content

def split(content):
    questionlist = []
    for line in content:
        hasi = False
        for i in range(len(line)):
            if line[i]=="?" or line[i]=="？":
                index = i
                hasi = True
        if hasi == True:
            body = line[:index+1]
            answer = line[index+1:]
            questionlist.append(question(body,answer))
    return questionlist
def main():
    content = parse("tk.txt")
    questionlist = split(content)
    for question in questionlist:
        print(question.__dict__)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

