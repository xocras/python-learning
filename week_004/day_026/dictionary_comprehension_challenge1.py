#  Dictionary Comprehension Challenge I

# 'What is the Airspeed Velocity of an Unladen Swallow?'

sentence = input()

result = {string: len(string) for string in sentence.split()}

print(result)
