from selenium import webdriver
import time
import os

os.system("pip install selenium")

usr_username = input("Username : ")
usr_password = input("Password : ")

url = "https://www.instagram.com/"

browser = webdriver.Firefox()
browser.get(url)
time.sleep(2)

username = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
password = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
giris = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')


username.send_keys(usr_username)
time.sleep(1)
password.send_keys(usr_password)
time.sleep(1)
giris.click()
time.sleep(3)
bilgi_kayıt = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
bilgi_kayıt.click()

