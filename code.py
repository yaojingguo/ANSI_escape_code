import time

def move_cursor():
  print("line1")
  time.sleep(2)
  print("\033[FMy text overwriting the previous line.")
  time.sleep(2)
  print("line2")
  time.sleep(2)

def esc(code):
  return f"\033[{code}m"

def color():
  print('this is ', esc('31'), 'really', esc(0), ' important', sep='')
  print('this is ', esc('31;1'), 'really', esc(0), ' important', sep='')
  print('this is ', esc('31;1;4'), 'really', esc(0), ' important', sep='')

color()
