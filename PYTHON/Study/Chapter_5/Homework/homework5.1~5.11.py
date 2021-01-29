#练习5-3

#能通过测试的版本
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")


#不能通过测试的版本
alien_color = 'red' 
 
if alien_color == 'green': 
    print("You just earned 5 points!")
print('\n')


#练习5-4
#不执行 else 代码块的版本
alien_color = 'green' 
 
if alien_color == 'green': 
    print("You just earned 5 points!") 
else: 
    print("You just earned 10 points!")
print('\n')

#执行 else 代码块的版本
alien_color = 'yellow' 
 
if alien_color == 'green': 
    print("You just earned 5 points!") 
else:
    print("You just earned 10 points!")
print('\n')

#if-elif-else 结构
alien_color = 'red' 
 
if alien_color == 'green': 
    print("You just earned 5 points!") 
elif alien_color == 'yellow': 
    print("You just earned 10 points!") 
else: 
    print("You just earned 15 points!")
print('\n')


#练习5-6
age = 17 
 
if age < 2: 
    print("You're a baby!") 
elif age < 4: 
    print("You're a toddler!") 
elif age < 13: 
    print("You're a kid!") 
elif age < 20: 
    print("You're a teenager!") 
elif age < 65: 
    print("You're an adult!") 
else: 
    print("You're an elder!")
print('\n')


#练习5-7
favorite_fruits = ['blueberries', 'salmonberries', 'peaches'] 
 
if 'bananas' in favorite_fruits: 
    print("You really like bananas!")
if 'apples' in favorite_fruits: 
    print("You really like apples!") 
if 'blueberries' in favorite_fruits: 
    print("You really like blueberries!") 
if 'kiwis' in favorite_fruits: 
    print("You really like kiwis!") 
if 'peaches' in favorite_fruits: 
    print("You really like peaches!")    
print('\n')


#练习5-8
usernames = ['eric', 'willie', 'admin', 'erin', 'ever'] 
 
for username in usernames: 
    if username == 'admin': 
        print("Hello admin, would you like to see a status report?") 
    else: 
        print(f"Hello {username}, thank you for loggin in again!")

print('\n')

#练习5-9
usernames = [] 
 
if usernames: 
    for username in usernames: 
        if username == 'admin': 
            print("Hello admin, would you like to see a status report?") 
        else: 
            print(f"Hello {username}, thank you for loggin in again!") 
else: 
    print("We need to find some users!")

print('\n')

#练习5-10
print('\n')
current_users = ['john','jack','johnson','thomas','mary']

new_users = ['Tom','Jerry','Mark','JoHn','JAck']

current_users_compare = current_users[:]

for current_user in current_users_compare:
    current_user = current_user.lower()

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f'{new_user} has been used! please choose another name!\n')
    else:
        print(f"{new_user} hasn't been used yet!\nsuccess to sign in!\n")


#练习5-11
numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number   == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    else:
        print(f'{number}th')

