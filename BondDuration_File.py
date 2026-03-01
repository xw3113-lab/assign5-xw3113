import numpy as np

def Duration(y, face, couponRate, m, ppy = 1):
    pvcfsum = 0
    dpvcfsum = 0
    cf = couponRate * face
    for t in range(1, (ppy *m) +1):
        pv = (1+ y/ppy) **(-t)
        pvcf= pv*cf/ppy
        pvcfsum += pvcf
        dpvcfsum += t*pvcf
    bondprice = pvcfsum + pv*face
    dbondprice = dpvcfsum + m*pv*face
    return(dbondprice/bondprice)
