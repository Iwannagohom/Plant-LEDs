def timeToSeconds(t):               #(t= "12:59:18 AM")
    h,m,s = t.split(":")
    #print(h,m,s)

    s,tt=s.split(" ")
    #print(s)
    #print(t)
    h=int(h)                       # all = (h,m,s,t)
    m=int(m)                        # ok = float(all)
    s=int(s)                        #print(type(h))
    print(h,m,s,tt)


    if h == 12 and tt == "AM":
       nH = 0
    else:
        nH = h*60*60

    print(nH)
    nM=m*60
    print(nH,nM, s, tt)

    total = nH + nM + s
    print(total, tt)




timeToSeconds("12:59:18 AM")


