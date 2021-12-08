
"""
log_type = "info"/"exception"/"debug"
"""
import logging


def print_logs(logs={'to_log': True, 'to_console': True}, msg="", log_type="info"):

    TO_LOG = logs['to_log']
    TO_CONSOLE = logs['to_console']

    if TO_LOG:
        if log_type == "info":
            logging.info(msg)
        elif log_type == "exception":
            logging.exception(msg)
        elif log_type == "debug":
            logging.debug(msg)

    if TO_CONSOLE:
        print(msg)



