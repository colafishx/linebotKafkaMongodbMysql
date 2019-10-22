#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
from datetime import *

class MsgToBackend:
    def __init__(self, user_id):
        self.user_id = user_id
        
    def msgbio(self):
        #chk the user's latest response for gender
        colnames = ['userId', 'val_Id', 'gender', 'tStamp']
        dfGen = pd.read_csv('../users_gender.csv', sep=',', header=None, names = colnames)
        gen = dfGen.loc[dfGen.loc[(dfGen['userId']==self.user_id)]['tStamp'].idxmax()]['gender']
        #chk the user's latest response for birthday
        colnames = ['userId', 'val_Id', 'bDate', 'tStamp']
        dfbDate = pd.read_csv('../users_birthday.csv', sep=',', header=None, names = colnames)
        bDate = dfbDate.loc[dfbDate.loc[(dfbDate['userId']==self.user_id)]['tStamp'].idxmax()]['bDate']
        #compute the user's age for classification
        age = (datetime.now()-datetime.strptime(bDate, '%Y-%m-%d')).days//365
        #chk the user's latest response for whether been to be Tokyo b4
        colnames = ['userId', 'val_Id', 'toTko', 'tStamp']
        dfTko = pd.read_csv('../users_been2tko.csv', sep=',', header=None, names = colnames)
        tko = dfTko.loc[dfTko.loc[(dfTko['userId']==self.user_id)]['tStamp'].idxmax()]['toTko']
        #integrate the msg & send
        msg_bio = {self.user_id: (gen, age, tko, datetime.timestamp(datetime.now()))}
        return msg_bio
    
    def msgflight(self):
        #chk the user's latest response for return date
        colnames = ['userId', 'val_Id', 'rDate', 'tStamp']
        dfRdate = pd.read_csv('../users_date_ret.csv', sep=',', header=None, names = colnames)
        rDate = dfRdate.loc[dfRdate.loc[(dfRdate['userId']==self.user_id)]['tStamp'].idxmax()]['rDate']
        #chk the user's latest response for departure date
        colnames = ['userId', 'val_Id', 'dDate', 'tStamp']
        dfDdate = pd.read_csv('../users_date_dept.csv', sep=',', header=None, names = colnames)
        dDate = dfDdate.loc[dfDdate.loc[(dfDdate['userId']==self.user_id)]['tStamp'].idxmax()]['dDate']
        #compute trip days for hotel and tour plan
        tripDays = datetime.strptime(rDate, '%Y-%m-%d')-datetime.strptime(dDate, '%Y-%m-%d')
        #transfer the departure date into weekday for flight, 1 for Mon & 7 for Sun
        dWkDay = datetime.isoweekday(datetime.strptime(dDate, '%Y-%m-%d'))
        #transfer the return date into weekday for flight
        rWkDay = datetime.isoweekday(datetime.strptime(rDate, '%Y-%m-%d'))
        #integrate the msg & send
        msg_flight = {self.user_id: (dWkDay, tripDays.days, rWkDay, datetime.timestamp(datetime.now()))}
        return msg_flight
    
    def msghotel(self):
        #chk the user's latest response for return date
        colnames = ['userId', 'val_Id', 'rDate', 'tStamp']
        dfRdate = pd.read_csv('../users_date_ret.csv', sep=',', header=None, names = colnames)
        rDate = dfRdate.loc[dfRdate.loc[(dfRdate['userId']==self.user_id)]['tStamp'].idxmax()]['rDate']
        #chk the user's latest response for departure date
        colnames = ['userId', 'val_Id', 'dDate', 'tStamp']
        dfDdate = pd.read_csv('../users_date_dept.csv', sep=',', header=None, names = colnames)
        dDate = dfDdate.loc[dfDdate.loc[(dfDdate['userId']==self.user_id)]['tStamp'].idxmax()]['dDate']
        #compute trip days for hotel and tour plan
        tripDays = datetime.strptime(rDate, '%Y-%m-%d')-datetime.strptime(dDate, '%Y-%m-%d')
        #integrate the msg & send
        msg_hotel = {self.user_id: (dDate, tripDays.days, rDate, datetime.timestamp(datetime.now()))}
        return msg_hotel
    
    def msgprefer(self):
        #chk the user's latest response for budget
        colnames = ['userId', 'val_Id', 'budget', 'tStamp'] 
        dfb = pd.read_csv('../users_budget.csv', sep=',', header=None, names = colnames)
        budget = dfb.loc[dfb.loc[(dfb['userId']==self.user_id)]['tStamp'].idxmax()]['budget']
        #chk the user's latest response for partner
        colnames = ['userId', 'val_Id', 'partner', 'tStamp']
        dfp = pd.read_csv('../users_partner.csv', sep=',', header=None, names = colnames)
        partner = dfp.loc[dfp.loc[(dfp['userId']==self.user_id)]['tStamp'].idxmax()]['partner']
        #integrate the msg & send
        msg_prefer = {self.user_id: (partner, budget, datetime.timestamp(datetime.now()))}
        return msg_prefer

