# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:58:48 2019

@author: caz2bj
"""
from asammdf import MDF; import pandas as pd, numpy as np

class mkAsamMdfReader:
    def __init__(self):
        self.filename = None
        self.mdf_file = None
        
    def read_mdf_file(self, filename:str, channels:[str] = []) -> MDF:
        """ read_mdf_file(filename: str, channels:[str] (all channels if empty list)) -> MDF.mdf_file
        READ MDF FILE, ALL CHANNELS OR ONLY CHANNELS IN LIST"""
        self.mdf_file = MDF(filename, channels = None if not channels else channels)
        return self.mdf_file
    
    def configure_mdf_file(self, use_display_names:bool = False, integer_interpolation:int = 0, float_interpolation:int = 0) -> None:
        """configure_mdf_file(mdf_file:[MDF.mdf_file], use_display_names:bool, integer_interpolation:int, float_interpolation:int) -> None:
        CONFIGURES BEHAVIOUR OF READED MDF FILE, MAINLY INTERPOLATION OF SIGNALS WITH DIFFERENT RASTERS WHEN LATER CONVERTED TO DATAFRAME"""
        self.mdf_file.configure(
                use_display_names     = use_display_names,     # using DisplayName of channel insted of channel name
                integer_interpolation = integer_interpolation, # 0 - repeat previous, 1 - linear interpolation
                float_interpolation   = float_interpolation)   # 0 - repeat previous, 1 - linear interpolation
            
    def search_for_channel(self, wildcards:[str]) ->[str]:
        """search_for_channel(mdf_file:[MDF.mdf_file], wildcard:str) -> found_channels_names_list:[str]:
        SEARCH FOR CHANNEL IN FILE BY NAMES USING WILDCARD SEARCH"""   
        channels_found = []
        for wildcard in wildcards:
            channels_found += self.mdf_file.search(wildcard, case_insensitive=True, mode='wildcard')
        return channels_found
    
    def mdf_file_to_df(self, channels:[str] = [], use_interpolation:int = True) -> pd.DataFrame:
        """mdf_file_to_df(channels:[str] (all channels if empty list)) -> pd.DataFrame:
        CREATES NEW PANDAS DATAFRAME FROM MDF FILE WITH ONLY SPECIFIED CHANNELS INCLUDED"""
        return self.mdf_file.to_dataframe(channels = channels if channels else None, 
                                          time_from_zero = False,                # reset first time to zero
                                          ignore_value2text_conversions = True,  # convert CoSCR_st states etc. to numbers
                                          use_interpolation = use_interpolation) # use interpolation type from config or fill missing values with nan
                                          
    def get_signal_raw(self, signal_name:str) -> (np.array, np.array):
        """get_signal_raw(signal_name:str) -> (np.array, np.array):
        RETURN NUMPY ARRAYS OF TIMESTAMPS AND VALUES"""       
        signal = self.mdf_file.select([signal_name], ignore_value2text_conversions = True)[0]
        return signal.timestamps, signal.samples
    
#%% MAIN
# if __name__ == '__main__':
#     file = r'C:/_binary_build/ED2206507_202206220931_4500_-7_11000_01_111dm100.mf4'
    
#     # read file
#     reader = AsamMdfReader(file)
#     reader.read_mdf_file(file)
    
#     # configure file 
#     reader.configure_mdf_file(use_display_names     = 0,
#                               integer_interpolation = 0, 
#                               float_interpolation   = 0)
    
#     # search for channels in file using wildcard
#     channels_names_found = reader.search_for_channel(["*sys*pres*rel", '*tank1*', "CoSCR_st"])
    
#     # convert all channels (if list is empty) or selected channels to dataframe (default: using interpolation repeat previous)
#     df  = reader.mdf_file_to_df( channels_names_found, use_interpolation = True )
#     df  = df.iloc[0:500, :]
    
#     # get raw signal values
#     x, y = reader.get_signal_raw("T_tank1")













