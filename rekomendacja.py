#  Wzorowane na przykładzie Rona Zacharskiego
#
from math import sqrt
from numpy import corrcoef

users = {
        "Ania": 
            {"Blues Traveler": 1.,
            "Broken Bells": 1.5,
            "Norah Jones": 2,
            "Deadmau5": 2.5,
            "Phoenix": 3.0,
            "Slightly Stoopid": .5,
            "The Strokes": 0.0,
            "Vampire Weekend": 2.0},
         "Bonia":
            {"Blues Traveler": 4.0,
            "Broken Bells": 4.5, 
            "Norah Jones": 5.0,
            "Deadmau5": 5.5, 
            "Phoenix": 6.0, 
            "Slightly Stoopid": 3.5, 
            "The Strokes": 2.0,
            "Vampire Weekend": 5.0}
        }

def manhattan(rating1, rating2):
    
    """Oblicz odległość w metryce taksówkowej między dwoma  zbiorami ocen
       danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
       Zwróć -1, gdy zbiory nie mają… wspólnych elementów"""
       
    # TODO: wpisz kod
    klucze1 = users[rating1].keys()
    klucze2 = users[rating2].keys()
    odleglosc = 0
    udaloSiePorownac = False

    for klucz in klucze1:
        if klucz in klucze2:
            udaloSiePorownac = True
            odleglosc = odleglosc + abs(users[rating2][klucz] - users[rating1][klucz])

    if (udaloSiePorownac==True):
        return odleglosc
    else:
        return -1

def pearson(rating1, rating2):
    korelacja=0
    x=0
    y=0
    sum_xy=0
    sum_x=0
    sum_y=0
    sum_x2=0
    sum_y2=0
    n=0 #count of the same groups to compare
    klucze1 = users[rating1].keys()
    klucze2 = users[rating2].keys()

    for klucz1 in klucze1:
        for klucz2 in klucze2:
            x = users[rating1][klucz1]
            y = users[rating2][klucz2]
            if klucz1 == klucz2:
                n=n+1
                sum_xy=sum_xy+(x*y)
                sum_x=sum_x+x
                sum_y=sum_y+y
                sum_x2=sum_x2+x**2
                sum_y2=sum_y2+y**2

    korelacja = (sum_xy-((sum_x*sum_y)/n))/(sqrt(sum_x2-(sum_x**2)/n)*sqrt(sum_y2-(sum_y**2)/n))
    return korelacja

def pearsonNumpy(rating1, rating2):
    
    korelacja=0

    klucze1 = users[rating1].keys()
    klucze2 = users[rating2].keys()
    a=[]
    b=[]
    for klucz1 in klucze1:
        for klucz2 in klucze2:
            if klucz1 == klucz2:
                a.append(users[rating1][klucz1])
                b.append(users[rating2][klucz2])
    korelacja = corrcoef([a,b])[1,0]
    return korelacja

print 'Odleglosc miedzy uzytkownikami Ania i Bonia przy uzyciu funkcji manhattan wynosi: ', manhattan("Ania","Bonia")
print 'Odleglosc miedzy uzytkownikami Ania i Bonia przy uzyciu funkcji pearson wynosi: ', pearson("Ania","Bonia")
print 'Odleglosc miedzy uzytkownikami Ania i Bonia przy uzyciu funkcji pearsonNumpy wynosi: ',pearsonNumpy("Ania","Bonia")

