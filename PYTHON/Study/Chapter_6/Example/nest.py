#字典列表
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'red','points':10}
alien_2 = {'color':'blue','points':15}

aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

#在字典中存储列表(一个键关联多个值)
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
    }

print(f"You ordered a {pizza['crust']}-crust""with the following toppings:")

for topping in pizza['toppings']:
    print('\t' + topping)

#改进favorite_language
favorite_languages = {
    'jen':['python','C'],
    'chen':['python','C','Java','JavaScript'],
    'jack':['python'],
    "mark":['C','C#','C++'],
}

for name,languages in favorite_languages.items():
    if(len(languages) == 1):
        language = favorite_languages[name][0]
        print(f"\n{name}'s favorite language is {language}.")
    else:
        print(f"\n{name}'s favorite languages are:")
        for language in languages:
            print(f"\t{language}")

#字典嵌套字典
users ={
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },
}

for username,user_info in users.items():
    print(f"\nUsername:{username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name:{full_name.title()}")
    print(f"\tLocation:{location}")