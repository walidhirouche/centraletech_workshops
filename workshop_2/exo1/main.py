# coding=utf-8
# Exercice 1.1

def info(s):
    return tuple(s.split(" "))

# Exercice 1.2

def mdpValide(mdp):
    return len(mdp)>=8 and set(list(mdp)).intersection(set(list("!@#$%^&*"))) and set(list(mdp)).intersection(set(list(map(str,range(0,10))))) and mdp.lower()!=mdp and mdp.upper()!=mdp

# Exercice 1.3

def remplace(s,w1,w2):
    #return w2.join(list(s.split(w1)))
    return s.replace(w1,w2)

# Exercice 1.4

def freq(s):
    return {chr(i):s.lower().count(chr(i)) for i in range(ord("a"),ord("z")+1) if s.lower().count(chr(i))!=0}

# Exercice 1.5

def acronym(s):
    return " ".join([w[0].upper() for w in s.split(" ")])

# Exercice 1.6

def classifie(s,p,n):
    t = ""
    l = list("&#.!/;,?=+@")
    for c in s:
        if not(c in l):
            t += c
    return "Positif" if set(t.split(" ")).intersection(set(p)) else "Negatif" if set(t.split(" ")).intersection(set(n)) else "Neutre"

def classificateur_sentiment(c,p,n):
    return [classifie(s.lower(),p,n) for s in c]

# Exercice 2.1

def freqMots(s):
    return {w:s.split(" ").count(w) for w in s.split(" ")}

# Exercice 2.2

def fusion(d1,d2):
    K = list(set(d1.keys()).union(set(d2.keys())))
    return {k:(d1[k]+d2[k] if k in d1.keys() and k in d2.keys() else d1[k] if not k in d2.keys() else d2[k] if not k in d1.keys() else 0) for k in K}

# Exercice 2.3

def imb(d):
    l = []
    for k in d.keys():
        if not isinstance(d[k],dict):
            l.append((k,d[k]))
        else:
            l.append((k,imb(d[k])))
    return l

# Exercice 2.4

def fusImb(d1,d2):
    K = list(set(d1.keys()).intersection(set(d2.keys())))
    K1, K2 = list(set(d1.keys()).difference(set(d2.keys()))), list(set(d2.keys()).difference(set(d1.keys())))
    d = {k:d1[k] for k in K1}
    d.update({k:d2[k] for k in K2})
    for k in K:
        if isinstance(d1[k],dict) and isinstance(d2[k],dict):
            d[k] = fusImb(d1[k],d2[k])
        else:
            d[k] = d1[k]+d2[k]
    return d

# Exercice 2.5

def sortVal(d):
    return {k:d[k] for k in sorted(d.keys(),key=lambda x : d[x])}

print(sortVal({'a': 5, 'b': 2, 'c': 8, 'd': 1}))