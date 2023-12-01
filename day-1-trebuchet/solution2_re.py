# Solution 2 using regex
import re

def solution(input: list[str]):
    
    total = 0
    
    mapping = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        # Abusing the unpacking operator to get
        # inline dictionary comprehension
        **{n: n for n in "123456789"},
    }
    
    regex_pattern = "(?=(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9))"
    
    for line in input:
        matches = re.findall(regex_pattern, line)
        if len(matches) > 0:
            total += int(mapping[matches[0]] + mapping[matches[-1]])
    
    print(total)    
    
if __name__ == '__main__':
    puzzle_input = open("input.txt", "r").readlines()
    solution(puzzle_input)
    