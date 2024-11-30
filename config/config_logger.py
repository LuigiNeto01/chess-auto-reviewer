import logging
import colorlog
import sys

class AutomaticTracebackLogger(logging.Logger):
    # Logger personalizado para adicionar traceback automaticamente em logs de erro.
    def error(self, msg, *args, **kwargs):
        exc_info = sys.exc_info()
        if exc_info[0] is not None:
            kwargs['exc_info'] = exc_info
        super().error(msg, *args, **kwargs)

    def exception(self, msg, *args, **kwargs):
        kwargs['exc_info'] = True
        self.error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        exc_info = sys.exc_info()
        if exc_info[0] is not None:
            kwargs['exc_info'] = exc_info
        super().critical(msg, *args, **kwargs)

def start_logger(name='RPA', log_file='BSEM_Atacadao-pastas.log'):
    # Configura o logger com coloração para o console e gravação em arquivo.
    logging.setLoggerClass(AutomaticTracebackLogger)
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        logger.setLevel(logging.INFO)
        logger.addHandler(_create_console_handler())
        logger.addHandler(_create_file_handler(log_file))
    return logger

def _create_console_handler():
    # Cria e configura o console handler com coloração.
    log_format = "%(log_color)s%(asctime)s - %(levelname)s - %(message)s - [%(pathname)s:%(lineno)d]"
    log_colors = {
        'DEBUG': 'bold_blue',
        'INFO': 'bold_green',
        'WARNING': 'bold_yellow',
        'ERROR': 'bold_red',
        'CRITICAL': 'bold_purple'
    }
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = colorlog.ColoredFormatter(log_format, log_colors=log_colors)
    console_handler.setFormatter(formatter)
    return console_handler

def _create_file_handler(log_file):
    # Cria e configura o file handler para gravação de logs em arquivo.
    log_format = '%(asctime)s - %(levelname)s - %(message)s - [%(pathname)s:%(lineno)d]'
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter(log_format)
    file_handler.setFormatter(formatter)
    return file_handler

# Exemplo de uso
if __name__ == "__main__":
    logger = start_logger()