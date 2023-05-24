def timeToSeconds(t):               #(t= "12:59:18 AM")
    h,m,s = t.split(":")            #split each number
    #print(h,m,s)

    s,tt=s.split(" ")               #Split to seperate numbers from AM or PM
    #print(s)
    #print(t)
    h=int(h)                       # H is hours 
    m=int(m)                       # M is minutes
    s=int(s)                       # S is second
    print(h,m,s,tt)                # tt is AM or PM
    


    if h == 12 and tt == "AM":
       nH = 0
    else:
        nH = h*60*60
                                # Converting hours (h), and minutes (m) into second whith now will be nH (new Hour), and nM (new Minutes)
    print(nH)
    nM=m*60
    print(nH,nM, s, tt)

    total = nH + nM + s
    print(total, tt)



#Just put in time in hh/mm/ss tt format and it's good to go!
timeToSeconds("12:59:18 AM")


