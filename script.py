def map(forms_range = range(0xfe80, 0xfefd), accents_range = range(0x064b, 0x0653), map_start_address = 0xe000):
    """maps each form + accent combination to an address in the unicode.
    By defualt, it maps to the Private Use Area which starts at address 0xE000
    the forms (Huruuf) used start from 0xfe80 to 0xfefc of the unicode
    and the accents (Tashkeel/Harakaat) used are from 0x064b to 0x0652 of the unicode
    which pretty much covers all common glyphs found in regular texts"""

    forms = list(forms_range)
    accents = list(accents_range)


    map = {}
    for form in forms:
        for accent in accents:
            form_offset = (form % forms[0]) * 8
            accent_offset = accent % accents[0]
            newGlyphAddress = map_start_address + form_offset + accent_offset
            map[(form, accent)] = newGlyphAddress
    return map

mapping = map()

font = fontforge.fonts()[0]
for key in mapping:
    newGlyphAddress = mapping[key]
    font.createChar(newGlyphAddress)
    font[newGlyphAddress].user_decomp = chr(key[0]) + chr(key[1])
    font[newGlyphAddress].build()
    
print("Finished")
