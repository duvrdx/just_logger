# Just Logger 
__________________________________________

This is a library featuring a simple logger for Python 3.


## Features
_________________________________________
- Add Log by Type ✔️
- Save Log's to file ✔️
- Filter Log's by Type ✔️
- Configure by .env ✔️

## Using 
__________________________________________

Here's how you can use this library to log events. First, let's understand the options for Levels and Filters.

### Levels
```python
class LogLevel(Enum):
  INFO = "INFO"
  WARNING = "WARNING"
  ERROR = "ERROR"
  CRITICAL = "CRITICAL"
```

### Filters
```python
class LogFilter(Enum):
  ONLY_INFO = [LogLevel.INFO]
  ONLY_WARNING = [LogLevel.WARNING]
  ONLY_ERROR = [LogLevel.ERROR]
  ONLY_CRITICAL = [LogLevel.CRITICAL]
  DEBUG = [LogLevel.INFO, LogLevel.WARNING, LogLevel.ERROR, LogLevel.CRITICAL]
  PROD = [LogLevel.WARNING, LogLevel.ERROR]
```

### Creating a Log

To create a log, first you must instantiate a Logger class. Then, create logs at the key points in your code.

```python
from just_logger import logging as jl

logger = jl.Logger(log_file="logs/log.log")

logger.info("This is an info message")
# | 2024-02-26T08:43:06.094567 - INFO: This is an info message |                                                                                        

```
This example demonstrates how to use the library to log an informational message.