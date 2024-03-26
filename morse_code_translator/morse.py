import sys
nazwa_pliku=sys.argv[1]
def main(plik_wej):
    with open(plik_wej) as plik:
        dane=[linia.upper().rstrip() for linia in plik]
    gotowe_dane=[]
    for linia in dane:
        gotowa_linia=''.join(i for i in linia if i.isalpha() or i.isspace())
        if gotowa_linia.isspace()==False:
            gotowe_dane.append(gotowa_linia.rstrip())
    morse= {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.',
            'G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..',
            'M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.',
            'S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-',
            'Y':'-.--','Z':'--..'}
    odp=[]
    for linia in gotowe_dane:
        ost_linia=''
        for i in range(len(linia)):
            if ord(linia[i])>=65 and ord(linia[i])<=90:
                ost_linia+=morse[linia[i]]
            elif linia[i]==' ' and linia[i-1]!=' ':
                ost_linia+='/'
            else:
                continue
            ost_linia+=' '
        odp.append(ost_linia)
    for el in odp:
        print(el)
main(nazwa_pliku)