import math
from random import randint


print(math.log2(512))
#creating a random list of 10 munbers where element range from 0 to 100
random_numbers = [randint(1, 100) for i in range(10)]

#os module interact with operating system
import os
current_directory = os.getcwd()  #get current working directory

# sys for system specific parameters
import sys
print(sys.argv)  # Command-line arguments

#get date and time, modify it, format it
from datetime import datetime
current_time = datetime.now()  # Get the current date and time
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
