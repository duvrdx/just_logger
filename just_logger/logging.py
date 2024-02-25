from datetime import datetime
from enums import LogLevel, LogFilters
from exceptions import LogError
from utils import add_file_and_line


class Log(object):
  
  _log_colors = {
    LogLevel.INFO: "\033[94m",
    LogLevel.WARNING: "\033[93m",
    LogLevel.ERROR: "\033[91m",
    LogLevel.CRITICAL: "\033[41m"
  }
  
  def __init__(self, message: str = None, level: LogLevel = LogLevel.INFO):
    self.message: str = message
    self.level: LogLevel = level
    self.timestamp: str = datetime.now().isoformat() 
    
    #TODO: Add a way to select log level in .env
    print(self) 
  
  def __str__(self, is_file: bool = False) -> str:
    if is_file:
      return f"| {self.timestamp} - {self.level.value}: {self.message} |".ljust(150)
    return f"{self._log_colors[self.level]}| {self.timestamp} - {self.level.value}: {self.message} ".ljust(150) + "|\033[0m"
  
  
class Logger(object):
  def __init__(self, log_file: str = None):
    self.log_file: str = log_file
    self.log_stack: list = []
    
  def _filter_log(self, filter: list[LogLevel]):
    return [log for log in self.log_stack if log.level in filter]
  
  def _log(self, log: Log):
    try: 
      with open(self.log_file, "a") as file:
        file.write(log.__str__(True) + "\n")
    except Exception as e:
      raise LogError(f"Error to Open Log File: {e}")
    
  def create_log(self, log: Log):
    self.log_stack.append(log)
    
    if self.log_file:
      try:
        self._log(log)
      except LogError as e:
        print(e)
    
  def info(self, message: str):
    return Log(message, LogLevel.INFO)
  
  def warning(self, message: str):
    return Log(add_file_and_line(message), LogLevel.WARNING)
  
  def error(self, message: str):
    return Log(add_file_and_line(message), LogLevel.ERROR)
  
  def critical(self, message: str):
    return Log(add_file_and_line(message), LogLevel.CRITICAL)
  
  def print_log_stack(self, log_filter: LogFilters = LogFilters.ALL):
    for log in self.filter_log(filter = log_filter.value):
      print(log)
      
      