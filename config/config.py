Chess = {
    "Url": {
        'login':'https://www.chess.com/pt-BR/login_and_go?returnUrl=https://www.chess.com/pt-BR',
        'review':'https://www.chess.com/analysis/game/live/{}?tab=review',
    },
    "Xpath": {
        'login':'//*[@id="username-input-field"]/div/input',
        'senha':'//*[@id="password-input-field"]/div/input',
        'lembrar_me':'//*[@id="authentication-login-form"]/div[4]/div/label',
        'entrar':'//*[@id="login"]',
    },
    "Paths": {
        'json':r'data/logged.json',
        'dotenv':'config/.env',
    }
}