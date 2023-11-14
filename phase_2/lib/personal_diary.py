def make_snippet(instring):
    words = instring.split()
    if len(words) > 5:
        snippet = ' '.join(words[:5]) + '...'
    else:
        snippet = instring
    return snippet

def count_words(instring):
    return len(instring.split()) 

def estimate_reading_time(instring):
    return round(len(instring.split()) / 200, 1)

def check_sentence_grammar(sentence):
    return sentence[0].isupper() and sentence[-1] in '.!?'

def check_contains_todo(text):
    if type(text) is not str:
        raise Exception('Input must be string')
    else:
        return '#TODO' in text
    
