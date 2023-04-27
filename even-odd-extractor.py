# Open numbers.txt (read), even.txt (append), odd.txt (append)
with open("numbers.txt") as main_file, open("even.txt", "a") as even_file, open("odd.txt", "a") as odd_file:
    # Read numbers.txt line by line 
    numbers = main_file.readlines()
    for line in numbers:
        # If even
        if int(line) % 2 == 0:
            even_file.write(str(line))
        # If odd
# Print the output