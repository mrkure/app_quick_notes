# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 10:55:31 2023

@author: CAZ2BJ
"""

import numpy as np, matplotlib as plt
import matplotlib.patches as mpatches
handler_map = {}

class mkPlot:
    
    class Circles(object):

        def __init__(self, multi):
            self.multi = multi
            return
        def legend_artist(self, legend, orig_handle, fontsize, handlebox):
    
            horizontal_shift = 3
            vertical_shift   = 5
            multiplicator    = 0.7
            
            patch1 = mpatches.Circle((0 + horizontal_shift,0 + vertical_shift),radius=7 * multiplicator, color="r")        
            handlebox.add_artist(patch1)
            
            horizontal_shift = 15
            patch2 = mpatches.Circle((0 + horizontal_shift,0 + vertical_shift),radius=7 * multiplicator, color="g")                
            handlebox.add_artist(patch2)
            
            horizontal_shift = 27
            patch3 = mpatches.Circle((0 + horizontal_shift,0 + vertical_shift),radius=7 * multiplicator, color="b")                
            handlebox.add_artist(patch3)
            return 
        
    class Stars(object):
        """Patch object used to add special tri-color label to curent plot
        """
        def __init__(self, multi):
            self.multi = multi
            return
        def legend_artist(self, legend, orig_handle, fontsize, handlebox):
    
            horizontal_shift = -5
            vertical_shift   = 0
            multiplicator    = 0.6
            
            n1 = np.array([0   + horizontal_shift,0  + vertical_shift])   * multiplicator
            n2 = np.array([10  + horizontal_shift,15  + vertical_shift])  * multiplicator
            n3 = np.array([20  + horizontal_shift,0   + vertical_shift])  * multiplicator
    
            n4 = np.array([0 + horizontal_shift,10  + vertical_shift])   * multiplicator
            n5 = np.array([20 + horizontal_shift,10 + vertical_shift])   * multiplicator
            n6 = np.array([10 + horizontal_shift,-5 + vertical_shift])   * multiplicator
    
            patch1 = mpatches.Polygon([n1,n2,n3 ], closed=True, color='r')
            patch2 = mpatches.Polygon([n4,n5,n6] , closed=True, color='r')
    
            handlebox.add_artist(patch1)
            handlebox.add_artist(patch2)
    
            horizontal_shift = 16
            vertical_shift   = 0
          
            n1 = np.array([0  + horizontal_shift,0 + vertical_shift]) * multiplicator
            n2 = np.array([10 + horizontal_shift,15 + vertical_shift])  * multiplicator
            n3 = np.array([20 + horizontal_shift,0 + vertical_shift])  * multiplicator
    
            n4 = np.array([0+ horizontal_shift,10+ vertical_shift])  * multiplicator
            n5 = np.array([20 + horizontal_shift,10 + vertical_shift])  * multiplicator
            n6 = np.array([10+ horizontal_shift,-5+ vertical_shift])  * multiplicator
           
            patch1 = mpatches.Polygon([n1,n2,n3 ], closed=True, color='g')
            patch2 = mpatches.Polygon([n4,n5,n6] , closed=True, color='g')
            
            handlebox.add_artist(patch1)
            handlebox.add_artist(patch2)
            
            horizontal_shift = 37
            vertical_shift   = 0
            
            n1 = np.array([0 + horizontal_shift,0  + vertical_shift]) * multiplicator
            n2 = np.array([10+ horizontal_shift,15 + vertical_shift]) * multiplicator
            n3 = np.array([20+ horizontal_shift,0 + vertical_shift])  * multiplicator
    
            n4 = np.array([0 + horizontal_shift,10 + vertical_shift])  * multiplicator
            n5 = np.array([20+ horizontal_shift,10 + vertical_shift])  * multiplicator
            n6 = np.array([10+ horizontal_shift,-5 + vertical_shift])  * multiplicator
           
            patch1 = mpatches.Polygon([n1,n2,n3 ], closed=True, color='b')
            patch2 = mpatches.Polygon([n4,n5,n6] , closed=True, color='b')
            
            handlebox.add_artist(patch1)
            handlebox.add_artist(patch2)
            return 
    
    class Crosses(object):
        """Patch object used to add special tri-color label to curent plot
        """
        def __init__(self, multi):
            self.multi = multi
            return
        def legend_artist(self, legend, orig_handle, fontsize, handlebox):
    
            horizontal_shift = -3
            vertical_shift   = 0
            multiplicator    = 0.9
    
            n1 = np.array([0   + horizontal_shift,0  + vertical_shift])   * multiplicator
            n2 = np.array([10  + horizontal_shift,10  + vertical_shift])  * multiplicator
            n3 = np.array([0   + horizontal_shift,10  + vertical_shift])   * multiplicator
            n4 = np.array([10  + horizontal_shift,0  + vertical_shift])  * multiplicator
            
            patch1 = mpatches.Polygon([n1,n2 ], closed=False,lw= 2,  color='r')      
            handlebox.add_artist(patch1)
            patch1 = mpatches.Polygon([n3,n4 ], closed=False, lw= 2, color='r')      
            handlebox.add_artist(patch1)
            
            horizontal_shift   = 10        
            n1 = np.array([0   + horizontal_shift,0  + vertical_shift])   * multiplicator
            n2 = np.array([10  + horizontal_shift,10  + vertical_shift])  * multiplicator
            n3 = np.array([0   + horizontal_shift,10  + vertical_shift])   * multiplicator
            n4 = np.array([10  + horizontal_shift,0  + vertical_shift])  * multiplicator
            
            patch1 = mpatches.Polygon([n1,n2 ], closed=False,lw= 2,  color='g')      
            handlebox.add_artist(patch1)
            patch1 = mpatches.Polygon([n3,n4 ], closed=False, lw= 2, color='g')      
            handlebox.add_artist(patch1)
            
            horizontal_shift   = 23         
            n1 = np.array([0   + horizontal_shift,0  + vertical_shift])   * multiplicator
            n2 = np.array([10  + horizontal_shift,10  + vertical_shift])  * multiplicator
            n3 = np.array([0   + horizontal_shift,10  + vertical_shift])   * multiplicator
            n4 = np.array([10  + horizontal_shift,0  + vertical_shift])  * multiplicator
            
            patch1 = mpatches.Polygon([n1,n2 ], closed=False,lw= 2,  color='b')      
            handlebox.add_artist(patch1)
            patch1 = mpatches.Polygon([n3,n4 ], closed=False, lw= 2, color='b')      
            handlebox.add_artist(patch1)
            return
    """ 
    ===============================================================================
     LINES
    ===============================================================================
    """
    class Lines(object):
        """Patch object used to add special tri-color label to curent plot
        """
        def __init__(self, multi):
            self.multi = multi
            return
        def legend_artist(self, legend, orig_handle, fontsize, handlebox):
    
            horizontal_shift = 0
            vertical_shift   = 0
            multiplicator    = 1
    
            n1 = np.array([0   + horizontal_shift,0  + vertical_shift])   * multiplicator
            n2 = np.array([30  + horizontal_shift,0  + vertical_shift])  * multiplicator        
            patch1 = mpatches.Polygon([n1, n2], closed=False,lw= 2,  color='r')      
            handlebox.add_artist(patch1)
            
            vertical_shift   = 5        
            n1 = np.array([0   + horizontal_shift,0  + vertical_shift])   * multiplicator
            n2 = np.array([30  + horizontal_shift,0  + vertical_shift])  * multiplicator        
            patch1 = mpatches.Polygon([n1,n2], closed=False,lw= 2,  color='g')      
            handlebox.add_artist(patch1)
            
            vertical_shift   = 10         
            n1 = np.array([0   + horizontal_shift,0  + vertical_shift])  * multiplicator
            n2 = np.array([30  + horizontal_shift,0  + vertical_shift])  * multiplicator        
            patch1 = mpatches.Polygon([n1,n2], closed=False,lw= 2,  color='b')      
            handlebox.add_artist(patch1)        
            return
    """ 
    ===============================================================================
     DASH_LINES
    ===============================================================================
    """
    class Dash_lines(object):
        """Patch object used to add special tri-color label to curent plot
        """
        def __init__(self, multi):
            self.multi = multi
            return
        def legend_artist(self, legend, orig_handle, fontsize, handlebox):
    
            horizontal_shift = 0
            vertical_shift   = 0
            multiplicator    = 1
    
            n1 = np.array([0   + horizontal_shift,0  + vertical_shift])   * multiplicator
            n2 = np.array([8  + horizontal_shift,0  + vertical_shift])  * multiplicator        
            patch1 = mpatches.Polygon([n1, n2], closed=False,lw= 2,  color='r')      
            handlebox.add_artist(patch1)
           
            vertical_shift   = 5        
            n1 = np.array([0   + horizontal_shift,0  + vertical_shift])   * multiplicator
            n2 = np.array([8  + horizontal_shift,0  + vertical_shift])  * multiplicator        
            patch1 = mpatches.Polygon([n1,n2], closed=False,lw= 2,  color='g')      
            handlebox.add_artist(patch1)
    
           
            vertical_shift   = 10 
            n1 = np.array([0   + horizontal_shift,0  + vertical_shift])  * multiplicator
            n2 = np.array([8  + horizontal_shift,0  + vertical_shift])  * multiplicator        
            patch1 = mpatches.Polygon([n1,n2], closed=False,lw= 2,  color='b')      
            handlebox.add_artist(patch1)  
       
            vertical_shift   = 0 
            horizontal_shift = 10
            n1 = np.array([0   + horizontal_shift,0  + vertical_shift])   * multiplicator
            n2 = np.array([8  + horizontal_shift,0  + vertical_shift])  * multiplicator        
            patch1 = mpatches.Polygon([n1, n2], closed=False,lw= 2,  color='r')      
            handlebox.add_artist(patch1)
            
            vertical_shift   = 5
            horizontal_shift = 10        
            n1 = np.array([0   + horizontal_shift,0  + vertical_shift])   * multiplicator
            n2 = np.array([8  + horizontal_shift,0  + vertical_shift])  * multiplicator        
            patch1 = mpatches.Polygon([n1,n2], closed=False,lw= 2,  color='g')      
            handlebox.add_artist(patch1)
            
            vertical_shift   = 10   
            horizontal_shift = 10
            n1 = np.array([0   + horizontal_shift,0  + vertical_shift])  * multiplicator
            n2 = np.array([8  + horizontal_shift,0  + vertical_shift])  * multiplicator        
            patch1 = mpatches.Polygon([n1,n2], closed=False,lw= 2,  color='b')      
            handlebox.add_artist(patch1)
            
            vertical_shift   = 0   
            horizontal_shift = 20        
            n1 = np.array([0   + horizontal_shift,0  + vertical_shift])   * multiplicator
            n2 = np.array([8  + horizontal_shift,0  + vertical_shift])  * multiplicator        
            patch1 = mpatches.Polygon([n1, n2], closed=False,lw= 2,  color='r')      
            handlebox.add_artist(patch1)
            
            vertical_shift   = 5   
            horizontal_shift = 20        
            n1 = np.array([0   + horizontal_shift,0  + vertical_shift])   * multiplicator
            n2 = np.array([8  + horizontal_shift,0  + vertical_shift])  * multiplicator        
            patch1 = mpatches.Polygon([n1,n2], closed=False,lw= 2,  color='g')      
            handlebox.add_artist(patch1)
            
            vertical_shift   = 10   
            horizontal_shift = 20       
            n1 = np.array([0   + horizontal_shift,0  + vertical_shift])  * multiplicator
            n2 = np.array([8  + horizontal_shift,0  + vertical_shift])  * multiplicator        
            patch1 = mpatches.Polygon([n1,n2], closed=False,lw= 2,  color='b')      
            handlebox.add_artist(patch1)        
            return
    


    
    def set_plot_config(ax, x_label='', y_label='', title='', xlim = [None, None], ylim = [None,None]):      
        """
        Sets comonly used plot parameters.

        Args:
            ax (TYPE): DESCRIPTION.
            x_label (string, optional): x label.
            y_label (string, optional): y label.
            title (string, optional): title.
            xlim ([float, float], optional): x axis limits.
            ylim ([float, float], optional): y axis limits.

        Returns:
            None.
            
        Examples:
            plt.plot([1,2,3], [1,2,3], 'ro-', label = 'legend label')
            Plot.set_plot_config(xa_label='xlabel', ya_label='ylabel', title='title', xlim = [None,100 ], ylim = [None, 100])

        """
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title(title)
         
        ax.set_xlim(xlim[0],xlim[1])
        ax.set_ylim(ylim[0],ylim[1])     
        return
 
    def set_rc_params(font_size_offset = 0, figsize = (1400,600), linewidth = 2, markersize = 6):
        """
        Sets comonly used plot parameters.     

        Args:
            font_size_offset (integer, optional): desired offset for titles, ticks, and legend fontsize values.
            figsize ((integer, integer), optional): size of figure in pixels(based on 96dpi monitors).
            markersize (integer, optional): DESCRIPTION. size of marker.

        Returns:
            None.
            
        Examples:
            Plot.set_rc_params(font_size_offset = 0, figsize = (1400,600), linewidth = 2, markersize = 6)
        """
        figsize = (figsize[0]/96, figsize[1]/96)
        plt.rc('lines', linewidth = linewidth,  markersize = markersize)
        plt.rc('axes',  titlesize = 16+font_size_offset, labelsize = 14 + font_size_offset, grid = False )
        plt.rc('xtick', labelsize = 14 + font_size_offset )
        plt.rc('ytick', labelsize = 14 + font_size_offset ) 
        plt.rc('legend', fontsize = 14 + font_size_offset )
        plt.rc('figure', dpi = 96, figsize = figsize, autolayout = True)  
        return

    def plot_swarm(arrays, positions, color="red", marker = "o", ms = 10, diff=0.1):
        """Draws swarm plot of inserted data sets
        
        Parameters
        ----------      
        axes : axes structure
            plt axes structure        
        arrays : nested array like 
            data that should be drawn, one list is one set of data
        positions : array like, number
            positions, where boxes should be drawn
        colors : string
            color of the swarm points
        diff : float
            seed for random difference between x positions of drawn points       
    
        Returns
        -------
        out:
        """      
        arrays, positions = mkPlot._remove_nonvalid_data(arrays, positions)
        t = 0
        for ar in arrays:
            if len(ar):
                t=1
            else:
                pass
        if t == False:
            return
        
        for array, position, in zip(arrays, positions):
            rand = np.random.uniform(low = position -diff, high = position + diff, size =  len(array))
            plt.plot( rand, array, linewidth = 0, c= color, marker = marker, ms = ms)        
        return            
    # =============================================================================
    # TEST    
    # data1  = [1,2,3,4,5]
    # data2 = [9,8,7,6,5,4]
    # plot_swarm([data1, data2], [88,99], color="g", marker= '*')
    # =============================================================================
    
    """ 
    ===============================================================================
     PLOT_BOX
    ===============================================================================
    """    
    def plot_box(arrays, positions, box_color = "k", whis = 1000):
        """Draws boxplot of inserted data sets. Contains function for removing nan and empty values.
        
        Parameters
        ----------      
        axes : axes structure
            plt axes structure        
        arrays : nested array like 
            data that should be drawn, one list is one set of data
        positions : array like, number
            positions, where boxes should be drawn
        box_color : string
            color of the boxes and medians      
        whis : integer
            setw how far should be whiskers drawn
        Returns
        -------
        out:
            None 
        """
        arrays, positions = mkPlot._remove_nonvalid_data(arrays, positions)
        t = 0
        for ar in arrays:
            if len(ar):
                t=1
            else:
                pass
        if t == False:
            return    
        
        
        zorder = 10
        aa = plt.boxplot(arrays, positions = positions, zorder = zorder, showmeans = False, whis = whis )
     
        bb = aa["means"]
        for line in bb:
            line.set_color(box_color)
            line.set_linewidth(2)
            line.set_zorder(zorder)
        bb = aa["medians"]
        for line in bb:
            line.set_color(box_color)
            line.set_linewidth(2) 
            line.set_zorder(zorder)              
        bb = aa["boxes"]      
        for line in bb:
            line.set_color(box_color)
            line.set_linewidth(2) 
            line.set_zorder(zorder)         
        bb = aa["whiskers"]    
        for line in bb:
            line.set_color(box_color)
            line.set_linewidth(2)
            line.set_zorder(zorder)
        bb = aa["fliers"]    
        for line in bb:
            line.set_color(box_color)
            line.set_linewidth(2)
            line.set_zorder(zorder)
        bb = aa["caps"]    
        for line in bb:
            line.set_color(box_color)
            line.set_linewidth(2)
            line.set_zorder(zorder)
        return
    # =============================================================================
    # TEST    
    # data1  = [1,2,3,4,5]
    # data2 = [9,8,7,6,5,4,30]
    # plot_box([data1, data2], [88,99], box_color="k")
    # =============================================================================
    
    """ 
    ===============================================================================
     MODIFY_TICKS
    ===============================================================================
    """
    def modify_ticks(new_labels, new_locations, action = "clear", axes_type = 'x'):
        """Adds ticks to current x_axes. Ticks are added in addition to curent ticks,
        when collision between old and new tick happens, it can be decided which ones should be kept
        
        Parameters
        ----------       
        tick_labels : list, string
            text shown on X axes for each box
        tick_positions : list, number
            positions, where labels on x axes should be drawn
        action : string
            clear - remove all old labels\n
            update - rewrite all old labels with the same axes position\n
            keep - keps all old labels with the same axes position
        axes_type : string 
            x or y axes
        Returns
        -------
        out:
            None 
        """
        old_locations, old_labels = plt.xticks()
        old_labels       = [a.get_text() for a in old_labels]  
        old_locations    = list(old_locations)
        result_labels    = []
        result_locations = []
      
        if action == "clear":
            result_labels    = new_labels
            result_locations = new_locations       
    
        elif action == "keep":
            result_labels.extend(old_labels)
            result_labels.extend(new_labels)
            result_locations.extend(old_locations)
            result_locations.extend(new_locations)
    
        elif action == "update":         
            result_labels.extend(new_labels)
            result_labels.extend(old_labels)
            result_locations.extend(new_locations)
            result_locations.extend(old_locations)
            
        else :pass
    
        for i, value in enumerate(result_locations):
            for j, value2 in enumerate(result_locations[i+1:]):
                if value == value2:
                    result_locations[j+i+1] = None
                    result_labels[j+i+1]    = None            
                else: pass
        
        result_locations = list(filter(lambda x : x != None, result_locations))         
        result_labels    = list(filter(lambda x : x != None, result_labels)) 
    
        if axes_type == "x":
            plt.xticks(result_locations, result_labels)
        if axes_type == "y":
            plt.yticks(result_locations, result_labels)
        return
    
    def add_label (label, line_color,  line_width = 2, line_style = '-', marker = '', marker_size = 6):
        """Adds special tri-color legend label to curent plot
        
        Parameters
        ---------- 
        label : string
            legend label string    
        line_color : string
            color of label object        
        line_width : int
            line width if there is a line
        line_style : string
            possible options - -, --, -., :      
        marker : string
            possible options - *,o,x,x and more.. 
        marker_size : int
            size of the marker
        Returns
        -------
        out:
            None 
        """
        plt.plot([], [], c = line_color, linewidth = line_width, ls = line_style, marker= marker, ms =marker_size, label = label)
        plt.legend(handler_map=handler_map)
        return 
    
    def add_label2 (ax, label, line_color,  line_width = 2, line_style = '-', marker = '', marker_size = 6):
        """Adds special tri-color legend label to curent plot
        
        Parameters
        ---------- 
        label : string
            legend label string    
        line_color : string
            color of label object        
        line_width : int
            line width if there is a line
        line_style : string
            possible options - -, --, -., :      
        marker : string
            possible options - *,o,x,x and more.. 
        marker_size : int
            size of the marker
        Returns
        -------
        out:
            None 
        """
        ax.plot([], [], c = line_color, linewidth = line_width, ls = line_style, marker= marker, ms =marker_size, label = label)
        ax.legend(handler_map=handler_map)
        return 

    def add_special_label (ax, label, symbol):
        """Adds special tri-color legend label to curent plot
        
        Parameters
        ----------           
        symbol : string
            possible options - *, o, x, -, -.
        label : string
            legend label text       
        Returns
        -------
        out:
            None 
        """    
        if symbol == "*":        
            handler_map.update({ax.plot([],[] , label = label)[0]:mkPlot.Stars(10)})  
        if symbol == "o":        
            handler_map.update({ax.plot([],[] , label = label)[0]:mkPlot.Circles(10)}) 
        if symbol == "x":        
            handler_map.update({ax.plot([],[] , label = label)[0]:mkPlot.Crosses(10)}) 
        if symbol == "-":        
            handler_map.update({ax.plot([],[] , label = label)[0]:mkPlot.Lines(10)}) 
        if symbol == "-.":        
            handler_map.update({ax.plot([],[] , label = label)[0]:mkPlot.Dash_lines(10)})
        plt.legend(handler_map=handler_map)
        return
    

    def _remove_nonvalid_data(data, positions):
        """
        Function removes nan values from nested lists and also removes empty lists from input data, next it removes corresponding values from positions list. Function should be used for boxplot, and violin plots to prevent errors.
        
        Parameters
        ----------       
        data : nested list
            data that should be drawn in violin or boxplot or such plot      
        positions : list 
            positions where data should be drawn
        positions : array like, number
            positions, where violins should be drawn       
    
        Returns
        -------
        data: nested list
            modified input data nested list 
        positions: list
            modified input parameters list        
        """
        for index, array in enumerate(data):
            data[index] = [x for x in array if (np.isnan(x) == False)]
        pos = []    
        for index, (array, position) in enumerate( zip(data, positions)):
        
            if len(array):
    
                pos.append(positions[index])
                
        data    = [x for x in data if len(x)] 
        return data,  pos 

class mkColorMap:
    """
    Color rotation class
    
    base map - ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'purple', 'pink', 'brown', 'orange', 'teal', 'coral', 'lightblue', 'lime', 'lavender', 'turquoise', 'darkgreen', 'tan', 'salmon', 'gold', 'darkred', 'darkblue']
    """  
    def __init__(self, arg = None):         
        """
        

        Args:
            arg (string iterable, optional): Colors list.

        Returns:
            None.

        """
        if arg:
            self.colors = arg
            self.pointer = 0
            self.number_of_colors = len(self.colors)            
                            
        else:
            self.pointer = 0
            self.colors           = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'purple', 'pink', 'brown', 'orange', 'teal', 'coral', 'lightblue', 'lime', 'lavender', 'turquoise', 'darkgreen', 'tan', 'salmon', 'gold', 'darkred', 'darkblue']
            self.number_of_colors = len(self.colors)
        return
    
    def reset(self):
        """
        Reset color list to first color

        Returns:
            None.

        """
        self.pointer = 0
        return
    
    def set_new_map(self, c_map):
        """
        Assing new custom color map.

        Args:
            c_map (TYPE): DESCRIPTION.

        Returns:
            None.

        """
        self.pointer = 0 
        self.colors = c_map
        self.number_of_colors = len(self.colors)        
        return

    def get_color(self, set_next = True):
        """
        Return current color and set pointer to next color in colors sequence.

        Args:
            set_next (Bool, optional): Set next color in colors sequence or keep current color.

        Returns:
            string: Color.

        """
        if self.pointer == self.number_of_colors-1: 
            if set_next:
                self.current_color = self.colors[self.pointer]            
                self.pointer = 0
            else:
                self.current_color = self.colors[self.pointer]                       
        else:
            if set_next:
                self.current_color = self.colors[self.pointer] 
                self.pointer += 1                
            else:
                self.current_color = self.colors[self.pointer]                 
                
        return self.current_color                
 