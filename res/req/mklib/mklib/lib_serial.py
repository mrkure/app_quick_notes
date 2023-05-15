# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 13:52:02 2019
@author: CAZ2BJ
VTS-7060, USB-RLY02
USING pyserial 3.4 
COM6 USB RELAY 
COM7 CHAMBER
"""

import serial as pyser
import serial.tools.list_ports as  tlp

class mkSerial:
    def __init__():
        pass  
    @staticmethod    
    def print_serial_devices():
        comports = tlp.comports()
        for port in comports:
            print(port.device, port.name, port.description)
        return 
    @staticmethod    
    def start_serial_com(port):
        try:
            ser = pyser.Serial(port=port,baudrate=9600,parity=pyser.PARITY_NONE,
                stopbits=pyser.STOPBITS_ONE, bytesize=pyser.EIGHTBITS, timeout=0)
            return ser
        except:
            raise Exception('Failed to start communication at port {}'.format(port))
    @staticmethod    
    def close_serial_com(port):
        port.close()


#%% MAIN
if __name__ == '__main__':
    mkSerial.print_serial_devices()




