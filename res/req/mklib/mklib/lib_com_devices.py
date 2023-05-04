# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 13:52:02 2019
@author: CAZ2BJ
VTS-7060, USB-RLY02
USING pyserial 3.4 
COM6 USB RELAY 
COM7 CHAMBER
"""
import time

class VTS7060: 
    """
    Remote controll of VTS7060 temperature chamber.

    Parameters
    ----------
     port : Comm port object of pyserial module.
        Comm port.

    Returns
    -------
    None.

    """
    def __init__(self, port):
        """
        Remote controll of VTS7060 temperature chamber.

        Parameters
        ----------
         port : Comm port object of pyserial module.
            Comm port.

        Returns
        -------
        None.

        """
        self._START_STRING        = '$01E TEMP_VALUE 0050.0 0000.0 0100.0 4200.0 0030.0 0005.0 0000.3 0000.1 0000.0 01000000000000000000000000000000\r\n'   
        self._STOP_STRING         = '$01E TEMP_VALUE 0050.0 0000.0 0100.0 4200.0 0030.0 0005.0 0000.3 0000.1 0000.0 00000000000000000000000000000000\r\n'  
        self._REQUEST_INFO_STRING = '$01I\r\n'
        self._port                =  port

    def set_port(self, port):
        """
        Set comm port.

        Parameters
        ----------
        port : Comm port object of pyserial module.
            Comm port.

        Returns
        -------
        None.

        """
        self._port = port 
  
    def get_temperature(self, delay = 1):
        """
        Get current, desired temperature.

        Parameters
        ----------
        delay : float [s], optional
            Writing delay to serial port.

        Returns
        -------
        temp_actual : float
            Actual temperature.
        temp_desired : float
            Desired(set temperature).
        temp_string : String
            Temperature string.

        """
        self._port.readline() # Flush buffer
        time.sleep(delay/3)    
        self._port.write(self._REQUEST_INFO_STRING.encode())
        time.sleep(delay/3)
        temp_string = self._port.readline().decode()
        time.sleep(delay/3)     
        temp_actual  = float(temp_string.split(' ')[1])
        temp_desired = float(temp_string.split(' ')[0])       
        return temp_actual, temp_desired, temp_string
   
    def set_temperature(self, temperature, delay = 1):
        """
        Set temperature to chamber.

        Parameters
        ----------
        temperature : float
            Temperature to be set.
        delay : float [s], optional
            Writing delay to serial port.

        Returns
        -------
        None.

        """
        temperature = '{}{:0>5.1f}'.format( ('-' if temperature < 0 else '0'), abs(temperature) )      
        result      = self._START_STRING.replace('TEMP_VALUE', temperature)
        time.sleep(delay/2)
        self._port.write(result.encode())
        time.sleep(delay/2)

  
    def stop(self, delay = 1):
        """       
        Stop chamber.
        
        Parameters
        ----------
        delay : float [s], optional
            Writing delay to serial port.

        Returns
        -------
        None.

        """
        actual_temp, desired_temp, string = self.get_temperature( delay = delay)
        desired_temp = '{}{:0>5.1f}'.format( ('-' if desired_temp < 0 else '0'), abs(desired_temp) )
        self._send_string_value( self._STOP_STRING.replace('TEMP_VALUE', desired_temp), delay = 1)          
                    
    def start(self, delay = 1):
        """
        Start chamber.
        
        Parameters
        ----------
        delay : float [s], optional
            Writing delay to serial port.

        Returns
        -------
        None.

        """
        actual_temp, desired_temp, string = self.get_temperature( delay = delay)
        desired_temp = '{}{:0>5.1f}'.format( ('-' if desired_temp < 0 else '0'), abs(desired_temp) )
        self._send_string_value(self._START_STRING.replace('TEMP_VALUE', desired_temp), delay = delay)    

    def is_running(self, delay = 1):
        """
        True if chamber is running.
        
        Parameters
        ----------
        delay : float [s], optional
            Writing delay to serial port.

        Returns
        -------
        bool
            DESCRIPTION.

        """
        a, b, c = self.get_temperature(delay = delay)
        if int(c.split(' ')[-1][1]):
            return True
        return False 
    
    def _send_string_value(self, value, delay = 1):
        """       
        Write string to serial port
        
        Parameters
        ----------
        value : String
            String to send.
        delay : float [s], optional
            Writing delay to serial port.

        Returns
        -------
        None.

        """
        time.sleep(delay/2)
        self._port.write(value.encode())
        time.sleep(delay/2)
   
    def _read_string_value(self, delay = 1):
        """       
        Read string from serial port.
        
        Parameters
        ----------
        delay : float [s], optional
            Writing delay to serial port.

        Returns
        -------
        temp_string : String
            String red from serial port.

        """
        time.sleep(delay/2)
        temp_string = self._port.readline().decode()
        time.sleep(delay/2)
        return temp_string
    
class USBrelay:
    def __init__(self, port):
        self.on_1    = 'e'
        self.on_2    = 'f'
        self.on_all  = 'd'       
        self.off_1   = 'o'
        self.off_2   = 'p'
        self.off_all = 'n'        
        self.port        = port
  
    def set_port(self, port):
        self.port = port
        
        
    def set_on_1(self, delay = 1):
        time.sleep(delay/2)
        self.port.write(self.on_1.encode())
        time.sleep(delay/2)

    def set_on_2(self, delay = 1):
        time.sleep(delay/2)
        self.port.write(self.on_2.encode())
        time.sleep(delay/2)
        
    def set_on_all(self, delay = 1):
        time.sleep(delay/2)
        self.port.write(self.on_all.encode())
        time.sleep(delay/2)        
   
    def set_off_1(self, delay = 1):
        time.sleep(delay/2)
        self.port.write(self.off_1.encode())
        time.sleep(delay/2)

    def set_off_2(self, delay = 1):
        time.sleep(delay/2)
        self.port.write(self.off_2.encode())
        time.sleep(delay/2)
        
    def set_off_all(self, delay = 1):
        time.sleep(delay/2)
        self.port.write(self.off_all.encode())
        time.sleep(delay/2)  
        
    def restart_1(self, time_ = 2):
        self.set_off_1()
        time.sleep(time_)
        self.set_on_1()
      
    def restart_2(self, time_ = 2):
        self.set_off_2()
        time.sleep(time_)
        self.set_on_2()
  
    def send_val(self, value):
        self.port.write(value.encode())




