"""
--------------------------------------------------------------------------
Temperature/Humidity Sensor
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

Requirements:
  - Passively checks temperature and humidity and displays
  - Will play alarm/LED if the readings are not in the ranges specified by the thresholds
  - Can adjust thresholds with buttons. To +1 on a threshold, click briefly. To -1 on a threshold, hold for more than 1 second.
  - Green buttons - temperature tresholds; yellow buttons - humidity thresholds
  - Can silence alarm with blue button

"""
import time
import ht16k33 as HT16K33
import sensor as SENSOR
import led as LED
import button as BUTTON
import buzzer as BUZZER
import threading

class Code():
    reset_time = None
    button     = None
    display    = None
    display2   = None
    
    
    def __init__(self, reset_time=1.0, button="P2_2", button2="P2_8", button3="P2_17",button4="P2_19", i2c_bus=1, i2c_bus2 = 2, i2c_address=0x70, i2c_address2=0x71):
        """ Initialize variables and set up displays, buttons, buzzers, and LEDs """
        self.reset_time = reset_time
        self.display    = HT16K33.HT16K33(i2c_bus, i2c_address)
        self.display2   = HT16K33.HT16K33(i2c_bus2, i2c_address)
        self.display3   = HT16K33.HT16K33(i2c_bus2, i2c_address2)
        self.display4   = HT16K33.HT16K33(i2c_bus, i2c_address2)
        self.tempbuzzer = BUZZER.Buzzer("P1_36")
        self.humiditybuzzer = BUZZER.Buzzer("P1_33")
        self.sensor     = SENSOR.Sensor()
        self.ledhumidity    = LED.LED("P2_4")
        self.ledtemp    = LED.LED("P2_6")
        self.ledsilence = LED.LED("P1_34")
        self.button = BUTTON.Button(button)
        self.button2 = BUTTON.Button(button2)
        self.button3 = BUTTON.Button(button3)
        self.button4 = BUTTON.Button(button4)
        self.buttonlock = BUTTON.Button("P1_10")
        self.lock = False
        self.tthresholdlow = 18
        self.tthresholdhigh = 30
        self.hthresholdlow = 30
        self.hthresholdhigh = 70
        self.reset_time = 1
        self._setup()
        
    
    # End def
    
    
    def _setup(self):
        """Setup the hardware components."""

        # Initialize Display to "0000"
        self.display.clear()
    
    # End def
    

    def runtempandhumidity(self):
        """Execute the main program."""
        
        import time
        button_press_time = 0
        button2_press_time = 0
        while(1):

            # Reads temperature and humidity - functions imported from sensor class
            temp = self.sensor.get_temperature()
            temp = round(temp,2)
            
            humidity = self.sensor.get_humidity()
            humidity = round(humidity,1)
            
            # Update the display
            self.display.updatefloat(temp)
            self.display2.updatefloat(humidity)
            self.display4.set_digit(1, (self.tthresholdlow % 10))
            self.display4.set_digit(0, (self.tthresholdlow // 10) % 10)
            self.display4.set_digit(3, (self.tthresholdhigh % 10))
            self.display4.set_digit(2, (self.tthresholdhigh // 10) % 10)
            
            self.display3.set_digit(1, (self.hthresholdlow % 10))
            self.display3.set_digit(0, (self.hthresholdlow // 10) % 10)
            self.display3.set_digit(3, (self.hthresholdhigh % 10))
            self.display3.set_digit(2, (self.hthresholdhigh // 10) % 10)
            
            # Checks if temp/humidity is within the threshold
            if not self.lock:
                self.ledsilence.off()
            else:
                self.ledsilence.on()
        
            if temp < self.tthresholdlow or temp > self.tthresholdhigh:
                self.ledtemp.on()
                if not self.lock:
                    self.tempbuzzer.play(440, 0.2, True)
            else:
                self.ledtemp.off()
            
            if humidity < self.hthresholdlow or humidity > self.hthresholdhigh:
                self.ledhumidity.on()
                if not self.lock:
                    self.humiditybuzzer.play(440, 0.2, True)
            else:
                self.ledhumidity.off()
            
            time.sleep(1)
            
            
            
    # End def
    
    def buttonthread(self):
        # Button anticipates for a press from function in button class
        # Will record button press time to determine action
        
        while True:
            self.button.wait_for_press()
            self.button_press_time = code.button.get_last_press_duration()
            print(self.button_press_time)
            
            if self.button_press_time < self.reset_time:
                self.tthresholdlow += 1
            else:
                self.tthresholdlow -= 1
                
    # End def
    
    def button2thread(self):
        # Button anticipates for a press from function in button class
        # Will record button press time to determine action
        
        while True:
            self.button2.wait_for_press()
            self.button2_press_time = code.button2.get_last_press_duration()
            print(self.button2_press_time)
            
            if self.button2_press_time < self.reset_time:
                self.tthresholdhigh += 1
            else:
                self.tthresholdhigh -= 1
    
    # End def
                
    def button3thread(self):
        # Button anticipates for a press from function in button class
        # Will record button press time to determine action
        
        while True:
            self.button3.wait_for_press()
            self.button3_press_time = code.button3.get_last_press_duration()
            print(self.button3_press_time)
            
            if self.button3_press_time < self.reset_time:
                self.hthresholdlow += 1
            else:
                self.hthresholdlow -= 1
                
    # End def
    
    def button4thread(self):
        # Button anticipates for a press from function in button class
        # Will record button press time to determine action
        
        while True:
            self.button4.wait_for_press()
            self.button4_press_time = code.button4.get_last_press_duration()
            print(self.button4_press_time)
            
            if self.button4_press_time < self.reset_time:
                self.hthresholdhigh += 1
            else:
                self.hthresholdhigh -= 1
                
    # End def
    
    def toggle_lock(self):
        # Button anticipates for a press from function in button class
        # Will switch the state of the lock variable on press
        
        while True:
            self.buttonlock.wait_for_press()
            if not self.lock:
                self.lock = True
                print("You locked it")
            else:
                self.lock = False
                print("You unlocked it")
    
    # End def


    def cleanup(self):
        """Cleanup the hardware components."""
        
        # Set Display to something fun to show program is complete
        self.display.text("done")
        self.display2.text("done")
        
    # End def

# End class



# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':

    print("Program Start")

    # Create instantiation of the code class
    code = Code()

    # Initialize the threads
    temp_thread = threading.Thread(target=code.runtempandhumidity)
    button_thread = threading.Thread(target=code.buttonthread)
    button2_thread = threading.Thread(target=code.button2thread)
    button3_thread = threading.Thread(target=code.button3thread)
    button4_thread = threading.Thread(target=code.button4thread)
    buttonlock_thread = threading.Thread(target=code.toggle_lock)

    # Start the threads
    temp_thread.start()
    button_thread.start()
    button2_thread.start()
    button3_thread.start()
    button4_thread.start()
    buttonlock_thread.start()
        
    try:
        while True:
            pass
        
    except KeyboardInterrupt:
        
        # Closes all threads when control C is used on Mac
        
        code.cleanup()
        temp_thread.join()
        button_thread.join()
        button2_thread.join()
        button3_thread.join()
        button4_thread.join()
        buttonlock_thread.join()

    print("Program Complete")
