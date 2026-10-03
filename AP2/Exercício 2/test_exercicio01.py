import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

local_path = f'file://{os.path.dirname(os.path.realpath(__file__))}/'

@pytest.fixture
def chrome():
    chrome = webdriver.Chrome()
    chrome.get(f'{local_path}exercicio01.html')
    yield chrome
    chrome.quit()

def test_titulo(chrome):
    assert chrome.title == "Exercício 01"

def test_paragrafo_tag_name(chrome):
    texto = chrome.find_element(By.TAG_NAME, "p").text
    assert texto == "O conteúdo do site vem aqui"

def test_paragrafo_css_selector(chrome):
    texto = chrome.find_element(By.CSS_SELECTOR, "p.content").text
    assert texto == "O conteúdo do site vem aqui"