def extract_language(locale):          
    return locale.split('_')[0]

def extract_region(locale):
    return locale.split('.')[0].split('_')[1]

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

    return iso_lang_dict.get(iso_code, 'Language not found')

def local_greet(locale):
    iso_dialect_dict = {
        "zh": {'CN' : "Nǐ hǎo ma!",      # Mandarin Chinese
               'TW' : "Nǐ hǎo!"},        # Mandarin Taiwan
        "es": {'MX' : "Beunos Dias!",    # Spanish Mexico
               'ES' : "Hola!"},          # Spanish Spain
        
        "en": {'AU' : "G'Day!",         # English Australia
               'CA' : "Hello there!",   # English Canada
               'GB' : "Hello!",          # English Great Britain
               'US' : "Hi!"},           # English USA
                                       
        "ar": {'EG' : "As-salamu alaykum!",   # Arabic Egypt
               'SA' : "As-salamu alaykum!"},  # Arabic Saudi Arabia
                                       
        "pt": {'BR' : 'Oi!',            # Portugese Brazil
               'PT' : "Olá!"},           # Portugese Portugal
        "fr": {'CA' : "Salut!",         # French Canada      
               'FR' : "Bonjour!"},       # French France
    }
    
    iso_code = extract_language(locale)
    country_code = extract_region(locale)

    if iso_code in iso_dialect_dict and country_code in iso_dialect_dict[iso_code]:
        greeting = iso_dialect_dict.get(iso_code).get(country_code, 'Country Not Found')
    else:
        greeting = greet(iso_code)
    
    return greeting


print(local_greet('en_US.UTF-8'))       # Hi!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # G'day!
print(local_greet('fr_FR.UTF-8'))       # Bonjour!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Bonjour!
print(local_greet('vi_VN'))             # Xin Chao
print(local_greet('vn_DH'))             # Language not found
