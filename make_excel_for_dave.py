#!/usr/bin/env python

from Ska.engarchive import fetch
import pandas as pd

# These are the temperatres relevant to the thermal model:
msidlist = [
        "2FE00ATM",  # Front-end Temperature (c)
        "2LVPLATM",  # LVPS Plate Temperature (c)
        "2IMHVATM",  # Imaging Det HVPS Temperature (c)
        "2IMINATM",  # Imaging Det Temperature (c)
        "2SPHVATM",  # Spectroscopy Det HVPS Temperature (c)
        "2SPINATM",  # Spectroscopy Det Temperature (c)
        "2PMT1T"  ,  # PMT 1 EED Temperature (c)
        "2PMT2T"  ,  # PMT 2 EED Temperature (c)
        "2DCENTRT",  # Outdet2 EED Temperature (c)
        "2FHTRMZT",  # FEABox EED Temperature (c)
        "2CHTRPZT",  # CEABox EED Temperature (c)
        "2FRADPYT",  # +Y EED Temperature (c)
        "2CEAHVPT",  # -Y EED Temperature (c)
        "2CONDMXT",  # Conduit Temperature (c)
        "2UVLSPXT",  # Snout Temperature (c)
        "2FEPRATM",  # FEA PreAmp (c)
        "2DTSTATT"   # OutDet1 Temperature (c)
        ]

# Dave asked for the last ~10 years of data, so
start = '2009:001'
stop = '2019:252'

# instantiate an emtpy dictionary to hold our fetch results
msid_means_dict = {}

# fetch every MSID, populate a dataframe
# you can also do this with MSIDset, like:
#temps = fetch.MSIDset(msidlist, start, stop, stat='daily')


print("Populating time column")
msid_means_dict['Time'] = fetch.MSID(msidlist[0], start, stop, stat='daily').times

for msid in msidlist:
    print("Fetching {}".format(msid))
    fetch_result = fetch.MSID(msid, start, stop, stat='daily')
    
    msid_means_dict[msid] = fetch_result.means
	
# Convert to a Pandas dataframe
dataframe = pd.DataFrame.from_dict(msid_means_dict)

# Create Excel file
dataframe.to_excel("hrc_temperatures_10yr.xlsx", index=False)
