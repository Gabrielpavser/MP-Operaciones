from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
from datetime import date, timedelta
yesterday = date.today() - timedelta(1)
ayer = yesterday.strftime('%d/%m/%Y')
contraseña = 'introducircontraseña'
usuario = 'introducir usuario'
driver = webdriver.Chrome("C:/Users/carogonzalez/Desktop/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(30)
#Abrir múltiples pestañas
driver.get('https://app.equals.com.br/conciliador/empresa/index/show')
driver.execute_script("window.open('https://app.equals.com.br/conciliador/empresa/index/show','new window')")
driver.execute_script("window.open('https://app.equals.com.br/conciliador/empresa/index/show','tab3')")
driver.execute_script("window.open('https://app.equals.com.br/conciliador/empresa/index/show','tab4')")
driver.execute_script("window.open('https://app.equals.com.br/conciliador/empresa/index/show','tab5')")
driver.execute_script("window.open('https://app.equals.com.br/conciliador/empresa/index/show','tab6')")
driver.execute_script("window.open('https://app.equals.com.br/conciliador/empresa/index/show','tab7')")
driver.execute_script("window.open('https://app.equals.com.br/conciliador/empresa/index/show','tab8')")
driver.execute_script("window.open('https://app.equals.com.br/conciliador/empresa/index/show','tab9')")
driver.execute_script("window.open('https://app.equals.com.br/conciliador/empresa/index/show','tab10')")
driver.execute_script("window.open('https://app.equals.com.br/conciliador/empresa/index/show','tab11')")
driver.execute_script("window.open('https://app.equals.com.br/conciliador/empresa/index/show','tab12')")
#Seleccionar la pestaña a utilizar
pestañas = driver.window_handles
driver.switch_to.window(pestañas [0])
#Loguearse
user = driver.find_element_by_id ("username")
user.send_keys(usuario)
passw = driver.find_element_by_id ("password")
passw.send_keys(contraseña)
enter = driver.find_element_by_id ("enter-equals")
enter.click()
#Elegir opción para ejecutar reporte
driver.find_element_by_link_text("Conciliação").click()
driver.find_element_by_link_text("Resumo Conc. de Vendas").click()
periodo_entrada = driver.find_element_by_id ("periodoDe")
periodo_entrada.clear()
periodo_entrada.send_keys("01/03/2018")
periodo_salida = driver.find_element_by_id ("periodoAte")
periodo_salida.clear()
periodo_salida.send_keys("31/03/2018")
adqui = driver.find_element_by_id ("botaoSelecionaradquirenteModal")
adqui.click()
driver.find_element_by_xpath("//input[@value='24']").click()
driver.implicitly_wait(25)
driver.find_element_by_xpath("//span[contains(@class,'ui-button-text') and contains(text(), 'Confirma')]").click()
driver.implicitly_wait(25)
driver.find_element_by_id ("opcaoDataPagamento").click ()
driver.find_element_by_id ("realizaDownload").click ()
driver.find_element_by_id ("botaoDownload").click ()
#Cambiar de pestaña para ejecutar otro reporte
driver.switch_to.window(pestañas [1])
user = driver.find_element_by_id ("username")
user.send_keys(usuario)
passw = driver.find_element_by_id ("password")
passw.send_keys(contraseña)
enter = driver.find_element_by_id ("enter-equals")
enter.click()
driver.find_element_by_link_text("Conciliação").click()
driver.find_element_by_link_text("Resumo Conc. de Vendas").click()
periodo_entrada = driver.find_element_by_id ("periodoDe")
periodo_entrada.clear()
periodo_entrada.send_keys("01/04/2018")
periodo_salida = driver.find_element_by_id ("periodoAte")
periodo_salida.clear()
periodo_salida.send_keys("30/04/2018")
adqui = driver.find_element_by_id ("botaoSelecionaradquirenteModal")
adqui.click()
driver.find_element_by_xpath("//input[@value='24']").click()
driver.implicitly_wait(25)
driver.find_element_by_xpath("//span[contains(@class,'ui-button-text') and contains(text(), 'Confirma')]").click()
driver.implicitly_wait(25)
driver.find_element_by_id ("opcaoDataPagamento").click ()
driver.find_element_by_id ("realizaDownload").click ()
driver.find_element_by_id ("botaoDownload").click ()
pestañas = driver.window_handles
driver.switch_to.window(pestañas [2])
user = driver.find_element_by_id ("username")
user.send_keys(usuario)
passw = driver.find_element_by_id ("password")
passw.send_keys(contraseña)
enter = driver.find_element_by_id ("enter-equals")
enter.click()
driver.find_element_by_link_text("Conciliação").click()
driver.find_element_by_link_text("Resumo Conc. de Vendas").click()
periodo_entrada = driver.find_element_by_id ("periodoDe")
periodo_entrada.clear()
periodo_entrada.send_keys("01/05/2018")
periodo_salida = driver.find_element_by_id ("periodoAte")
periodo_salida.clear()
periodo_salida.send_keys("31/05/2018")
adqui = driver.find_element_by_id ("botaoSelecionaradquirenteModal")
adqui.click()
driver.find_element_by_xpath("//input[@value='24']").click()
driver.implicitly_wait(25)
driver.find_element_by_xpath("//span[contains(@class,'ui-button-text') and contains(text(), 'Confirma')]").click()
driver.implicitly_wait(25)
driver.find_element_by_id ("opcaoDataPagamento").click ()
driver.find_element_by_id ("realizaDownload").click ()
driver.find_element_by_id ("botaoDownload").click ()
pestañas = driver.window_handles
driver.switch_to.window(pestañas [3])
user = driver.find_element_by_id ("username")
user.send_keys(usuario)
passw = driver.find_element_by_id ("password")
passw.send_keys(contraseña)
enter = driver.find_element_by_id ("enter-equals")
enter.click()
driver.find_element_by_link_text("Conciliação").click()
driver.find_element_by_link_text("Resumo Conc. de Vendas").click()
periodo_entrada = driver.find_element_by_id ("periodoDe")
periodo_entrada.clear()
periodo_entrada.send_keys("01/06/2018")
periodo_salida = driver.find_element_by_id ("periodoAte")
periodo_salida.clear()
periodo_salida.send_keys("30/06/2018")
adqui = driver.find_element_by_id ("botaoSelecionaradquirenteModal")
adqui.click()
driver.find_element_by_xpath("//input[@value='24']").click()
driver.implicitly_wait(25)
driver.find_element_by_xpath("//span[contains(@class,'ui-button-text') and contains(text(), 'Confirma')]").click()
driver.implicitly_wait(25)
driver.find_element_by_id ("opcaoDataPagamento").click ()
driver.find_element_by_id ("realizaDownload").click ()
driver.find_element_by_id ("botaoDownload").click ()
pestañas = driver.window_handles
driver.switch_to.window(pestañas [4])
user = driver.find_element_by_id ("username")
user.send_keys(usuario)
passw = driver.find_element_by_id ("password")
passw.send_keys(contraseña)
enter = driver.find_element_by_id ("enter-equals")
enter.click()
driver.find_element_by_link_text("Conciliação").click()
driver.find_element_by_link_text("Resumo Conc. de Vendas").click()
periodo_entrada = driver.find_element_by_id ("periodoDe")
periodo_entrada.clear()
periodo_entrada.send_keys("01/07/2018")
periodo_salida = driver.find_element_by_id ("periodoAte")
periodo_salida.clear()
periodo_salida.send_keys("31/07/2018")
adqui = driver.find_element_by_id ("botaoSelecionaradquirenteModal")
adqui.click()
driver.find_element_by_xpath("//input[@value='24']").click()
driver.implicitly_wait(25)
driver.find_element_by_xpath("//span[contains(@class,'ui-button-text') and contains(text(), 'Confirma')]").click()
driver.implicitly_wait(25)
driver.find_element_by_id ("opcaoDataPagamento").click ()
driver.find_element_by_id ("realizaDownload").click ()
driver.find_element_by_id ("botaoDownload").click ()
pestañas = driver.window_handles
driver.switch_to.window(pestañas [5])
user = driver.find_element_by_id ("username")
user.send_keys(usuario)
passw = driver.find_element_by_id ("password")
passw.send_keys(contraseña)
enter = driver.find_element_by_id ("enter-equals")
enter.click()
driver.find_element_by_link_text("Conciliação").click()
driver.find_element_by_link_text("Resumo Conc. de Vendas").click()
periodo_entrada = driver.find_element_by_id ("periodoDe")
periodo_entrada.clear()
periodo_entrada.send_keys("01/08/2018")
periodo_salida = driver.find_element_by_id ("periodoAte")
periodo_salida.clear()
periodo_salida.send_keys(ayer)
adqui = driver.find_element_by_id ("botaoSelecionaradquirenteModal")
adqui.click()
driver.find_element_by_xpath("//input[@value='24']").click()
driver.implicitly_wait(25)
driver.find_element_by_xpath("//span[contains(@class,'ui-button-text') and contains(text(), 'Confirma')]").click()
driver.implicitly_wait(25)
driver.find_element_by_id ("opcaoDataPagamento").click ()
driver.find_element_by_id ("realizaDownload").click ()
driver.find_element_by_id ("botaoDownload").click ()
pestañas = driver.window_handles
driver.switch_to.window(pestañas [6])
user = driver.find_element_by_id ("username")
user.send_keys(usuario)
passw = driver.find_element_by_id ("password")
passw.send_keys(contraseña)
enter = driver.find_element_by_id ("enter-equals")
enter.click()
driver.find_element_by_link_text("Conciliação").click()
driver.find_element_by_link_text("Resumo Conc. de Cancelamentos").click()
periodo_entrada = driver.find_element_by_id ("periodoDe")
periodo_entrada.clear()
periodo_entrada.send_keys("01/03/2018")
periodo_salida = driver.find_element_by_id ("periodoAte")
periodo_salida.clear()
periodo_salida.send_keys("31/03/2018")
adqui = driver.find_element_by_id ("botaoSelecionaradquirenteModal")
adqui.click()
driver.find_element_by_xpath("//input[@value='24']").click()
driver.implicitly_wait(25)
driver.find_element_by_xpath("//span[contains(@class,'ui-button-text') and contains(text(), 'Confirma')]").click()
driver.implicitly_wait(25)
driver.find_element_by_id ("opcaoDataPagamentoInterno").click ()
driver.find_element_by_id ("realizaDownload").click ()
driver.find_element_by_id ("botaoDownload").click ()
driver.switch_to.window(pestañas [7])
user = driver.find_element_by_id ("username")
user.send_keys(usuario)
passw = driver.find_element_by_id ("password")
passw.send_keys(contraseña)
enter = driver.find_element_by_id ("enter-equals")
enter.click()
driver.find_element_by_link_text("Conciliação").click()
driver.find_element_by_link_text("Resumo Conc. de Cancelamentos").click()
periodo_entrada = driver.find_element_by_id ("periodoDe")
periodo_entrada.clear()
periodo_entrada.send_keys("01/04/2018")
periodo_salida = driver.find_element_by_id ("periodoAte")
periodo_salida.clear()
periodo_salida.send_keys("30/04/2018")
adqui = driver.find_element_by_id ("botaoSelecionaradquirenteModal")
adqui.click()
driver.find_element_by_xpath("//input[@value='24']").click()
driver.implicitly_wait(25)
driver.find_element_by_xpath("//span[contains(@class,'ui-button-text') and contains(text(), 'Confirma')]").click()
driver.implicitly_wait(25)
driver.find_element_by_id ("opcaoDataPagamentoInterno").click ()
driver.find_element_by_id ("realizaDownload").click ()
driver.find_element_by_id ("botaoDownload").click ()
driver.switch_to.window(pestañas [8])
user = driver.find_element_by_id ("username")
user.send_keys(usuario)
passw = driver.find_element_by_id ("password")
passw.send_keys(contraseña)
enter = driver.find_element_by_id ("enter-equals")
enter.click()
driver.find_element_by_link_text("Conciliação").click()
driver.find_element_by_link_text("Resumo Conc. de Cancelamentos").click()
periodo_entrada = driver.find_element_by_id ("periodoDe")
periodo_entrada.clear()
periodo_entrada.send_keys("01/05/2018")
periodo_salida = driver.find_element_by_id ("periodoAte")
periodo_salida.clear()
periodo_salida.send_keys("31/05/2018")
adqui = driver.find_element_by_id ("botaoSelecionaradquirenteModal")
adqui.click()
driver.find_element_by_xpath("//input[@value='24']").click()
driver.implicitly_wait(25)
driver.find_element_by_xpath("//span[contains(@class,'ui-button-text') and contains(text(), 'Confirma')]").click()
driver.implicitly_wait(25)
driver.find_element_by_id ("opcaoDataPagamentoInterno").click ()
driver.find_element_by_id ("realizaDownload").click ()
driver.find_element_by_id ("botaoDownload").click ()
driver.switch_to.window(pestañas [9])
user = driver.find_element_by_id ("username")
user.send_keys(usuario)
passw = driver.find_element_by_id ("password")
passw.send_keys(contraseña)
enter = driver.find_element_by_id ("enter-equals")
enter.click()
driver.find_element_by_link_text("Conciliação").click()
driver.find_element_by_link_text("Resumo Conc. de Cancelamentos").click()
periodo_entrada = driver.find_element_by_id ("periodoDe")
periodo_entrada.clear()
periodo_entrada.send_keys("01/06/2018")
periodo_salida = driver.find_element_by_id ("periodoAte")
periodo_salida.clear()
periodo_salida.send_keys("30/06/2018")
adqui = driver.find_element_by_id ("botaoSelecionaradquirenteModal")
adqui.click()
driver.find_element_by_xpath("//input[@value='24']").click()
driver.implicitly_wait(25)
driver.find_element_by_xpath("//span[contains(@class,'ui-button-text') and contains(text(), 'Confirma')]").click()
driver.implicitly_wait(25)
driver.find_element_by_id ("opcaoDataPagamentoInterno").click ()
driver.find_element_by_id ("realizaDownload").click ()
driver.find_element_by_id ("botaoDownload").click ()
driver.switch_to.window(pestañas [10])
user = driver.find_element_by_id ("username")
user.send_keys(usuario)
passw = driver.find_element_by_id ("password")
passw.send_keys(contraseña)
enter = driver.find_element_by_id ("enter-equals")
enter.click()
driver.find_element_by_link_text("Conciliação").click()
driver.find_element_by_link_text("Resumo Conc. de Cancelamentos").click()
periodo_entrada = driver.find_element_by_id ("periodoDe")
periodo_entrada.clear()
periodo_entrada.send_keys("01/07/2018")
periodo_salida = driver.find_element_by_id ("periodoAte")
periodo_salida.clear()
periodo_salida.send_keys("31/07/2018")
adqui = driver.find_element_by_id ("botaoSelecionaradquirenteModal")
adqui.click()
driver.find_element_by_xpath("//input[@value='24']").click()
driver.implicitly_wait(25)
driver.find_element_by_xpath("//span[contains(@class,'ui-button-text') and contains(text(), 'Confirma')]").click()
driver.implicitly_wait(25)
driver.find_element_by_id ("opcaoDataPagamentoInterno").click ()
driver.find_element_by_id ("realizaDownload").click ()
driver.find_element_by_id ("botaoDownload").click ()
driver.switch_to.window(pestañas [11])
user = driver.find_element_by_id ("username")
user.send_keys(usuario)
passw = driver.find_element_by_id ("password")
passw.send_keys(contraseña)
enter = driver.find_element_by_id ("enter-equals")
enter.click()
driver.find_element_by_link_text("Conciliação").click()
driver.find_element_by_link_text("Resumo Conc. de Cancelamentos").click()
periodo_entrada = driver.find_element_by_id ("periodoDe")
periodo_entrada.clear()
periodo_entrada.send_keys("01/08/2018")
periodo_salida = driver.find_element_by_id ("periodoAte")
periodo_salida.clear()
periodo_salida.send_keys(ayer)
adqui = driver.find_element_by_id ("botaoSelecionaradquirenteModal")
adqui.click()
driver.find_element_by_xpath("//input[@value='24']").click()
driver.implicitly_wait(25)
driver.find_element_by_xpath("//span[contains(@class,'ui-button-text') and contains(text(), 'Confirma')]").click()
driver.implicitly_wait(25)
driver.find_element_by_id ("opcaoDataPagamentoInterno").click ()
driver.find_element_by_id ("realizaDownload").click ()
driver.find_element_by_id ("botaoDownload").click ()
