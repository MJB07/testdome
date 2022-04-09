# Importing necessary packages
import spacy
from langdetect import detect

# Iterating over language code and identify the correct 
# language based on the given input string
nlp={}    
for lang in ['ca','zh','da','nl','en','fr','de','el','it',
        'ja','lt','mk','xx','nb','pl','pt','ro','ru','es']:
    if lang == 'en':
        nlp[lang]=spacy.load(lang + '_core_web_sm')
    elif lang == 'xx':
        nlp[lang]=spacy.load(lang + '_ent_wiki_sm')
    else: 
        nlp[lang]=spacy.load(lang + '_core_news_sm')

# This main funtion will detect correct language and 
# an extracts the entities
def main(text):
     lang = detect(text)
     try:
         doc =nlp[lang]
     except KeyError:
         return Exception(lang + " model is not loaded")
     return [({'text':str(x), 'type':x.label_, 
            'start_pos':x.start_char, 'end_pos':x.end_char})
             for x in doc(str(text)).ents]


if __name__=="__main__":
    input_text = """Serum Institute of India has decided
    to revise the price of Covishield vaccine for private
    hospitals from Rs.600 to Rs 225 per dose, says Adar 
    Poonawalla, CEO, Serum Institute of India"""
    
    input_text2 = """Das Serum Institute of India hat 
    beschlossen, den Preis des Covishield-Impfstoffs 
    für private Krankenhäuser von 600 Rs. auf 225 Rs. pro 
    Dosis zu erhöhen, sagt Adar Poonawalla, CEO 
    des Serum Institute of India"""

    """
    This will generate the output - a list of each
    entity in Python Dict with fields text, type,
    star_pos, end_pos
    """
    print(main(input_text))
