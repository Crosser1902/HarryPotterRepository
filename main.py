# This is a sample Python script.
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class question(object):
    def __init__(self,body,answer):
        self.body = body
        self.answer = answer

def typein(qlist):
    chrome_options = webdriver.ChromeOptions()
    # 使用headless无界面浏览器模式
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    # 启动浏览器，获取网页源代码
    # browser = webdriver.Chrome(chrome_options=chrome_options)
    browser = webdriver.Chrome()
    browser.implicitly_wait(30)
    mainUrl = "https://hpq.azurewebsites.net/wp-admin/post-new.php?post_type=fca_qc_quiz"
    browser.get(mainUrl)
    browser.find_element_by_id("user_login").send_keys("cyz1902")
    browser.find_element_by_id("user_pass").send_keys("cyz131519")
    browser.find_element_by_id("wp-submit").click()
    # print(f"browser text = {browser.page_source}")
    index = 0
    time.sleep(10)
    for question in qlist:
        browser.find_elements_by_xpath("//textarea[@placeholder='例如 猫会飞吗？']")[index].send_keys(question.body)
        browser.find_elements_by_xpath("//textarea[@placeholder='例如 没有']")[index].send_keys(question.answer)
        browser.find_element_by_id("fca_qc_add_question_btn").click()
        index = index+1
    # browser.quit()
    browser.find_element_by_id("fca_qc_submit_button").click()

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
    typein(questionlist)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

