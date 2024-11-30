from src.utils import *


def main():
    
    driver = setup_driver('chess', os.path.join(os.getcwd(), 'data/profile'))

    data = load_json(r'data/logged.json')

    if data['logged'] == False:
        load_dotenv('config/.env', override=True)

        driver.get('https://www.chess.com/pt-BR/login_and_go?returnUrl=https://www.chess.com/pt-BR')

        escrever_Input(driver,'//*[@id="username-input-field"]/div/input',os.getenv('USERNAME'))
        escrever_Input(driver,'//*[@id="password-input-field"]/div/input',os.getenv('PASSWORD'))

        clicar_elemento(driver,'//*[@id="authentication-login-form"]/div[4]/div/label')
        clicar_elemento(driver,'//*[@id="login"]')

        data['logged'] = True
        salvar_json(r'data/logged.json', data)

    url = input('url da partida: ')
    codigo = url.split('/')[-1]
    driver.get(f'https://www.chess.com/analysis/game/live/{codigo}?tab=review')

main()
