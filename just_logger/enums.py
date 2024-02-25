from enum import Enum

class LogLevel(Enum):
  INFO = "INFO"
  WARNING = "WARNING"
  ERROR = "ERROR"
  CRITICAL = "CRITICAL"

class LogFilter(Enum):
  ONLY_INFO = [LogLevel.INFO]
  ONLY_WARNING = [LogLevel.WARNING]
  ONLY_ERROR = [LogLevel.ERROR]
  ONLY_CRITICAL = [LogLevel.CRITICAL]
  ALL = [LogLevel.INFO, LogLevel.WARNING, LogLevel.ERROR, LogLevel.CRITICAL]
  LTE_ERROR = [LogLevel.INFO, LogLevel.WARNING, LogLevel.ERROR]
  LTE_WARNING = [LogLevel.INFO, LogLevel.WARNING]

class LogColor(Enum):
  INFO = "\033[94m"
  WARNING = "\033[93m"
  ERROR = "\033[91m"
  CRITICAL = "\033[41m"
  RESET = "\033[0m"