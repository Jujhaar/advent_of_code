import re
def convert_letters_to_numbers(text):
  text = text.replace("one", "o1ne")
  text = text.replace("two", "t2wo")
  text = text.replace("three", "th3ree")
  text = text.replace("four", "f4our")
  text = text.replace("five", "f5ive")
  text = text.replace("six", "s6ix")
  text = text.replace("seven", "se7ven")
  text = text.replace("eight", "ei8ght")
  text = text.replace("nine", "n9ine")
  return text

def extract_digits(text):
  digits = re.findall("\d", text)
  return digits


with open('files/day1file.txt', "r") as file:
  lines = file.readlines()

total = 0
for line in lines:
  converted_line = convert_letters_to_numbers(line)
  line_digits = extract_digits(converted_line)
  if len(line_digits) == 0:
    print("ERROR, no digits in line", line)
  else:
    line_sum = line_digits[0] + line_digits[-1]
    total += int(line_sum)
    print(line,converted_line, line_sum, total)
print(total)

