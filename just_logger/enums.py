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
  DEBUG = [LogLevel.INFO, LogLevel.WARNING, LogLevel.ERROR, LogLevel.CRITICAL]
  PROD = [LogLevel.WARNING, LogLevel.ERROR]