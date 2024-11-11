import logging
import logging.config
import os


def get_logger(logger_name: str, filename: str) -> logging.Logger:
    """
    Creates and configures a logger with both file and console handlers.

    If a logger with the given name does not already exist, this function will:
    - Create a directory named 'logs' if it does not already exist.
    - Configure a logger with the specified name and set its logging level to DEBUG.
    - Add a file handler to write log messages to the specified file in the 'logs' directory, with DEBUG level logging.
    - Add a console handler to display ERROR level log messages in the console.

    Log messages are formatted to include the timestamp, logger name, log level, filename, line number, and message.

    Args:
        logger_name (str): The name of the logger to create or retrieve.
        filename (str): The name of the file to write log messages to within the 'logs' directory.

    Returns:
        logging.Logger: Configured logger instance.
    """
    if not os.path.exists('logs'):
        os.makedirs('logs')
    logger = logging.getLogger(logger_name)
    if not logger.hasHandlers():
        logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(f'logs/{filename}')
        file_handler.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.ERROR)

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(filename)s - line %(lineno)d - %(message)s'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
