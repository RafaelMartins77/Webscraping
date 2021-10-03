from selenium import webdriver
import pandas as pd
from IPython.display import display

nav = webdriver.Firefox()

# coletando dados

# dolar
nav.get("https://dolarhoje.com/")
cotacao_dolar = nav.find_element_by_xpath('//*[@id="nacional"]').get_attribute('value')

# euro
nav.get("https://www.melhorcambio.com/euro-hoje")
cotacao_euro = nav.find_element_by_xpath('//*[@id="comercial"]').get_attribute('value')

# importando planilha

produtos = pd.read_excel("preço_produto.xlsx")
display(produtos)

# atualizando planilha

produtos.loc[produtos['Moeda'] == "Dólar", "cotação"] = cotacao_dolar
produtos.loc[produtos['Moeda'] == "Euro", "cotação"] = cotacao_euro
display(produtos)

# exportanto planilha aualizada

produtos.to_excel("preços_atualizados.xlsx", index=False)
