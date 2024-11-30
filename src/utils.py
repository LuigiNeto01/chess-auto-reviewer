import pandas as pd
import json
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
from unidecode import unidecode
import openpyxl
from openpyxl.styles import Alignment, PatternFill
import pyodbc
import pandas as pd
from tqdm import tqdm
from time import sleep
from dotenv import *
from config.config_logger import *
from config.config import *

def criar_pasta(site_name):
    download_dir = os.path.join(os.getcwd(), "Downloads", site_name)
    os.makedirs(download_dir, exist_ok=True)
    return download_dir

def setup_driver(site_name, profile_path,mode= None):
    chrome_options = Options()
    chrome_options.add_argument(f"--user-data-dir={profile_path}")
    chrome_options.add_argument("--profile-directory=Default")
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--kiosk-printing')
    chrome_options.add_argument("--log-level=3")  # Suprime mensagens de log
    if mode == 'headless':
        chrome_options.add_argument('--headless')

    settings = {
        "recentDestinations": [{
            "id": "Save as PDF",
            "origin": "local",
            "account": ""
        }],
        "selectedDestinationId": "Save as PDF",
        "version": 2,
        "isHeaderFooterEnabled": False,
        "marginsType": 2,
        "scalingType": 3,
        "scaling": "100",
        "isLandscapeEnabled": False
    }

    prefs = {
        "download.default_directory": criar_pasta(site_name),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        'printing.print_preview_sticky_settings.appState': json.dumps(settings),
        'savefile.default_directory': criar_pasta(site_name)
    }
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(options=chrome_options)

    return driver

def clicar_elemento(driver, Xpath): 
    # Xpath é o xpath do elemento que deseja clicar
    
    element = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, Xpath))
    )
    element.click()

def esperar_elemento(driver, Xpath, timeout):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, Xpath))
        )
        return True
    except:
        False

def escrever_Input(driver, xpath, texto): 
    # xpath é o xpath do input onde deseja digitar
    # texto é o texto desejado no campo

    input_element = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    input_element.clear()
    input_element.send_keys(texto)

def load_json(caminho_json):
    try:
        with open(caminho_json, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
    except Exception as e:
        json_data = {}
    return json_data

def salvar_json(path, dados):
    with open(path , 'w', encoding='utf-8') as arquivo_json:
        json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)
