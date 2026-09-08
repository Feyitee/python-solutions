# Phase 2: Tuples & Immutability
# 
# Problem 6 of 100: The Protected RecordGoal: Understand that tuples cannot be changed (immutability) and extract data from them.Instructions:Unlike lists, tuples use parentheses ( ) and cannot be modified after they are created.Write a function called get_user_info(user_tuple) that takes a tuple representing a user 
# record: (user_id, name, email, age). The function should return a formatted string saying: "User [name] is [age] years old."


user = (101, "Alice", "alice@example.com", 28)
def get_user_info(data):
    age = data[-1]
    user_name = data[1]
    email_address = data[2]
    return (f"User {user_name} is {age}yrs old at email {email_address}")

print(get_user_info(user))