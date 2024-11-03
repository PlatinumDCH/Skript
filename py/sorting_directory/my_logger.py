import  logging

def setup_logger(name, level=logging.INFO,log_file=None):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    format_str = '%(asctime)s %(levelname)s - %(message)s'
    formatter = logging.Formatter(format_str)

    # output in console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

if __name__ == "__main__":
    logger = setup_logger(__name__, level=logging.DEBUG, log_file='app.log')

    logger.info('program start.')
    logger.debug('Debug messages')
    logger.error('Error msg')



