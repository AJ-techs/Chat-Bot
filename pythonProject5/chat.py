from nltk.chat.util import Chat, reflections


pairs = [
        ['my name is (.*)', ['hi %1']],
        ['(greetings|hi|hello|hey|holla|hola)', ['hey there']],
        ['(hi how is it going)', ['Good']],
        ['(how  are you doing?)', ['fine ,and you?']],
        ['(hi ,nice to meet you)', ['nice to meet you too']],
        ['(good morning)', ['good morning']],
        ['(good afternoon)', ['Good afternoon']],
        ['(good night)', ['Good Night']],
        ['(exit)',["exiting..."]]


        ]
reflections
chat=Chat(pairs , reflections)
chat.converse()

