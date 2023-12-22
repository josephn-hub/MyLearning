import re


text_name = '''My name is JOSPEH , and studying machine learning course from 08-08-2023.

Mr. John
Mrs. Kate
Ms. Sasyara
Mr T
Mr. Jake Thomas

sit
pit
kit
tit
'''

phone_number = '''
740-5434-054
996*6223*844
900.0053.110
800-2341-567

'''

pattern_check = re.compile(r'[89]00[- * .]\d\d\d\d[- * .]\d\d\d')
word_pattern_check = re.compile(r'[^t]it')
name_pattern_check = re.compile(r'M(R|r|s|rs).?\s[A-Z]\w*')
regex = '^\w+\s+\w*'


check_word = word_pattern_check.finditer(text_name)
check_numbers = pattern_check.finditer(phone_number)
check_names = name_pattern_check.finditer(text_name)

for name in check_names:
    print(name)

# print(text_name[18:19])


