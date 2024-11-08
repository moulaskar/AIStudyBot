import logging
import os
from datetime import datetime

class Logger:
    def __init__(self, name):
        # Create and configure logger
        now = datetime.now()
        timestmp = now.strftime("%y%m%d%H%M%S")
        logFilename = timestmp + "_" + name + ".log" 
        log_file_path = os.path.join("logs", logFilename)
        os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

        self.level = logging.DEBUG
        logging.basicConfig(
            level= self.level,
            filename=log_file_path,
            filemode='w'    
        )

        # Creating an object
        self.logger = logging.getLogger(name)
        self.logger.setLevel(self.level)

    # Function to change log level
    def change_log_level(self, level):
        self.logger.setLevel(level)
        self.level = level

    def logMsg(self, msg: str):
        level = self.level

        if level == logging.DEBUG:
            self.logger.debug(msg)
        elif level == logging.INFO:
            self.logger.info(msg)
        elif level == logging.WARNING:
            self.logger.warning(msg)
        elif level == logging.ERROR:
            self.logger.error(msg)
        elif level == logging.CRITICAL:
            self.logger.critical(msg)
        else:
            self.logger.error(f"Unknown log level: {level}. Message: {msg}")

    def debug(self, msg: str):
        self.logger.debug(msg)

    def info(self, msg: str):
        self.logger.info(msg)

    def warning(self, msg: str):
        self.logger.warning(msg)

    def error(self, msg: str):
        self.logger.error(msg)

    def critical(self, msg: str):
        self.logger.critical(msg)

    