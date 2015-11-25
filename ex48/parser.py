class ParserError(Exception):
	pass

class Sentence(object):
	
    def __init__(self, sentence_value):
        self.sentence_value = sentence_value
        self.list_result = []
        
        for i in sentence_value[::1]:
            if i[0] == 'noun':
                self.list_result.append(i[1])
            elif i[0] == 'verb':
                self.list_result.append(i[1])
            elif i[0] == 'direction':
                self.list_result.append(i[1])
            elif i[0] == 'number':
                self.list_result.append(i[1])
            else:
                pass
            
    		
    def to_tuple(self):
		return tuple(self.list_result)

def peek(word_list):
	
	if word_list:
		word = word_list[0]
		return word[0]
	else:
		return None

def match(word_list, expecting):
			
	if word_list:
		word = word_list.pop(0)
		
		if word[0] == expecting:  
			return word
		else:
			return None
	else:
		return None
	
def skip(word_list, word_type):
	
	while peek(word_list) == word_type:
	
		match(word_list, word_type)
		
def parse_verb(word_list):
	
	skip(word_list, 'stop')
	
	if peek(word_list) == 'verb':
		return match(word_list, 'verb')
	else:
		raise ParserError("Expected a verb next.")
		
def parse_object(word_list):

	skip(word_list, 'stop')
	next_word = peek(word_list)
	
	if next_word == 'noun':
		return match(word_list, 'noun')
	elif next_word == 'direction':
		return match(word_list, 'direction')
	
	#elif next_word == 'number':
		#return parse_numbers(word_list)
	
	else:
		raise ParserError("Expected a NOUN or a direction next.")

def parse_subject(word_list):
	
	skip(word_list, 'stop')
	next_word = peek(word_list)
	
	if next_word == 'noun':
		return match(word_list, 'noun')
	elif next_word == 'verb':
		return('noun', 'player')
	else:
		raise ParserError("Expected a VERB next.")
		

def parse_numbers(word_list):
	
	skip(word_list, 'stop')
	next_word = peek(word_list)
	
	if next_word == 'number':
		return match(word_list, 'number')
	else:
		raise ParserError("Expected a NUMBER next.")

def parse_error(word_list):
	
	skip(word_list, 'stop')
	next_word = peek(word_list)
	
	if next_word == 'error':
		return match(word_list, 'error')
	else:
		raise ParserError("Expected an ERROR next.")
	
def peek_sentence_kind(word_list):
	
	if word_list:
		word = word_list[0]
		return word
	else:
		return None
		
def parse_sentence(word_list):
    
    sentence_value = []
    
    if word_list:
		
		for i in word_list[::1]:
			
			#word_chooser = peek_sentence_kind(i)
			
			if i[0] == 'noun':
				subject = parse_subject(word_list)
				sentence_value.append(subject)
				
			if i[0] == 'verb':
				verb = parse_verb(word_list)
				sentence_value.append(verb)
				
			if i[0] == 'direction':
				obj = parse_object(word_list)
				sentence_value.append(obj)
			
			if i[0] == 'number':
				num = parse_numbers(word_list)
				sentence_value.append(num)
			if i[0] == 'error':
				error = parse_error(word_list)
				sentence_value.append(error)  #moje da skipnem,za6toto
			else:							  #Sentence otseive errorite w/e sweg			
				pass
	
	#__init__(self, subject=None, verb=None, obj=None, num=None)
	#return Sentence(subject, verb, obj, num)
    return Sentence(sentence_value)
	
	

	

	
#v1zmojno li e da se returne Classa Sentence s1s argumentite ot parse_sentence
#taka 4e stoinostta da im se izpolzva za assert_equal
#a ne prosto kato id na pametta , v koqto se namira value-to

