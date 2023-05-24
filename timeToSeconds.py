def timeToSeconds(t, k):               #(t= "12:59:18 AM")
                                         #!!! K is the difference between UTC and EST time zone.
                                         #K is a variable to convert EST time into UCT time later in the code  
    
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
    
    if total < 18000:
        total = ((total + 86400)+k*60*60)
        #print("Total = ", total, tt)
    
    return total              #Print or return depending if it's within the rest of the code or on it's own



#Just put in time in "hh:mm:ss tt" format, and what is the differense betwent UTC and EST time zone and it's good to go!
timeToSeconds("12:59:18 AM", -5)


