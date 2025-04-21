# Caesar cipher for emoji characters (Unicode range 1F600-1F64F)

# Define the Unicode range for emoji characters
EMOJI_START = 0x1F600
EMOJI_END = 0x1F64F
EMOJI_RANGE = EMOJI_END - EMOJI_START + 1

# Read input
shift = int(input())
text = input()

# Encrypt the text
encrypted_text = ""
for char in text:
    # Check if the character is in the specified emoji range
    char_code = ord(char)
    if EMOJI_START <= char_code <= EMOJI_END:
        # Apply the shift with cyclic behavior
        position = char_code - EMOJI_START
        new_position = (position + shift) % EMOJI_RANGE
        new_char_code = EMOJI_START + new_position
        encrypted_text += chr(new_char_code)
    else:
        # Keep non-emoji characters unchanged
        encrypted_text += char

# Output the encrypted text
print(encrypted_text)