'''
Create a list of all odd numbers between 1 and a max number. Max number is something you
need to take from a user using input() function
'''

def oddNumbers(num):
    odd_nums = []
    for i in range(1, num):
        if i%2 != 0:
            odd_nums.append(i)

    return odd_nums

odd_nums = oddNumbers(10)
print(odd_nums)
