#coding: utf-8 -*-

GreekText = open("GreekText.txt", "r")

InternalText = GreekText.read()

MyList = [

#Prep υ > Φ
('Αυ','Αφ'),('αυ','αφ'),('Ευ','εφ'),('ευ','εφ'),('Ηυ','Ηφ'),('ηυ','ηφ'),
('Aύ','Άφ'),('αύ','άφ'),('Εύ','Έφ'),('εύ','έφ'),('Ηύ','Ήφ'),('ηύ','ήφ'),

#Prep υ > u
('Ου','Ou'),('ου','ou'),
('Ού','Oú'),('ού','oú'),

#Greek to latin
('Α','A'),('α','a'),('Β','V'),('β','v'),('Γ','G'),('γ','g'),('Δ','D'),('δ','d'),
('Ε','E'),('ε','e'),('Ζ','Z'),('ζ','z'),('Η','I'),('η','i'),('Θ','Th'),('θ','th'),
('Ι','I'),('ι','i'),('Κ','K'),('κ','k'),('Λ','L'),('λ','l'),('Μ','M'),('μ','m'),
('Ν','N'),('ν','n'),('Ξ','Ks'),('ξ','ks'),('Ο','O'),('ο','o'),('Π','P'),('π','p'),
('Ρ','R'),('ρ','r'),('Σ','S'),('σ','s'),('ς','s'),('Τ','T'),('τ','t'),('Υ','I'),
('υ','i'),('Φ','F'),('φ','f'),('Χ','Ch'),('χ','ch'),('Ψ','Ps'),('ψ','ps'),
('Ω','o'),('ω','o'),

#Accented vowels
('Ά','Á'),('Ή','Í'),('Έ','É'),('Ί','Í'),('Ό','Ó'),('Ύ','Ý'),('Ώ','Ó'),
('ά','á'),('ή','í'),('έ','é'),('ί','í'),('ό','ó'),('ύ','ý'),('ώ','ó'),

#post conversion clean-up
('ai','e'),('ou','u'),('ei','i'),('nt','d')
,('oi','i'),('eí','í'),('oú','ú'),('mp','b')
,('oí','í'),('aí','é'),('y','i'),('ý','í')
,('x','ks'),('Y','I'),('Nt','D'),('Oí','Í')
,('Oi','I'),('nk','g'),('Nk','G'),('Eí','Í')
,('ge','ye'),('Ge','Ye'),('gi','yi'),('gé','yé')
,('Gi','Yi'),('gí','yí'),('dh','nth'),('prí','proí')
,('edh','enth'),(' zí ',' zoí '),('X','Ks')
,('Mariléna','Marilú')]

for k,v in MyList:
    InternalText = InternalText.replace(k, v)

GreekText.close()

#Write GreekText.txt file with transliterated Greek. #Need to close and open
#GreekText again.

WriteFile = open("GreekText.txt", "w")
WriteFile.write(InternalText)
WriteFile.close()
