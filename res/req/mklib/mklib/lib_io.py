# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 14:58:34 2023

@author: CAZ2BJ
"""

import os, sys, subprocess, stat 

class mkIO:
    def ishidden(path):
        return bool(os.stat(path).st_file_attributes  &  stat.FILE_ATTRIBUTE_HIDDEN)
    
    
    def isreadonly(path):
        return bool(os.stat(path).st_file_attributes  &  stat.FILE_ATTRIBUTE_READONLY)
    
    
    def issystem(path):
        return bool(os.stat(path).st_file_attributes  &  stat.FILE_ATTRIBUTE_SYSTEM)
    
    
    def istemporary(path):
        return bool(os.stat(path).st_file_attributes  &  stat.FILE_ATTRIBUTE_TEMPORARY)
    
    
    def isnormal(path):
        return not any([mkIO.ishidden(path), mkIO.issystem(path), mkIO.istemporary(path)])
    
    
    def apply_filter_files(path, filters):
        if not filters:
            return True
        results = []
        for ffilter in filters[:-1]:
            filter_res = [True]  
            
            if ffilter['part'] == 0:
                var, ext = os.path.splitext(path)
            elif ffilter['part'] == -1:
                base, ext = os.path.splitext(path)
                var       = base.split(os.sep)[ffilter['part']]          
            else:
                base, ext = os.path.splitext(path)
                var = path.split(os.sep)[ffilter['part']]
    
            for key, val in ffilter.items():      
                if key == "con" and val:
                    if not val[-1]([con in var for con in val[:-1]]): 
                        filter_res.append(False)
                        break
                if key == "exc" and val:
                    if val[-1]([exc in var for exc in val[:-1]]): 
                        filter_res.append(False)
                        break    
                if key == "ext" and val:
                    if not val[-1]([f".{e}" == ext for e in val[:-1]]): 
                        filter_res.append(False)
                        break 
                    else:
                        pass
                if key == "attr" and val:
                    if not val[-1]([attr(path) for attr in val[:-1]]): 
                        filter_res.append(False)
                        break
    
            results.append(all(filter_res))        
        return filters[-1](results)
    
    
    def apply_filter_dirs(path, filters):
        if not filters:
            return True
        results = []
        for ffilter in filters[:-1]:
            filter_res = [True]  
            if ffilter['part'] == 0:
                var = path
            else:
                var = path.split(os.sep)[ffilter['part']]
    
            for key, val in ffilter.items():      
                if key == "con" and val:
                    if not val[-1]([con in var for con in val[:-1]]): 
                        filter_res.append(False)
                        break
                if key == "exc" and val:
                    if val[-1]([exc in var for exc in val[:-1]]): 
                        filter_res.append(False)
                        break    
                if key == "ext" and val:
                    pass
                if key == "attr" and val:
                    if not val[-1]([attr(path) for attr in val[:-1]]): 
                        filter_res.append(False)
                        break
    
            results.append(all(filter_res))        
        return filters[-1](results)
    
    
    def get_dirs(root_dir:str, rec = [0,100], filters_dirs = [],pprint:bool = False) -> [str]:
        root_dir = os.path.realpath(root_dir.replace("'", "").replace('"',""))
        min_deep_level = len(root_dir.split(os.sep)) + rec[0]
        max_deep_level = len(root_dir.split(os.sep)) + rec[1]
        dirs_res = []
        
        for dirpath, dirnames, filenames in os.walk(root_dir):
            # continue if out of rec limits
            dirpath_dir_deep_level = len(dirpath.split(os.sep))
            if dirpath_dir_deep_level < min_deep_level or dirpath_dir_deep_level > max_deep_level: continue 
            # get dirs       
            dirs = [os.path.normpath(f'{dirpath}\{dirname}') for dirname in dirnames] 
            # check if dirrs fulfill filter requirements
            for dirr in dirs: 
                accept = mkIO.apply_filter_dirs(dirr, filters_dirs)
                if accept:                
                    if pprint: print(dirr)
                    dirs_res.append(dirr)          
        #sort and create extended dirs 
        dirs_res.sort()  
        return dirs_res
    
    
    def get_files(root_dir:str, rec:[int, int] = [0,100], filters_dirs:[{}] = [], filters_files:[{}] = [], pprint:bool = False):
        root_dir = os.path.realpath(root_dir.replace("'", "").replace('"',""))
        dirs_res = mkIO.get_dirs(root_dir, rec = [rec[0]-1, rec[1]-1], pprint = False, filters_dirs = filters_dirs)
   
        if rec[0] == 0: dirs_res.append(root_dir)
    
        files_res = []
        for dirr in dirs_res:
            files = [os.path.join(dirr,f) for f in os.listdir(dirr) if os.path.isfile(os.path.join(dirr,f))]
            for file in files:
                accept = mkIO.apply_filter_files(file, filters_files)
                if accept:
                    files_res.append(file)                  
                    if pprint: print(file) 
        files_res.sort()            
        return files_res
                
    def get_files_mulltipaths(paths:str, rec:[int, int] = [0,100], filters_dirs:[{}] = [], filters_files:[{}] = [], pprint:bool = False):
        files = []
        for item in paths:
            if os.path.isfile(item):
                if pprint: print(item)
                files.append(item)
            else:
                files += mkIO.get_files(item, rec = rec, filters_dirs = filters_dirs, filters_files = filters_files, pprint=True)  
        files.sort()
        len_files = len(files)
        files = [(num, len_files, file) for num, file in enumerate(files)] 
        return files        
    
        
    def activate_env_from_filename(activate:bool, script_name:str) -> None:
        """ activate:bool option to run/not run activation
        
        script_name:str in a form of __file__ variable
        
        FUNCTION USES FILENAME AS NEXT PARAMETERS 
        
        script_name-env-work-1-py -> split for parts, work: envname, 1:show window"""
        
        split = script_name.replace(".", "-").split("-")
        if len(sys.argv) == 1 and activate and len(split) >=5 and split[-4] == "env":
            env_name    = split[-3]
            show_window = int(split[-2])
            commands = []
            commands.append(f"call conda activate {env_name}")
            commands.append(f"python {script_name} dummy_arg")
            command = " & ".join(commands)        
            if show_window:  subprocess.Popen(command, shell = True)
            else:            subprocess.Popen(command, shell = True,  creationflags = subprocess.CREATE_NO_WINDOW)
            sys.exit(f'Loading "{env_name}" environment...\n')

    def activate_env(activate:bool, env_name:str, script_name:str, show_window) -> None:
        if len(sys.argv) == 1:
            commands = []
            commands.append(f"call conda activate {env_name}")
            commands.append(f"python {script_name} dummy_arg")
            command = " & ".join(commands)        
            if show_window:  subprocess.Popen(command, shell = True)
            else:            subprocess.Popen(command, shell = True,  creationflags = subprocess.CREATE_NO_WINDOW)
            sys.exit(f'Loading "{env_name}" environment...\n')
            
    def get_tesla_value_from_filename(filename:str) ->str:
        """ get tesla string from path, if not found return enpty string"""
        name = os.path.normpath(filename)
        dir_names       = name.split(os.sep)
        result = ''
        for i in dir_names:
            if len(i) == 11 and 'E' in i and '-'in i:
                result =  i
        if result == '':
            result = 'Results'
        return result