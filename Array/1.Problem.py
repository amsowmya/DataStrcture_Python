'''
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''

expenses = {'Jan': 2200, 'Feb': 2350, 'Mar': 2600, 'Apr': 2130, 'May': 2190}

if expenses['Feb'] > expenses['Jan']:
    extra_amt = expenses['Feb'] - expenses['Jan']
    print(f"On month Feb extra {extra_amt} amount spent")
else:
    print('There is no extra amount spent')

# 2. Find out your total expense in first quarter (first three months) of the year.
i = 0
total_amt = 0
for key in expenses.keys():
    if i == 3:
        break
    total_amt += expenses[key]
    i += 1

print(f'On first quater total amount spent {total_amt}')

# 3. Find out if you spent exactly 2000 dollars in any month

for key in expenses.keys():
    if expenses[key] == 2000:
        print(f'In the month of {key}, spent exactly 2000')
    else:
        print('In non of the months spent exactly 2000')

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

expenses['June'] = 1980
print(expenses)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list

expenses['Apr'] = expenses['Apr'] - 200
print(expenses)