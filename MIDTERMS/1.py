with open('numbers.txt', 'r') as file:
    num=file.readlines()

for idx, line in enumerate(num):
    line=line.strip()
    numbers=[int(n) for n in line.split(',') if n.isdigit()]
    total_sum=sum(numbers)
    
    if str(total_sum) == str(total_sum)[::-1]:
        final="is a Palindrome"
    else:
        final="is not a palindrome"
    print(f"Line {idx + 1}: {line} (sum {total_sum}) {final}")