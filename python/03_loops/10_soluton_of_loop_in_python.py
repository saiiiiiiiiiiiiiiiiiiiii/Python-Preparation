
# 10) Exponential Backoff
# Implement an Exponential Backoff Stratergy that doubles the waiting time between retries,
# stsrting from 1 sec but stops after 5 retries 
import time
waiting_time = 1
maximum_retries = 5
attempts = 0
while attempts < maximum_retries:
  print(f"attempt's {attempts + 1} waiting time second's  {waiting_time}" )
  time.sleep(waiting_time)
  waiting_time *= 2
  attempts += 1