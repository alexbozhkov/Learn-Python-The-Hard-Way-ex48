from nose.tools import *
from ex48 import parser, lexicon

def test_Sentence():
	word_list = lexicon.scan("bear go north 1")
	foo = parser.Sentence(word_list)
	assert_equal(foo.to_tuple(), ('bear','go' , 'north', 1))


def test_peek(): #word_list[('noun', 'princess')]
	word_list = lexicon.scan('princess')
	test = parser.peek(word_list)
	assert_equal(test, 'noun')
	assert_equal(None, None)

def test_match(): #word_list[('noun', 'bear')]
	
	test = parser.match([('noun', 'bear')], 'noun')
	assert_equal(test, ('noun', 'bear'))
	#da dov1r6a, ne znam za6to vinagi dava -OK na nosetests ??? 


def test_skip(): #word_list[('stop', 'the')]
	word_list = lexicon.scan('the')
	s = parser.skip(word_list, word_type='stop')
	assert_equal = (parser.skip(word_list, word_type='stop'), 'stop')
	

	#word_list = lexicon.scan('bear eat princess')
	#assert_equal(word_list, [('noun', 'bear'), ('verb', 'eat'), ('noun', 'princess')])

	
def test_parse_verb(): #word_list[('verb', 'go')]
	word_list = lexicon.scan('go')
	assert_equal(parser.parse_verb(word_list), ('verb', 'go'))
	assert_raises(parser.ParserError, parser.parse_verb, [('vverb', 'go')])
	#dava -Ok , za6toto parse_verb e v1rnal gre6ka , koeto ozna4ava 4e v nosetest e pravilno
	#ako be6e [('verb', 'go')] , assert_raises 6te6e da v1rne gre6ka v nose (ne izp1lnen)
	#(bqh slojil [('noun', 'bear')])
	
def test_parse_object():
	word_list = lexicon.scan('north')
	assert_equal(parser.parse_object(word_list), ('direction', 'north'))
	assert_raises(parser.ParserError, parser.parse_object, [('ddirection', 'north')])
	
def test_parse_subject():
	word_list = lexicon.scan('bear')
	assert_equal(parser.parse_object(word_list), ('noun', 'bear'))
	assert_raises(parser.ParserError, parser.parse_object, [('nNoun', 'bear')])
	
def test_parse_numbers():
	word_list = lexicon.scan('1')
	assert_equal(parser.parse_numbers(word_list), ('number', 1))
	assert_raises(parser.ParserError, parser.parse_numbers, [('numberr', 1)])
	
def test_parse_error():
	word_list = lexicon.scan('asdf')
	assert_equal(parser.parse_error(word_list), ('error', 'asdf'))
	assert_raises(parser.ParserError, parser.parse_error, [('Eerror', 'asdf')])
		
def test_parse_sentence():#[('noun', 'bear'), ('verb', 'eat'), ('noun', 'princess')]
	
	word_list = lexicon.scan("bear eat princess")
	test = parser.parse_sentence(word_list)
	#assert_equal(test, parser.Sentence([('noun', 'bear'), ('verb', 'eat'), ('noun', 'princess')]))
	
	#moje li da se assertva pri nali4ieto na for loop ?

	
	
	

#tova e s kombiniran test ot lexicona
'''
def test_parse_sentence():
    word_list = lexicon.scan('the bear eat door')
    s = parser.parse_sentence(word_list)
    assert_equal(s.to_tuple(), ('bear', 'eat', 1, 'door'))
    word_list = lexicon.scan('in eat door')
    s = parser.parse_sentence(word_list)
    assert_equal(s.to_tuple(), ('player', 'eat', 1, 'door'))
    word_list = lexicon.scan('north eat door')
    assert_raises(parser.ParserError, parser.parse_sentence, word_list)'''