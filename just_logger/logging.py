from datetime import datetime
from enums import LogLevel, LogFilter
from exceptions import LogError
from utils import add_file_and_line
import settings


class Log(object):
  def __init__(self, message: str = None, level: LogLevel = LogLevel.INFO) -> None:
    self.message: str = message
    self.level: LogLevel = level
    self.timestamp: str = datetime.now().isoformat() 
    
    if self.level in settings.log_filter.value:
      print(self) 
  
  def __str__(self, is_file: bool = False) -> str:
    if is_file:
      return f"| {self.timestamp} - {self.level.value}: {self.message} |".ljust(150)
    return f"{settings.log_colors[self.level.value]}| {self.timestamp} - {self.level.value}: {self.message} ".ljust(150) + "|\033[0m"
  
class Logger(object):
  def __init__(self, log_file: str = None) -> None:
    self.log_file: str = log_file
    self.log_stack: list = []
    
  def _filter_log(self, filter: list[LogLevel]) -> list[Log]:
    return [log for log in self.log_stack if log.level in filter]
  
  def _log(self, log: Log) -> None:
    try: 
      with open(self.log_file, "a") as file:
        file.write(log.__str__(is_file=True) + "\n")
    except Exception as e:
      raise LogError(f"Error to Open Log File: {e}")
    
  def _create_log(self, log: Log) -> None:
    self.log_stack.append(log)
    
    if self.log_file:
      try:
        self._log(log)
      except LogError as e:
        print(e)
    
  def info(self, message: str) -> Log:
    self._create_log(Log(message, LogLevel.INFO))
  
  def warning(self, message: str) -> Log:
    self._create_log(Log(add_file_and_line(message), LogLevel.WARNING))
  
  def error(self, message: str) -> Log:
    self._create_log(Log(add_file_and_line(message), LogLevel.ERROR))
  
  def critical(self, message: str) -> Log:
    self._create_log(Log(add_file_and_line(message), LogLevel.CRITICAL))
  
  def print_log_stack(self, log_filter: LogFilter = LogFilter.DEBUG) -> None:
    for log in self.filter_log(filter = log_filter.value):
      print(log)
      
      