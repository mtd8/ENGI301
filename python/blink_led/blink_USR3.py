"""
--------------------------------------------------------------------------
Blink LED
--------------------------------------------------------------------------
Author: Marc De Guzman (mtd8 @ rice dot edu)

Copyright 2024, Marc De Guzman

License:   

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Function that will blink the USR3 LED on the PocketBeagle at 5 Hz

Use Control C to stop the function

---------------
"""

import time
import Adafruit_BBIO.GPIO as GPIO

LED = "USR3"

def blink():
    try:
        GPIO.setup(LED, GPIO.OUT)

        # Blinks the LED at 5 Hz - Total Cycle should be 0.2 seconds
        while True:
            # Turns the LED on
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(0.1)  # 0.1 seconds on

            # Turns the LED off
            GPIO.output(LED, GPIO.LOW)
            time.sleep(0.1)  # 0.1 seconds off
        