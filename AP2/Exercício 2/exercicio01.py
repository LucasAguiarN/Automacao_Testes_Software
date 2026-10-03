import os
from selenium import webdriver
from selenium.webdriver.common.by import By

local_path = f'file://{os.path.dirname(os.path.realpath(__file__))}/'

chrome = webdriver.Chrome()
chrome.get(f'{local_path}exercicio01.html')

titulo = chrome.title
p_tag_name = chrome.find_element(By.TAG_NAME, "p").text
p_css_selector = chrome.find_element(By.CSS_SELECTOR, "p.content").text

print('\nExercício A')
print(f'Título: {titulo}')

print('\nExercício B')
print(f'Parágrafo (TAG NAME): {p_tag_name}')

print('\nExercício C')
print(f'Parágrafo (CSS SELECTOR): {p_css_selector}')

chrome.quit()