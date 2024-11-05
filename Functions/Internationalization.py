# def greet(iso_code):
#     match iso_code.casefold():
#         case "zh":
#             return "Nǐ hǎo"        # Mandarin Chinese
#         case "es":
#             return "Hola"          # Spanish
#         case "en":
#             return "Hello"         # English
#         case "hi":
#             return "Namaste"       # Hindi
#         case "ar":
#             return "Marhaban"      # Arabic
#         case "bn":
#             return "Nomoshkar"     # Bengali
#         case "pt":
#             return "Olá"           # Portuguese
#         case "ru":
#             return "Zdravstvuyte"  # Russian
#         case "ja":
#             return "Konnichiwa"    # Japanese
#         case "pa":
#             return "Sat sri akaal" # Western Punjabi
#         case "mr":
#             return "Namaskar"      # Marathi
#         case "te":
#             return "Namaskaram"    # Telugu
#         case "tr":
#             return "Merhaba"       # Turkish
#         case "ko":
#             return "Annyeong"      # Korean
#         case "fr":
#             return "Bonjour"       # French
#         case "de":
#             return "Hallo"         # German
#         case "vi":
#             return "Xin chào"      # Vietnamese
#         case "ta":
#             return "Vanakkam"      # Tamil
#         case "ur":
#             return "Assalam-o-Alaikum" # Urdu
#         case "it":
#             return "Ciao"          # Italian
#         case _:
#             return "No data for ISO code"
        
# iso = input('Enter Language ISO code: ')

# print(greet(iso))

# Solution using a dictionary:
def greet(iso_code):
    iso_lang_dict = {
        "zh": "Nǐ hǎo",                # Mandarin Chinese
        "es": "Hola",                  # Spanish
        "en": "Hello",                 # English
        "hi": "Namaste",               # Hindi
        "ar": "Marhaban",              # Arabic
        "bn": "Nomoshkar",             # Bengali
        "pt": "Olá",                   # Portuguese
        "ru": "Zdravstvuyte",          # Russian
        "ja": "Konnichiwa",            # Japanese
        "pa": "Sat sri akaal",         # Western Punjabi
        "mr": "Namaskar",              # Marathi
        "te": "Namaskaram",            # Telugu
        "tr": "Merhaba",               # Turkish
        "ko": "Annyeong",              # Korean
        "fr": "Bonjour",               # French
        "de": "Hallo",                 # German
        "vi": "Xin chào",              # Vietnamese
        "ta": "Vanakkam",              # Tamil
        "ur": "Assalam-o-Alaikum",     # Urdu
        "it": "Ciao"                   # Italian
    }

    return iso_lang_dict.get(iso_code, 'ISO code Not Found')

iso = input('Enter Language ISO code: ').casefold()

print(greet(iso))

