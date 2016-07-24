import math

def calcProp(DV, Mpayload, Isp, IMF):
    ''' Calculate the propellant load(s) for burns in DV with payload Mpayload.
    DV and Mpayload must be lists in brackets []. Isp and IMF are floats.'''    
    err = 100.0
    Minert = 1000.0
    Mprop = list()
    MR = list()
    for burn in DV: # Create list of mass ratios and initialize propellant list
        MR.append(math.exp(burn / 9.81 / Isp))
        Mprop.append(3000.0)
#    if 1/IMF > MR[1]: # Check mass ratio vs. IMF
#        raise RuntimeError("The IMF is too high to accommodate this mass ratio")        
    while err > 0.001:
        for i in range(len(DV)):
            if i == 0: # If final burn, don't add  propellant to payload
                Mprop[-i-1] = (MR[-i-1] - 1.0) * (Minert + Mpayload[-i-1])
            else: # All other burns add propellant for subsequent burns as paylaod
                Mprop[-i-1] = (MR[-i-1] - 1.0) * (Minert + Mpayload[-i-1] + sum(Mprop[-i:]))
        Minert2 = calcInert(Minert, sum(Mprop), IMF) # Refresh inert mass guess
        err, Minert = math.sqrt((Minert2 - Minert)**2), Minert2 # Calculate error and set new inert mass guess
    return Minert, sum(Mprop), Mprop
    
def calcInert(Minertguess, Mprop, IMF):
    return IMF * (Minertguess + Mprop)
        
burns = [100.0, 200.0, 300.0, 400.0, 500.0]
payloads = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0]
Isp = 320.0
IMF = 0.1
Minert, Mproptot, Mproplist = calcProp(burns, payloads, Isp, IMF)
print(Minert)
print(Mproptot)
print(Mproplist)
