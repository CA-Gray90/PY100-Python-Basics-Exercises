# Write code that checks whether the string char_sequence contains the character x

char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'

print('x' in char_sequence)
print(char_sequence.find('x'))

for char in char_sequence:
    if char == 'x':
        print(f"'x' has been found! It is at index {char_sequence.find(char)}!")
        break

print("'x' has been found!" if 'x' in char_sequence else "'x' not found :(")