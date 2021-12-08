
"""
log_type = "info"/"exception"/"debug"
"""
import logging


def print_logs(logs={'to_log': True, 'to_console': True}, msg="", log_type="info"):

    TO_LOG = logs['to_log']
    TO_CONSOLE = logs['to_console']

    if TO_LOG and log_type == "exception":
        if log_type == "exception":
            logging.exception(msg)

    if TO_CONSOLE:
        print(log_type + '\t' + msg)



