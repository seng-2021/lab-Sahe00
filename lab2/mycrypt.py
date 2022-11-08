import codecs

def encode(s):
    if not isinstance(s,str):
        raise TypeError
    origlen = len(s)
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if len(s) > 1000:
        raise ValueError
        
    for c in s:
        if 0 <= ord(c) <= 127:
            if c.isalpha():
                if c.islower():
                    c=c.upper()
                # Rot13 the character for maximum security
                crypted+=codecs.encode(c,'rot13')
        else:
            raise ValueError
                
        elif c in digitmapping:
          crypted+=digitmapping[c]
        else:
            raise ValueError
    return crypted

def decode(s):
    return encode(s)

