# 4. Найти в строке указанную подстроку и заменить ее на новую. Строку, ее подстроку для замены и новую подстроку вводит пользователь.

def find_substring(input_string, substring, new_substring):

    a = input_string.replace("baby", "child")
    print(a)

sub = 'baby'
string_a = 'cryingbabybaby'
new_sub = "child"
find_substring(string_a, sub, new_sub)

