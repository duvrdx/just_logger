from enum import Enum

class LogLevel(Enum):
  INFO = "INFO"
  WARNING = "WARNING"
  ERROR = "ERROR"
  CRITICAL = "CRITICAL"

class LogFilters(Enum):
  ONLY_INFO = [LogLevel.INFO]
  ONLY_WARNING = [LogLevel.WARNING]
  ONLY_ERROR = [LogLevel.ERROR]
  ONLY_CRITICAL = [LogLevel.CRITICAL]
  ALL = [LogLevel.INFO, LogLevel.WARNING, LogLevel.ERROR, LogLevel.CRITICAL]
  LTE_ERROR = [LogLevel.INFO, LogLevel.WARNING, LogLevel.ERROR]
  LTE_WARNING = [LogLevel.INFO, LogLevel.WARNING]