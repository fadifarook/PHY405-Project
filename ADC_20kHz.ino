#include <TimerOne.h>

#define OUTPUT_PIN 9    
#define ANALOG_PIN A0   

#define PWM_FREQUENCY 20000  

unsigned long previousMicros = 0;
const unsigned long updateInterval = 100;  

void setup() {
    pinMode(OUTPUT_PIN, OUTPUT);

    Timer1.initialize(1000000 / PWM_FREQUENCY);  
    Timer1.pwm(OUTPUT_PIN, 512); 
}

void loop() {
    unsigned long currentMicros = micros();

    if (currentMicros - previousMicros >= updateInterval) {
        previousMicros = currentMicros;

        int sensorValue = analogRead(ANALOG_PIN);  
        Timer1.pwm(OUTPUT_PIN, sensorValue);       

}
