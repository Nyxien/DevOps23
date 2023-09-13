import json

my_chars = '["abc","\u00e5\u00e4\u00f6","123"]'
data_list = json.loads(my_chars)
for item in data_list:
    print(item)