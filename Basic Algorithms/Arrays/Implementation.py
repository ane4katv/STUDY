

# ======== NEXT ============
# finish
# https://www.youtube.com/watch?v=xNaLrnTuw-M record algorithm

# do the rest of Lucid

# try 3-4 easy leetcode


def lower_to_cap(char):
    letter = ord(char) # prints decimal ASCII
    conv = 0b11011111 # created num that has all '1s' and just the one zero
                  # at the place we need to have zero
                  # 01100010 &
                  # 11011111        ANDing '1' will keep all original digits, ANDing zero will make zero!

    cap_letter  = chr(letter & conv)

    return cap_letter
#
def cap_to_lower(char):
    letter = ord(char)
    to_lower = 0b00100000 # using OR ( | ) with all zeros beside of one '1' in the place where we need '1'
                          # all other digits will remain the same!
    result = chr(letter | to_lower)

    return result

print(f'Upper case is ', lower_to_cap('b'))
print(f'Lower case is ', cap_to_lower('B'))

# convert letter to upper or lowercase.
letr = ord('a')
to_upper = 0b11011111 # 0b11011111, 0xDF
to_lower = 32  # 0b00100000, 0x20 *** Can use decimal representation of binary number

print("\nBitwise 'AND' operator: 97 & 223 =", chr( letr & to_upper ))
print("Bitwise 'OR' operator: 97 | 32 =", chr(  letr | to_lower ))