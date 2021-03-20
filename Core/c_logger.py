import logging
import coloredlogs

coloredlogs.DEFAULT_LOG_FORMAT = '%(asctime)s - %(message)s'
coloredlogs.DEFAULT_FIELD_STYLES = {'asctime': {'color': 'white'}}
level_styles = coloredlogs.DEFAULT_LEVEL_STYLES
level_styles['title'] = {'color':'blue', 'bold':True}
coloredlogs.install()

logging.getLogger("paramiko").setLevel(logging.WARNING)


TITLE = 68
SUCCESS = 70

logging.addLevelName(TITLE, 'TITLE')
logging.addLevelName(SUCCESS, 'SUCCESS')

def title_(message, *args, **kwargs):
    logging.log(TITLE, message, *args, **kwargs)


def success_(message, *args, **kwargs):
    logging.log(SUCCESS, message, *args, **kwargs)


logging.Logger.success_ = success_
logging.Logger.title_ = title_

log_level = logging.DEBUG

def debug(msg:str):
    logging.debug(msg)


def info(msg:str):
    logging.info(msg)


def critical(msg:str):
    logging.critical(msg)


def success(msg:str):
    success_(msg)


def error(msg:str):
    logging.error(msg)


def title(msg:str):
    coloredlogs.DEFAULT_LOG_FORMAT = '%(message)s'
    coloredlogs.install()
    print(len(msg)*'-')
    title_(msg)
    print(len(msg)*'-')
    coloredlogs.DEFAULT_LOG_FORMAT = '%(asctime)s - %(message)s' # reset coloredlogs format
    coloredlogs.install()
    