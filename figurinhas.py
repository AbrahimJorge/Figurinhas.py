from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui

#PATH para abrir o chromedriver.exe que ta a pasta
PATH = "C:\Teste\chromedriver.exe" 
#Tem quer o chrome driver da mesma versão do seu Chrome
driver = webdriver.Chrome(PATH)
#Para abrir o o navegador(Google, Fire Fox, Explorer)
driver.get("https://web.whatsapp.com/")

sleep(20)
element_download = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/div[2]/div/div[1]/p")
element_download.click()
element_download.send_keys('Marco')
pyautogui.press("enter")
sleep(0.5)

element_download = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[1]/div[1]/button[2]/div/span")
sleep(0.5)
element_download.click()
sleep(0.5)
element_download = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[1]/div[1]/button[4]/div/span")
sleep(0.5)
element_download.click()
sleep(15)
while True:
    element_download = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[5]/div/footer/div[2]/div/div[3]/div/div/div[1]/div/div[2]/span/span")
    sleep(0.5)
    element_download.click()
    sleep(0.5)
    element_download = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[5]/div/footer/div[2]/div/div[3]/div/div/div[2]/div[2]/div/div/div/div[2]/div/span/img")
    sleep(0.5)
    element_download.click()
    sleep(0.5)
    """while True:
    element_download = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
    sleep(0.5)
    element_download.click()
    element_download.send_keys('FODE')
    pyautogui.press("enter")
    element_download = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
    sleep(0.5)
    element_download.click()
    element_download.send_keys('ME FODE')
    pyautogui.press("enter")
    element_download = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
    sleep(0.5)
    element_download.click()
    element_download.send_keys('AAAAAAAAAAAAAAAAA')
    pyautogui.press("enter")
    #sleep(1)"""

#CAMINHO
#/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[1]/div[1]/button[2]/div/span
#FIGURINHA
#/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[1]/div[1]/button[4]/div/span
#fAV
#/html/body/div[1]/div/div/div[5]/div/footer/div[2]/div/div[3]/div/div/div[1]/div/div[3]/span/span
#BRANCO
#/html/body/div[1]/div/div/div[5]/div/footer/div[2]/div/div[3]/div/div/div[2]/div[2]/div/div/div/div[35]/div/span/img
