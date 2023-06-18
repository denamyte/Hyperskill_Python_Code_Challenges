import nltk

sent = ['The', 'horse', 'that', 'was', 'raced', 'past', 'the', 'barn', 'fell', 'down', '.']

seq = nltk.pos_tag(sent)
pred = lambda x: x[0] == 'raced'
tpl = next(filter(pred, seq))
print(tpl[1])
