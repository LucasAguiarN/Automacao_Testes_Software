import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

local_path = f'file://{os.path.dirname(os.path.realpath(__file__))}/'
URL = f'{local_path}index.html'

dados = {
    "nome": "Lucas Aguiar Nunes",
    "ra": "2403912",
    "data_nascimento": "18/11/1998",
    "curso": "Análise e Desenvolvimento de Sistemas",
    "aproveitamento": "9",
    "sugestoes": "Fazer exercícios práticos aplicando em projetos dos semestres anteriores com acompanhamento do professor.",
    "observacoes": "Essa disciplina deveria ter vindo antes na grade em vez de ser no último semestre.",
}

chrome = webdriver.Chrome()
chrome.maximize_window()

chrome.get(URL)
time.sleep(0.8)

campo_nome = chrome.find_element(By.ID, "nome")
campo_nome.send_keys(dados["nome"])
time.sleep(0.8)

campo_ra = chrome.find_element(By.ID, "ra")
campo_ra.send_keys(dados["ra"])
time.sleep(0.8)

campo_dia = chrome.find_element(By.ID, "dia")
campo_dia.send_keys(dados["data_nascimento"].split("/")[0])
time.sleep(0.8)

campo_mes = chrome.find_element(By.ID, "mes")
campo_mes.send_keys(dados["data_nascimento"].split("/")[1])
time.sleep(0.8)

campo_ano = chrome.find_element(By.ID, "ano")
campo_ano.send_keys(dados["data_nascimento"].split("/")[2])
time.sleep(0.8)

campo_curso = Select(chrome.find_element(By.ID, "curso"))
campo_curso.select_by_visible_text(dados["curso"])
time.sleep(0.8)

campo_aproveitamento = Select(chrome.find_element(By.ID, "aproveitamento"))
campo_aproveitamento.select_by_value(dados["aproveitamento"])
time.sleep(0.8)

campo_sugestoes = chrome.find_element(By.ID, "sugestoes")
campo_sugestoes.send_keys(dados["sugestoes"])
time.sleep(0.8)

campo_observacoes = chrome.find_element(By.ID, "observacoes")
campo_observacoes.send_keys(dados["observacoes"])
time.sleep(0.8)

botao_enviar = chrome.find_element(By.ID, "btn")
botao_enviar.click()
time.sleep(2.0)

chrome.quit()