
1. Define a function called `convert_num_to_words` that converts numbers from 0 to 999 to their equivalent in words. This function will be used to convert the day, month, and year to words.
2. Write a function called `convert_date_to_words` that takes a date in the format "ddmmyyyy" as input and returns the date in words using the `convert_num_to_words` function.
3. Get the date input from the user using `input()` function and convert it to words using the `convert_date_to_words` function.

Here's the complete code:

```python
# filename: date_to_words.py

def convert_num_to_words(num):
    # Define the number names for 0-19, tens, and special cases
    num_names = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
        11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
        19: 'nineteen',
        2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
        7: 'seventy', 8: 'eighty', 9: 'ninety'
    }

    # Convert the number to words
    if num < 20:
        return num_names[num]
    elif num < 100:
        return num_names[num // 10 * 10] + '-' + num_names[num % 10]
    else:
        return num_names[num // 100] + ' hundred' + \
               (' and ' + convert_num_to_words(num % 100) if num % 100 > 0 else '')

def convert_date_to_words(date):
    day = convert_num_to_words(int(date[:2]))
    month = convert_num_to_words(int(date[2:4]))
    year = convert_num_to_words(int(date[4:]))

    return f"{day} {month} {year}"

# Get the date input from the user
date_input = input("Enter the date (ddmmyyyy): ")

# Convert the date to words
date_in_words = convert_date_to_words(date_input)

# Print the result
print(f"The date in words is: {date_in_words}")
```

To execute this code, the user needs to save the code in a file named `date_to_words.py` and run it using Python. After running the code, the user will be prompted to enter the date in the format "ddmmyyyy". The program will then print the date in words.
