def solution(input: list[str]):
    total = 0
    for line in input:
        nums = []
        for char in line:
            if ord(char) > 48 and ord(char) < 58:
                nums.append(char)
        total += int(nums[0] + nums[-1])
    print(total)
    
if __name__ == '__main__':
    puzzle_input = open("input.txt", "r").readlines()
    solution(puzzle_input)