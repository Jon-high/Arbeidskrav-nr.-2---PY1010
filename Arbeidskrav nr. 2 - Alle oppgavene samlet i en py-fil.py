# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:27:40 2024

@author: Jon-k
"""
#%%

#Oppgave nr. 1: 
 
#Du skal her lage et program som skal starter med alder = int(input('Hvilket år er du født? ') ) 
#Programmet skal så regne ut hvor gammel personen blir nå i løpet av år 2024 og skrive svaret til skjerm med passende tekst.

    #Svar på nr.1: 
        
#Spør brukeren om å oppgi fødselsår:
fodselsar = int(input('Hvilket år er du født? '))

#Definer nåværende/inneværende år:
naavaerende_ar = 2024

#Regn ut alderen mtp. innput av årstall ift. innværende år:
alder = naavaerende_ar - fodselsar

#Skriv ut resultatet med en passende tekst:
print(f'I løpet av året 2024 vil du bli {alder} år gammel.')


#%%

#Oppgave nr. 2: Det skal arrangeres en klassefest og man antar at hver elev spiser 1/4 pizza. 
#Lag et program som tar inn antall elever fra konsollen ved antall_elever = int(input('Skriv inn antall elever:' )) 
#Programmet skal så regne ut hvor mange pizzaer som skal handles inn til festen og skrive svaret til skjerm. 
#Merk, man kan ikke kjøpe 4 og en kvart pizza på butikken (man må da kjøpe 5). 
#Hint1: Gir programmet ditt et fornuftig svar hvis det f.eks er 21 elever i klassen? 
#Hint2: Det er ikke vanlig å si/skrive: ‘Det må handles inn 6.0 pizzaer til festen’. 
#Hvordan kan sikre at antall pizzaer skrives ut som et heltall (ikke desimaltall)?

    #Svar på nr. 2: 

#Importerer bibliotek:
import math

#Her må brukeren oppgi forventet antall elever som skal ha pizza:
antall_elever = int(input('Skriv inn antall elever: '))

#Basert på antall forventa personer beregnes det ut antall hele pizzaer som trengs til selskapet:
antall_pizzaer = math.ceil(antall_elever * 0.25)

#Skriv ut resultatet med passende tekst:
print(f'Det må handles inn {antall_pizzaer} pizzaer til festen.')


#%%

#Oppgave nr. 3: 
#Lag et program med en funksjon som regner om fra grader til radianer. 
#Programmet skal starte med: import numpy as np 
#v_grad = float(input('Skriv inn gradtallet:' )) 
#Radiantallet til vinkelen regnes så ut ved følgende formel: v_rad = v_grad*np.pi/180 
#Resultatet v_rad skrives til skjerm med passende tekst og verdi. 
#Merk: np.pi er en ferdiglaget funksjon som gir verdien 3.1415....

    #Svar på nr. 3: 
    
import numpy as np

#Vi lager en funksjon for å konvertere grader om til radianer:
def grader_til_radianer(v_grad):
    v_rad = v_grad * np.pi / 180
    return v_rad

#Ta inn gradtallet fra brukeren:
v_grad = float(input('Skriv inn gradtallet: '))

#Regn ut radianer ved hjelp av funksjonen
v_rad = grader_til_radianer(v_grad)

#Skriv ut resultatet med passende tekst:
print(f'Vinkelen på {v_grad} grader er {v_rad} radianer.')


#%%

#Oppgave nr. 4 - a:
# Opprett en dictionary som gitt under. Dictionaryen har ulike land som nøkkel (Keys) 
#og gir info om hovedstaden i landet og antall innbyggere i mill. i hovedstaden.

    #Svar på a:

#Land, hovedstad og innbyggertall i million-skala:
land_info = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]}

#Skriv ut dictionaryen
for land, info in land_info.items():
    hovedstad, innbyggere = info
    print(f"Hovedstaden i {land} er {hovedstad} med {innbyggere} millioner innbyggere.")
#%%

#Oppgave nr. 4 - b:
# Lag et program som ber brukeren skrive inn et land (eksempelvis England). 
#Programmet skal på bakgrunn av dette skrive ut følgende setning: 
#London er hovedstaden i England og det er 8.982 mill. innbyggere i London 

    #Svar på b:
    
    
#Opprett dictionaryen med land, hovedstad og antall innbyggere
land_info = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
}

#Vi ver brukeren om å skrive inn et land:
land = input('Skriv inn et land: ')

#Vi ser om landet er tilgjengelig i vår dictionaryen:
if land in land_info:
    hovedstad, innbyggere = land_info[land]
    print(f'{hovedstad} er hovedstaden i {land} og det er {innbyggere} mill. innbyggere i {hovedstad}.')
else:
    print(f'Beklager, informasjon om {land} er ikke tilgjengelig.')
    
#%%

#oppgave nr. 4 - c: 
#Lag et program som ber brukeren skrive inn info om et nytt land (altså et land som ikke allerede finnes i dictionaryen data). 
#Videre skal brukeren oppgi hovedstad og antall innbyggere for det «nye» landet. Programmet skal så utvide/oppdatere 
#dictionaryen med den nye informasjonen. Dictionaryen data skrives så til skjerm. 

    #Svar på c:
    
#Initial dictionary med noen land, hovedstad og antall innbyggere:
land_info = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
}

#Vi ber om at brukeren skrive inn informasjonen på; nytt land, hovedstad og hvor mange innbyggere det er:
nytt_land = input('Skriv inn navnet på et nytt land: ')
hovedstad = input(f'Skriv inn hovedstaden i {nytt_land}: ')
innbyggere = float(input(f'Skriv inn antall innbyggere (i millioner) i {hovedstad}: '))

#Oppdater dictionaryen med den nye informasjonen:
land_info[nytt_land] = [hovedstad, innbyggere]

#Skriv ut den oppdaterte dictionaryen:
print("\nOppdatert informasjon om land:")
for land, info in land_info.items():
    hovedstad, antall_innbyggere = info
    print(f"Hovedstaden i {land} er {hovedstad} med {antall_innbyggere} millioner innbyggere.")
#%%
#Oppgaver nr. 5: 
    
#Lag et program med en funksjon som tar a og b som inn-argumenter og som så 
#regner ut arealet og «ytre» omkrets til en figur satt sammen av en rettvinklet trekant og en halvsirkel, 
#se figuren i oppg.5. Med «ytre» omkrets menes samlet lengde av de sorte strekene. 
#Funksjonen skal returnere arealet og «ytre» omkrets, som så skrives til skjerm med passende tekst.

    #Svar på nr. 5:

#Importerer bibliotek:
import math

def beregn_figur(a, b):
 #Arealberegning for trekant og halvsirkel:
    areal_trekant = (a * b) / 2 #Areal på trekant: grunnlinja -a- x høyden -b-  : 2.
    radius = a / 2 #Diamenter til sirkelen delt på 2 = radius til senter av sirkel.
    areal_halvsirkel = (math.pi * (radius ** 2)) / 2 #Utregning av arealet til en halvirkel, ikke en helsirkel.
    totalt_areal = areal_trekant + areal_halvsirkel #Vi begger sammen arealet for trekanten og arealet for halvsirkelen.

#Omkretsberegning for trekant og halvsirkel:
    hypotenus = math.sqrt(a**2 + b**2) #Vi beregner hypotenusen med alebra: ** = eksponenten -> 2 aka. potensregning. math.sqrt -> kvadratroten.
    omkrets_trekant = a + b + hypotenus #Vi beregner omkretsen til hele trekanten!
    omkrets_halvsirkel = (math.pi * a) / 2 #Vi beregner omkretsen til halvsirkelen. 
    ytre_omkrets = b + hypotenus + omkrets_halvsirkel # Vi må få vekk -a- i omrketsen på trekanten/diamenteren til sirkelen, da denne ikke er den del av de ytre strekkene. 
#Vi skal legge sammen følgende lengder for å finne omkretsen: b + hypotenus + bua lengde på halvsirkel = omkretsen!
    return totalt_areal, ytre_omkrets # Beregner kun den ytre omkrets av figurene når de er slått sammne til en stor figur. 

#Hovedprogram:
def main():
    a = float(input("Skriv inn lengden a: "))
    b = float(input("Skriv inn lengden b: "))
    areal, omkrets = beregn_figur(a, b)
    print(f"Arealet av figuren er {areal:.2f} kvadratmeter.")
    print(f"Den ytre omkretsen av figuren er {omkrets:.2f} meter.")

if __name__ == "__main__":
    main()


#%%

#Oppgave nr. 6:
    
#Skriv en kode som plotter funksjonen 𝑓(𝑥) = −𝑥2 − 5, for x på intervallet [-10,10]. 
#Hint: np.linspace(-10, 10, 200) gir en array med 200 punkter jevnt fordelt på intervallet [-10,10].

    #Svar på nr. 6:

#Importerer bibliotek:
import numpy as np
import matplotlib.pyplot as plt

#Definer funksjonen f(x):
def f(x):
    return -x**2 - 5

#Generer 200 punkter jevnt fordelt på intervallet [-10, 10]:
x = np.linspace(-10, 10, 200)
y = f(x)

#Plot funksjonen:
plt.plot(x, y, label='$f(x) = -x^2 - 5$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot av funksjonen $f(x) = -x^2 - 5$')
plt.legend()
plt.grid(True)
plt.show()

#%%

#Takk for oppgavene!
#Mvh. Jon-K












