#Pasanen Leena
import codecs

def encode(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    if len(s) > 1000:
        raise ValueError("Input length must be at most 1000 characters")
    
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=', '!"#€%&/()=1234567890'))
    
    # Check for specific characters to avoid
    for c in s:
        if c.lower() in ["+", "å", "ä", "ö"]:
            raise ValueError("Invalid character found: +, å, ä, or ö")
    
    # Encode the string
    for c in s:
        if c.isalpha():
            if c.islower():
                c = c.upper()
                crypted += codecs.encode(c, 'rot_13')
            elif c.isupper():
                c = c.lower()
                crypted += codecs.encode(c, 'rot_13')
        elif c in digitmapping:
            crypted += digitmapping[c]
        # Handle other characters here if needed
    
    return crypted

import codecs

def decode(s):
    decrypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=', '!"#€%&/()=1234567890'))
    
    for c in s:
        if c.isalpha():
            if c.isupper():
                c = c.lower()
            # Reverse ROT13 encryption
            decrypted += codecs.decode(c, 'rot_13')
        elif c in digitmapping.values():
            # Reverse the digit mapping
            for key, value in digitmapping.items():
                if value == c:
                    decrypted += key
    
    return decrypted
