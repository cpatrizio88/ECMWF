#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 12:39:24 2017

@author: cpatrizio
"""
#!/usr/bin/env python
import calendar
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()
   
def retrieve_era_interim():
    '''    
       A function to demonstrate how to retrieve ERA-Interim monthly means data.   
       Change the variables below to adapt to your needs.
  
       ERA-Interim monthly data is timestamped to the first of the month, hence dates
       have to be specified as a list in this format:
       '19950101/19950201/19950301/.../20051101/20051201'.
  
       Data is stored on one tape per decade, so for efficiency we split the date range into
       decades, hence we get multiple date lists by decade:
       '19950101/19950201/19950301/.../19991101/19991201'
       '20000101/20000201/20000301/.../20051101/20051201'
       '20000101/20000201/20000301/.../20051101/20051201'
       In the example below the output data are organised as one file per decade:
       'era_interim_moda_1990'
       'era_interim_moda_2000'
       'era_interim_moda_2010'
       Please note that at the moment only decade 2010 is available.
    '''
    yearStart = 1979                       # adjust to your requirements - as of 2017-07 only 2010-01-01 onwards is available
    yearEnd = 2017                       # adjust to your requirements
    months = [1,2,3,4,5,6,7,8,9,10,11,12]   # adjust to your requirements
    var = 'Qnetsurf'                            
  
    years = range(yearStart, yearEnd+1)
    print 'Years: ',years
    decades = list(set([divmod(i, 10)[0] for i in years]))
    decades = [x * 10 for x in decades]
    decades.sort()
    print 'Decades:', decades
  
# loop through decades and create a month list
    for d in decades:
        requestDates=''
        for y in years:
            if ((divmod(y,10)[0])*10) == d:
                for m in months:
                    requestDates = requestDates+str(y)+(str(m)).zfill(2)+'01/'
        requestDates = requestDates[:-1]
        print 'Requesting dates: ', requestDates
        target = 'era_interim_moda_{:s}_{:d}.nc'.format(var, d) # specifies the output file name
        print 'Output file: ', target
        era_interim_request(requestDates, d, target)
  
# the actual data request
def era_interim_request(requestDates, decade, target):
    '''
        Change the keywords below to adapt to your needs.
        The easiest way to do this is:
        1. go to http://apps.ecmwf.int/datasets/data/interim-full-moda/levtype=sfc/
        2. click through to the parameters you want, for any date
        3. click 'View the MARS request'
    '''
    server.retrieve({
            #uncomment to retrieve 12 hour accumulated lhf and shf
           "class": "ei",
           "dataset": "interim",
           "expver": "1",
           "grid": "0.75/0.75",
           "levtype": "sfc",
           "param": "146.128/147.128",
           "step": "0-12",
           "stream": "mdfa",
           "type": "fc",
           'format': 'netcdf',
           'date': requestDates,
           'decade': decade,
           'target': target,
#        "class": "ei",              # do not change
#        "dataset": "interim",       # do not change
#        'expver': '1',              # do not change
#        'stream': 'moda',           # monthly means of daily means
#        'type': 'an',               # analysis (versus forecast, fc)
#        'levtype': 'sfc',           # surface data (versus pressure level, pl, and model level, ml)
#        #"levelist": "1/2/3/5/7/10/20/30/50/70/100/125/150/175/200/225/250/300/350/400/450/500/550/600/650/700/750/775/800/825/850/875/900/925/950/975/1000",
#        'param': '260487/260488',             # specify parameter code for variable here
#        'grid': '0.75/0.75',        # horizontal resolution of output in degrees lat/lon
#        'format': 'netcdf',         # get output in netcdf; only works with regular grids; for GRIB remove this line
#        'date': requestDates,       # dates, set automatically from above
#        'decade': decade,           # decade set automatically from above
#        'target': target            # output file name, set automatically from above
    })
    
#param codes
#levtype: sfc
#Curl of Wind Stress	: 151151
#10-m u/v: 165.128/166.128
#v wind: 132.128
#SST: 34
#mean SLP: 151
#accumulated SHF/LHF: 146.128/147.128
#net shortwave/net longwave/clear-sky counterparts: 
  #sfc:"176.128/177.128/210.128/211.128"
#TOA: 178.128/179.128/208.128/209.128/
#levype: pl
#fraction of cloud cover: 248.128 (would need to specify levels for this, e.g.     
# "levelist": "1/2/3/5/7/10/20/30/50/70/100/125/150/175/200/225/250/300/350/400/450/500/550/600/650/700/750/775/800/825/850/875/900/925/950/975/1000",
#stream function: 1 
#meridional wind: 300034
#omega: 135
#ocean parameters: 
#  ocean mixed layer u/v: 260487/260488
# ocean mixed layer thickness: 151227
if __name__ == '__main__':
    retrieve_era_interim()

#COPY FOR SURFACE SENSIBLE AND LATENT HEAT FLUXES
#!/usr/bin/env python
#    "class": "ei",
#    "dataset": "interim",
#    "expver": "1",
#    "grid": "0.75/0.75",
#    "levtype": "sfc",
#    "param": "146.128/147.128",
#    "step": "0-12",
#    "stream": "mdfa",
#    "type": "fc",
#    'format':, 'netcdf'
#    'date':, requestDates
#    'decade':, decade,
#    'target': target,
