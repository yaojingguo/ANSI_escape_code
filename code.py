import time

def move_cursor():
  print("line1")
  time.sleep(2)
  print("\033[FMy text overwriting the previous line.")
  time.sleep(2)
  print("line2")
  time.sleep(2)


move_cursor()
