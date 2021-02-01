#coding: utf-8 -*-
import readline #aby raw_input mohol zobrat vacsi text.

text = raw_input('Input Greek Text: ')

MyList = [
('ai','e'),('ou','u'),('ei','i'),('nt','d')
,('oi','i'),('eí','í'),('oú','ú'),('mp','b')
,('oí','í'),('aí','é'),('y','i'),('ý','í')
,('x','ks'),('Y','I'),('Nt','D'),('Oí','Í')
,('Oi','I'),('nk','g'),('Nk','G'),('Eí','Í')
,('ge','ye'),('Ge','Ye'),('gi','yi'),('gé','yé')
,('Gi','Yi'),('gí','yí'),('dh','nth'),('prí','proí')
,('edh','enth'),(' zí ',' zoí '),('X','Ks')
,('Dimítris: ','\n\nDimítris: \n'),('Mariléna: ','\n\nMarilú: \n')]

for k,v in MyList:
    text = text.replace(k, v)

print ("\n\n\n"), text
