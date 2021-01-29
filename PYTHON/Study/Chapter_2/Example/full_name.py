#full_name.py
first_name = 'ada'
last_name  = 'lovelace'
full_name  = f"{first_name} {last_name}"
print(full_name)
print(f"Hello! {full_name.title()}!")

message = f"Hello! {full_name.title()}!"
print(message)

#python 3.5及之前
full_name = "{} {}".format(first_name,last_name)
print(full_name)
