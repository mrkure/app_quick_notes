# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 11:09:17 2023

@author: CAZ2BJ
"""
import json, os, sys

class Tools:
    
    dic_params = { 
                    'x':0,
                    'y':0,
                    'w':100,
                    'h':100,
                    'string':'',        
                  }
    
    def save_params(dic_params):
        file = rf'{os.path.split(os.path.dirname(__file__))[0]}/res/{os.getlogin()}_settings.ini'
        with open(file, 'w') as file_object:  
            json.dump(dic_params, file_object, indent = 4) 
            
    def load_params():
        try:
            file = rf'{os.path.split(os.path.dirname(__file__))[0]}/res/{os.getlogin()}_settings.ini'
            with open(file, 'r') as file_object:  
                dic_params = json.load(file_object)     
        except:
            return Tools.dic_params
        return {**Tools.dic_params, **dic_params} 


      
#%% TEST
if __name__ == "__main__":
    dic = Tools.load_params()
    Tools.save_params(dic)
