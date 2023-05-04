# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 19:50:21 2020
import mk_io
@author: CAZ2BJ
"""
import nptdms, numpy as np
    
class mkTdmsReader:
    def __init__(self):
        self.tdms_file = None
    
    def read_file(self, file_name:str)-> nptdms.tdms.TdmsFile:
        """read_file (nptdms.TdmsFile.open - reads only needed channels, nptdms.TdmsFile.read whole file)"""
        self.tdms_file  = nptdms.TdmsFile.open(file_name, raw_timestamps = False)
        return self.tdms_file
    
    def get_raw_channel(self, group_number:int, channel_name:str) ->(np.array, np.array):  
        """channel with original time data format (numpy.datetime64('2021-05-08T12:16:48.126951') in [us])"""
        group  = self.tdms_file.groups()[group_number]
        times  = group[f'Date time\n{channel_name}'][:]
        values = group[channel_name][:]
        return times, values 
    
    def get_channel(self, group_number, channel_name) ->(np.array, np.array):  
        """channel with time format in seconds starting at zero"""
        group  = self.tdms_file.groups()[group_number]
        times  = group[f'Date time\n{channel_name}'][:]
        times  = times.astype('int64')/1e6  # datetime to epoch time
        times  = times - times[0]
        values = group[channel_name][:]
        return times, values  
    
    def print_groups_and_channels(self) -> print:
        """print channels and groups"""
        for idx, group in enumerate(self.tdms_file.groups()):
            group_name = group.name
            for idxx, channel in enumerate(group.channels()):
                channel_name = channel.name
                print('group_idx: {} group_name: "{}" channel_idx: {} channel_name: "{}"\n'.format(idx, group_name, idxx, channel_name))
                print("------------------------------------------------------")
                
    def search_for_channel(self, _channel_name:str) -> print:
        """print channel and group if channel is in file (not case sensitive)"""
        for idx, group in enumerate(self.tdms_file.groups()):
            group_name = group.name
            for idxx, channel in enumerate(group.channels()):
                channel_name = channel.name
                if _channel_name.lower() in channel_name.lower():
                    print('group_idx: {} group_name: "{}" channel_idx: {} channel_name: "{}"\n'.format(idx, group_name, idxx, channel_name))
                    print("------------------------------------------------------")       
                    
#%% MAIN
# if __name__ == '__main__':
    
#     file = r'X:/03_Leepa/Leepa_2023/E2300040-02/data/recording/Dataloger/0-200_cycles/E2300040-02_20230201_080609_0001.tdms'        
#     tdms = TdmsReader()
#     tdms.read_file(file)
#     tdms.print_groups_and_channels()
#     tdms.search_for_channel("Pres")
#     x,y = tdms.get_channel(0, '-AI-Pressure-10')
    
    
