import datetime

teraz = datetime.datetime.now()
peciatka = teraz.timestamp()
print(f'Teraz je {teraz}, čomu zodpovedá pečiatka {peciatka}')

peciatka2 = 1234567890
moment = datetime.datetime.fromtimestamp(peciatka2)
print(f'Pečiatke {peciatka2} zodpovedá čas a dátum {moment}')



import datetime

teraz = datetime.datetime.now() # Aktuálny čas a dátum
posun1 = datetime.timedelta(weeks = 3) # Rozdiel 3 týždne

# Rozdiel cca 7 rokov - problem je, ako pristupovat k priestupnym rokom
#  v ramci intervalu 7 rokov mozu byt 1 alebo 2
#  Ci ich budeme brat do uvahy alebo nie, zavisi od ucelu prorgamu
#  Podobny problem vyvstava pri posune o mesiace - kolko je 1 mesiac?
# Parameter years alebo months tu neexistuje,
#  najdlhsia jednotka pre timedelta je weeks
posun2 = datetime.timedelta(days = 7 * 365)

# Rozdiel 1 rok, 2 tyzdne a 3 dni
posun3 = datetime.timedelta(weeks = 2, days = 1 * 365 + 3) 

print(f'O 3 týždne bude {teraz + posun1}')
print(f'Pred {posun1} bol {teraz - posun1}')

print(f'O 7 rokov bude {teraz + posun2}')
print(f'Pred {posun2} bol {teraz - posun2}')

print(f'O 1 rok, 2 týždne a 3 dni bude {teraz + posun3}')
print(f'Bude to nasledujúci deň v týždni: {(teraz + posun3).strftime("%A")}')