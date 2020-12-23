# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/


def find_first_occcur(needle, haystack):
    if needle == "":
        return 0
    else:
        return haystack.find(needle)


haystack = "hello"
needle = "ll"
print(find_first_occcur(needle, haystack))

haystack = "aaaaa"
needle = "bba"
print(find_first_occcur(needle, haystack))

haystack = ""
needle = ""
print(find_first_occcur(needle, haystack))
