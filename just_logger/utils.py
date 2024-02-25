import inspect 

def add_file_and_line(message: str):
  frame = inspect.currentframe()
  frame = inspect.getouterframes(frame)
  return f"{message} - {frame[2][1]}:{frame[2][2]}"