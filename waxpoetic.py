
import random

list_nouns = ['fossil','horse','aardvark','judge','chef','mango','extrovert','gorilla']
list_verbs = ['kicks','jingles','bounces','slurps', 'meows','explodes','curdles']
list_adj = ['furry','balding','incredulous','fragrant','exuberant','glistening']
list_prep = ['against','after','into','beneath','upon','for','in','like','over','within']
list_adv = ['curiously','extravagantly','tantalizingly','furiously','sensuously']

random_noun = random.choices(list_nouns, k = 3)
random_verbs = random.choices(list_verbs, k = 3)
random_adj = random.choices(list_adj, k = 3)
random_prep = random.choices(list_prep, k = 2)
random_adv = random.choice(list_adv)

noun1, noun2, noun3 = random_noun
verb1, verb2, verb3 = random_verbs
adj1, adj2, adj3 = random_adj
prep1, prep2 = random_prep
adv1 = random_adv

vowel = ['a','e','i','o','u']
if adj1[0] in vowel:
    print(f' An {adj1} {noun1}')
    print('')
    print(f'''An {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2} {adv1},
      the {noun1} {verb2} the {noun2} {verb3} {prep2} a {adj3} {noun3} )''')

else:
    print(f' A {adj1} {noun1}')
    print('')
    print(f'''A {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2} {adv1},
the {noun1} {verb2} the {noun2} {verb3} {prep2} a {adj3} {noun3} ''')
