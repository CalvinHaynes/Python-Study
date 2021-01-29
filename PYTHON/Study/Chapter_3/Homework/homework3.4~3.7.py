#练习3-4
guest = ['Jack','Mary','John','michal']
for i in range(len(guest)):
    print(f'{guest[i]},please come to dinner.')


#练习3-5
No_guest = 'Jack'
print(f"\n{No_guest} can't make an appointment.\n")
del guest[0]
guest.insert(0,'Thomas')
for i in range(len(guest)):
    print(f'{guest[i]},please come to dinner.')


#练习3-6
print('\nOh! I have found a bigger table!')
guest.insert(0,'Lihua')
guest.append('Jackie')
guest.insert(3,"Wanggang")
for i in range(len(guest)):
    print(f'{guest[i]},please come to dinner.')

#练习3-7
print('\nSorry! we can only invite two people to dinner')
for i in range(len(guest)-2):
    poped_guest = guest.pop()
    print(f'sorry,{poped_guest},there is no room at the table')
for j in range(2):
    print(f'{guest[j]},please come to dinner.')

print('\n')

for k in range(len(guest)):   
    del guest[0]
print(guest)
