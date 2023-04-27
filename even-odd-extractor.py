import pyfiglet

import colorama
from colorama import Fore

description = "Program 1: Even-Odd Extractor"
print(pyfiglet.figlet_format (description.center(5)) + Fore.BLUE)

# Open numbers.txt (read), even.txt (append), odd.txt (append)
with open("numbers.txt") as main_file, open("even.txt", "a") as even_file, open("odd.txt", "a") as odd_file:
    # Read numbers.txt line by line 
    numbers = main_file.readlines()
    for line in numbers:
        # If even
        if int(line) % 2 == 0:
            even_file.write(str(line))
        # If odd
        else:
            odd_file.write(str(line))
            
# Print the output
print(numbers)