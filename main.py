from just_logger.logging import Logger

logger = Logger(log_file="logs/log-today.log")

logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")

print("Log Stack:", len(logger.log_stack))