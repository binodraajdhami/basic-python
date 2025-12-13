# String Data Type
# Escape String
address = "Hattban\"s Lalitpur"
address = "Hattban\'s Lalitpur\\"
address = "Hattban \nLalitpur"
address = "Hattban Lalitpur"

# Check total characters
print(len(address))

# Check First Position
print(address[0])

# Check Last Position
print(address[-1])

# Check Random Position
print(address[5])

print(address[0:7])
print(address[:7])
print(address[:])

first_name = "Binod"
last_name = 'RD'

# Concatnation: , +
full_name = first_name + " " + last_name

# Format String
full_name = f"Fist Name: {first_name} \nLast Name: {last_name}"

message = """
Hi Jharana!
How are you doing?
I hope you are doing good!
"""

print(message)
