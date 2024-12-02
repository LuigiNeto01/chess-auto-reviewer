from src.utils import *

def login_chess(driver, data):
    load_dotenv(Chess['Paths']['dotenv'], override=True)

    driver.get(Chess['Url']['login'])

    escrever_Input(driver,Chess['Xpath']['login'],os.getenv('USERNAME'))
    escrever_Input(driver,Chess['Xpath']['senha'],os.getenv('PASSWORD'))

    clicar_elemento(driver,Chess['Xpath']['lembrar_me'])
    clicar_elemento(driver,Chess['Xpath']['entrar'])

    data['logged'] = True
    salvar_json(Chess['Paths']['json'], data)

def get_stats(driver, url):

    codigo = url.split('/')[-1]
    driver.get(Chess['Url']['review'].format(codigo))


def main(url):
    
    driver = setup_driver('chess', os.path.join(os.getcwd(), 'data/profile'))

    data = load_json(Chess['Paths']['json'])

    if data['logged'] == False:
        login_chess(driver, data)

    get_stats(driver, url)
