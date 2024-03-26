def find(string,text):
    if len(string)==0 or len(text)==0:
        return []
    if len(string)>len(text):
        return []
    ans=[]
    q=20029
    alfa=ile_unikalnych(string)
    w=hashuj(string,alfa,q)
    okno=len(string)
    cand=hashuj(text[0:okno],alfa,q)   
    len_tekst=len(text)
    alfa_one=(alfa**(okno-1))
    i=0
    while(True):
        last=i
        if cand==w:
            if text[i:i+okno]==string:
                ans.append(i)
                i+=okno-1
        i+=1
        if i<=len_tekst-okno:
            for j in range(i-last):
                cand=((cand-(ord(text[last+j])-80)*alfa_one)*alfa+ord(text[last+j+okno])-80)%q
        else:
            break
    return(ans)

def hashuj(str,alfa,q):
    hasz=0
    l=len(str)
    for i in range(l):
        hasz+=(ord(str[i])-80)*(alfa**(l-(i+1)))
    return hasz%q

def ile_unikalnych(str):
    ile=set([])
    for i in range(len(str)):
        ile.add(str[i])
    return len(ile)

if __name__ == '__main__':
    text = "ALA MA MAŁEGO KOTA. MAŁEGO"
    string = "MAŁEGO"
    print(find(string, text))

