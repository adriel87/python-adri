import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

listed = re.split(' ',re.sub('.',' ', paragraph))

unique_words = list(set(listed))

the_count = sorted(list(map(lambda word: (len(re.findall(word,paragraph)), word) , unique_words)), key=lambda tup:tup[0],reverse=True) 



print(re.finditer('.', paragraph))

(6, 'love'), 
(6, 'love.'), 
(5, 'you'), 
(4, 'an'), 
(3, 'can'), 
(3, 'I'), 
(2, 'else'), 
(2, 'teaching'), 
(2, 'do'), 
(2, 'not'), 
(2, 'teaching.'), 
(2, 'what'), 
(1, 'something'), 
(1, 'application'), 
(1, 'If'), 
(1, 'give'), 
(1, 'the'), 
(1, 'Python'), 
(1, 'all'), 
(1, 'if'), 
(1, 'develop'), 
(1, 'capabilities'), 
(1, 'which'), 
(1, 'to')