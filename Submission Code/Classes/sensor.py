"""
--------------------------------------------------------------------------
Sensor Driver
--------------------------------------------------------------------------
License:   
Copyright 2024 Marc De Guzman

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Potentiometer Driver for PocketBeagle

Software API:

  Potentiometer(pin)
    - Provide PocketBeagle pin that the potentiometer is connected

    get_temperature()
      - Gets temperature

    get_humidity()
      - Gets humidity

"""
import Adafruit_BBIO.ADC as ADC
import adafruit_ahtx0
import board

i2c = board.I2C()
aht10 = adafruit_ahtx0.AHTx0(i2c)

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

class Sensor():
    
    def get_temperature(self):
        """ Read temperatures """
        
        temp = aht10.temperature
        
        return temp
       

    # End def


    def get_humidity(self):
        """ Read humidities
        """
        
        humidity = aht10.relative_humidity
        
        return humidity

    # End def
    
    def cleanup(self):
        """Cleanup the hardware components."""
        # Nothing to do 
        pass        
        
    # End def

# End class



# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':
    import time

    print("Sensor Test")

    # Use a Keyboard Interrupt (i.e. "Ctrl-C") to exit the test
    print("Use Ctrl-C to Exit")
    
    try:
        while(1):
            # Test if temperature and humidity can be read
            temp = Sensor().get_temperature()
            humidity = Sensor().get_humidity()
            print(temp)
            print(humidity)
            time.sleep(7)
        
    except KeyboardInterrupt:
        pass

    print("Test Complete")
