def match_substring(start: int, input: str, substring: str):
    if len(substring) > len(input)-start:
        return False
    
    for i, subchar in enumerate(substring): 
        if input[start+i] != subchar:
            return False
    
    return True
        

def solution(input: list[str]):
    
    word_mapping = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    
    total = 0
    
    for line in input:
        nums = []
        idx = 0
        while idx < len(line):
            char = line[idx]
            if ord(char) > 48 and ord(char) < 58:
                nums.append(char)
            else:
                for (key, value) in word_mapping.items():
                    if match_substring(idx, line, key):
                        nums.append(value)
                        break      
            idx += 1    
        result = int(nums[0] + nums[-1])
        total += result
    print(total)
    
    
if __name__ == '__main__':
    puzzle_input = open("input.txt", "r").readlines()
    solution(puzzle_input)
    