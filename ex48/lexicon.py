
lexicon = {
    'north': 'direction',
    'south': 'direction',
    'east': 'direction',
    'go': 'verb',
    'kill': 'verb',
    'eat': 'verb',
    'the': 'stop',
    'in': 'stop',
    'of': 'stop',
    'bear': 'noun',
    'princess': 'noun',
    '1234': 'number',
    3: 'number',
    91234: 'number'
    }

#!!! Trqbva da namerq na4in da convertiram 4isalta
#v1zmojno re6enie e :
'''
d = {'1':'cyka' , '2':'blyat'}
d = {int(k):str(v) for k,v in d.items()}
>>> d
{1: 'cyka', 2: 'blyat'}
'''
    

def scan(sentence):
    #trqbva da mu se dade argument (north) ot test-a
    #iska stoinosti ot nqkak1v dict(moje bi result ?)
    #i value-tata v dicta sa tuples

    words = sentence.split()
    result = []
    
    for word in words:
        check_string = convert_numbers(word)
        
        if word in lexicon:
            
            check_number = convert_numbers(word)
            pair = (lexicon[word], check_number)
            result.append(pair)
				
        
        elif type(check_string) == type(1):
            
            number = convert_numbers(word)
            if number:
                
                pair = ('number' , number)
                result.append(pair)
        else:
            error_word = word
            pair = ('error', error_word)
            result.append(pair)
                
    return result
    
def convert_numbers(s):
    try:
        return int(s)
    except ValueError:
        return s
        
#s kopiran ot Zed scan funkciq e lesno da se dov1r6i
#samo trqbva da updatevam dict-a
#koeto e retardsko
#az sam nqma6e se da se setq za polovinata raboti





#V1PROS ZA JERI :

#KAK DA NAKARAM PROGRAMATA DA PROVERI CIFRATA V TUPLE-A NA TEST ('number', 1234)