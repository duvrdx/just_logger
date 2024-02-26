import os
from dotenv import load_dotenv
from .enums import LogFilter


load_dotenv()

# Settings for just_logger project.
log_colors = {
  "INFO": "\033[94m",
  "WARNING": "\033[93m",
  "ERROR": "\033[91m",
  "CRITICAL": "\033[41m"
}

log_filter = os.environ.get("JL_LOG_FILTER", "DEBUG") # DEBUG, PROD, ONLY_INFO, ONLY_WARNING, ONLY_ERROR, ONLY_CRITICAL

match log_filter:
  case "DEBUG":
    log_filter = LogFilter.DEBUG
  case "PROD":
    log_filter = LogFilter.PROD
  case "ONLY_INFO":
    log_filter = LogFilter.ONLY_INFO
  case "ONLY_WARNING":
    log_filter = LogFilter.ONLY_WARNING
  case "ONLY_ERROR":
    log_filter = LogFilter.ONLY_ERROR
  case "ONLY_CRITICAL":
    log_filter = LogFilter.ONLY_CRITICAL
  case _:
    log_filter = LogFilter.DEBUG

