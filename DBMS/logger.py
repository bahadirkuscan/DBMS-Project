import os
from enum import Enum
from .utils import PROJECT_ROOT
import time

class LogStatus(Enum):
    BEGIN = "BEGIN"
    SUCCESS = "success"
    FAILURE = "failure"

def log_command(message: str, status: LogStatus) -> None:
    """
    Log a message to the log file.
    For incomplete commands, the success parameter should be None. When the command is completed and the message is
    logged again with a definite status, the logs will be updated accordingly.

    :param status: whether the log is for an unfinished command (BEGIN), a successful command (SUCCESS), or a failed command (FAILURE).
    :param message: The message to log.
    """

    message = message.strip()
    log_file_path = os.path.join(PROJECT_ROOT, 'log.csv')

    # Ensure the log directory exists
    if not os.path.exists(log_file_path):
        f = open(log_file_path, 'w')
    else:
        f = open(log_file_path, 'a')

    if status == LogStatus.BEGIN:
        log = f"{int(time.time())}, {message}, {status.value}\n"
        f.write(log)
    elif status == LogStatus.SUCCESS:
        log = f"{int(time.time())}, {message}, {status.value}\n"
        f.write(log)
    elif status == LogStatus.FAILURE:
        log = f"{int(time.time())}, {message}, {status.value}\n"
        f.write(log)
    else:
        raise ValueError(f"Invalid status '{status}'. Expected 'BEGIN', 'SUCCESS', or 'FAILURE'.")
    f.close()

