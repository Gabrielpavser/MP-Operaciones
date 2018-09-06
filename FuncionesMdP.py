#      Repositorio de Funciones - Automatización Colaborativa


#     Todas estas funciones son genéricas y contienen las librerías a incluir

# 	- Para mejorar la performance del prototipo es recomendable importar una 
#	 sola vez la librería en la parte superior del programa


############################# Chrome ###############################

##
#Define cual va ser nuestro Explorador.
##


def define_driver(chromedriver_location):
	from selenium import webdriver
	driver = webdriver.Chrome(chromedriver_location)
	return driver
##
#Define cual va ser nuestro Explorador y la carpeta de descarga.
##	
	
def define_driver_and_download_directory(download_path):
	from selenium import webdriver
	import json
	"""driver = webdriver.Chrome(chromedriver_location)"""
	chrome_options = webdriver.ChromeOptions()
	prefs = { 'download.default_directory': download_path }
	json.dumps(prefs)
	chrome_options.add_experimental_option('prefs', prefs)
	driver = webdriver.Chrome(chrome_options=chrome_options)
	return driver
##
#Abre una Página.
##
	
	
def open_webpage(driver,webpage):
	from selenium import webdriver
	driver.get(webpage)
##
#Sirve para ingresar fechas donde no se puede escribir.
##

	
def enter_date_picklist_by_id (driver,element_id,date):
	from selenium import webdriver
	element = driver.find_element_by_id(element_id)
	driver.execute_script("arguments[0].value = arguments[1]",element,date)

	
##
#Escribe un Campo reconociendolo por el nombre.
##

	
def send_keys_by_name(driver,element_name,keys_to_send):
	from selenium import webdriver
	usuario = driver.find_element_by_name(element_name)
	usuario.send_keys(keys_to_send)

##
#Escribe un Campo reconociendolo por el id.
##

	
def send_keys_by_id(driver,element_id,keys_to_send):
	from selenium import webdriver
	element = driver.find_element_by_id(element_id) 
	element.send_keys(keys_to_send)

##
#Hace click en un elemento reconociendolo por el id.
##
	
def click_element_by_id(driver,element_id):
	from selenium import webdriver
	element = driver.find_element_by_id(element_id) 
	element.click()
##
#Hace Click en un elemento reconociendolo por el xpath.
##	
	
def click_element_by_xpath(driver,element_xpath):
	from selenium import webdriver
	element = driver.find_element_by_xpath(element_xpath) 
	element.click()	
##
#Verifica la presencia de un elemento reconociendolo por el id.
##	
	
def element_visible_by_id(driver,element_id):
	from selenium import webdriver
	try:
		element = driver.find_element_by_id(element_id) 
		found = 1
	except:
		found=0
	return found
##
#Espera la presencia de un elemento reconociendolo por el id.
##

	
def wait_presence_of_element_by_id(driver,element_id):
	from selenium.webdriver.support import expected_conditions as EC
	from selenium.webdriver.support.ui import WebDriverWait
	from selenium.webdriver.common.by import By
	wait = WebDriverWait(driver, 100)
	element = wait.until(EC.element_to_be_clickable((By.ID,element_id)))
##
#Espera la presencia de un elemento reconociendolo por el id.
##
	
def wait_presence_of_element_by_xpath(driver,element_xpath):
	from selenium.webdriver.support import expected_conditions as EC
	from selenium.webdriver.support.ui import WebDriverWait
	from selenium.webdriver.common.by import By
	wait = WebDriverWait(driver, 100)
	element = wait.until(EC.element_to_be_clickable((By.XPATH,element_xpath)))

	
	
	
	
	
############################# Fechas	
	
	
##
#Devuelve la fecha aplicando una diferencia con respecto a la actual con dd-mm-yy.
##
		
def date_from_current_date(difference):
	import datetime
	today = datetime.date.today( )
	if difference==0:
		return today
	else:
		if difference>0:
			future = today + datetime.timedelta(days=difference)
			return future
		else:	
			past = today - datetime.timedelta(days=abs(difference))
			return past
##
#Devuelve la fecha aplicando una diferencia con respecto a la actual con dd/mm/yy.
##
		
			
def date_from_current_date_slash(difference):

	import datetime
	today = datetime.date.today( )
	if difference==0:
		return today.strftime("%d/%m/%Y")
	else:
		if difference>0:
			future = (today + datetime.timedelta(days=difference)).strftime("%d/%m/%Y")
			return future
		else:	
			past = (today - datetime.timedelta(days=abs(difference))).strftime("%d/%m/%Y")
			return past


###############################  Sistema operativo		
		
		
##
# Mueve archivos entre carpetas.
##

def move_files(folder_origin,folder_destination,file_name):
	import shutil
	folder1_name=folder_origin+'\\'+file_name
	folder2_name=folder_destination+'\\'+file_name
	shutil.move(folder1_name,folder2_name)
		
		
##
#Devuelve el nombre del ultimo archivo en una carpeta.
##		
def latest_file_name_from_directory(file_location):
	import glob
	import os
	list_of_files = glob.glob(file_location+'\\*') 
	latest_file = max(list_of_files, key=os.path.getctime).rsplit('\\', 1)
	return latest_file[1]
##
#Espera la descarg de un archivo.
##
	
def download_wait(path_to_downloads):
	import time
	import os
	seconds = 0
	dl_wait = True
	while dl_wait and seconds < 20:
		time.sleep(1)
		dl_wait = False
		for fname in os.listdir(path_to_downloads): 
			if fname.endswith('.crdownload'):#se fija si hay un archivo que termina con .crdownload
				dl_wait = True
		seconds += 1
	return seconds
	
##
#Elimina las lineas de un archivo txt que contengan una cadena de caracteres (content_string)
##
	
	
def delete_lines_from_txt_containing(download_path,file_name,content_string,additional_character):
	f=open(str(download_path+file_name),"r+")
	new_file_name =str(file_name[:-4]+additional_character+'.txt')
	f2=open(str(download_path+new_file_name),"w+") #le saco el .txt y despues se lo vuelvo a poner
	original_file = f.readlines()
	f2.seek(0)
	for line in original_file:
		if content_string not in line:
			f2.write(line)
	f2.truncate()
	return new_file_name

	
