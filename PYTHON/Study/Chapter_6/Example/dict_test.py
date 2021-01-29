alien_0 = {'color':'green','points':5}

new_points = alien_0['points']
print(f'You just earned {new_points} points!\n')

#排列顺序与添加顺序相同
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

#值可以改变
alien_0['color'] = 'red'
print(alien_0)
print()#print自带一个换行(才发现有这种情况发生，如果是print('\n')的话，会空两行)

#添加外星人速度变化
alien_0['speed'] = 'medium'

print(f"The Original x_position is {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"Now the alien move to {alien_0['x_position']}(x_position)\n")

del alien_0['points']#删除的键值对会永远消失
print(alien_0)

favorite_languages = {
    'jen':'python',
    'chen':'C',
    'sarah':'JavaScript',
    'edward':'Java',
    'human':"python"
    }

language = favorite_languages['sarah'].title()
print(f"sarah's favorite language is {language}\n")

#如果访问字典的键不存在时，会出错
#解决办法如下：
point_value = alien_0.get('points','No point value assigned')#(参数1：指定键，参数二：指定键不存在时返回的值)
print(point_value)
print()

color_value = alien_0.get('color')
print(color_value)
print()

agrssivity_value = alien_0.get('agressivity')
print(agrssivity_value)
print()

#遍历字典
for name,language in favorite_languages.items():
    print(f'{name.title()},I see you love {language.upper()}')

print()

print(favorite_languages.keys())
print(favorite_languages.values())    
print()

#按特定顺序遍历字典中的所有键
#按字母顺序遍历
for name in sorted(favorite_languages.keys()):
    print(f'{name.title()},thank you for taking the poll.')
print()

#遍历字典中的所有值
for language in favorite_languages.values():
    print(language.title())
print()

#利用集合的互异性set()函数
for language in set(favorite_languages.values()):
    print(language)
print()

#集合
languages = {'python','C','python','Java','JavaScript'}
print(languages)