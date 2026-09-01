import time
import csv

start_time = time.time()  # Get current time in second since the Epoch
print(time.ctime(1788164926))
my_range = range(100000000)
print(my_range[1000])

# time.sleep(2.5) # Stop for 2.5seconds
end_time = time.time()  # Get current time in second since the Epoch

print("Total duration of the operation: ", end_time -
      start_time)  # The difference in seconds
