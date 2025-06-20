from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from pathlib import Path
import glob
import os
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

navegador.get("https://nuvem.connectuse.com.br/apps/f?p=1025:LOGIN:10263782467675:::::")

#nome login
navegador.find_element('xpath', 
                       '//*[@id="P101_USERNAME"]').send_keys("Insira o usuário aqui")
#senha
navegador.find_element('xpath', 
                      '//*[@id="P101_PASSWORD"]').send_keys("Insira a senha aqui")
#botao de entrar
navegador.find_element('xpath', 
                      '//*[@id="B308836535372843204"]').click()

time.sleep(5)

#coordenadas da loja
x = 643
y = 327

pyautogui.moveTo(x, y)

time.sleep(1)

pyautogui.click()

time.sleep(2)

#compras e recebimentos
navegador.find_element('xpath', 
                       '//*[@id="R_PRODUTOS_Cards"]/div/div[3]/ul/li[6]/div/a').click()

#nova aba
time.sleep(5)

newURl = navegador.window_handles[1]

navegador.switch_to.window(newURl)

#recebimento
navegador.find_element('xpath', 
                       '//*[@id="R13384465127013883265"]/tbody/tr[3]/td/table/tbody/tr/td[4]/a[1]/img').click()

#nf-e notas fiscais recebidas
navegador.find_element('xpath', 
                       '//*[@id="R5296982125561203371"]/tbody/tr[3]/td/div/a[1]').click()

#editacao
navegador.find_element('xpath', 
                       '//*[@id="5447839162135116988"]/tbody/tr[2]/td[1]/a/button').click()

#MALUQUICE
for i in range(2, 51):
    #associar produto
    xpath_clicar = '//*[@id="5693146171802114035"]/tbody/tr[{}]/td[22]/a'.format(i)
    navegador.find_element('xpath', xpath_clicar).click()

    time.sleep(2)

    # criar novo produto
    x = 812
    y = 342

    # Move o mouse para as coordenadas desejadas
    pyautogui.moveTo(x, y)

    # Aguarda um breve momento (opcional)
    time.sleep(1)

    # Simula um clique na posição atual do mouse
    pyautogui.click()

    time.sleep(4)

    newURl = navegador.window_handles[2]

    navegador.switch_to.window(newURl)
    
    #unidade
    #navegador.find_element('xpath', 
                           #'//*[@id="P4_UCOM"]').send_keys("u")

    #categoria
    navegador.find_element('xpath', 
                           '//*[@id="P4_IDCATEGORIA"]').send_keys("a")

    #familia
    navegador.find_element('xpath', 
                           '//*[@id="P4_IDFAMILIA"]').send_keys("pro")

    #produto e vendido
    navegador.find_element('xpath', 
                           '//*[@id="P4_AOVENDA"]/div/label').click()

    #produto e comprado
    navegador.find_element('xpath', 
                           '//*[@id="P4_AOCOMPRA"]/div/label').click()

    #gravar
    navegador.find_element('xpath', 
                           '//*[@id="CREATE"]').click()

    #copiar texto
    navegador.find_element('xpath', 
                           '//*[@id="P4_XPROD"]').click()

    #encontra e copia o texto
    elemento_input = navegador.find_element('xpath', '//*[@id="P4_XPROD"]')
    elemento_input.send_keys(Keys.CONTROL, 'a')
    elemento_input.send_keys(Keys.CONTROL, 'c')

    #voltando para a segunda aba
    navegador.close()

    newURl = navegador.window_handles[1]

    navegador.switch_to.window(newURl)

    #control v
    x = 592
    y = 480

    #Move o mouse para clicar e control v
    pyautogui.moveTo(x, y)

    time.sleep(1)

    pyautogui.click()

    pyautogui.hotkey('ctrl', 'v')

    pyautogui.press('enter')

    #associar
    x = 760
    y = 585
    pyautogui.moveTo(x, y)

    time.sleep(1)

    pyautogui.click()
    time.sleep(3)
