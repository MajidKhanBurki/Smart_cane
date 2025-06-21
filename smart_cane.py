import RPi.GPIO as GPIO
import time

# Pin Assignments
IR_PIN        = 17     # IR sensor
BUZZER_PIN    = 23     # Buzzer
TRIG_PIN      = 22     # Ultrasonic trigger
ECHO_PIN      = 27     # Ultrasonic echo
TILT_PIN      = 24     # Tilt switch
TOUCH_PIN     = 25     # Touch switch

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(IR_PIN, GPIO.IN)
GPIO.setup(TILT_PIN, GPIO.IN)
GPIO.setup(TOUCH_PIN, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

GPIO.output(BUZZER_PIN, GPIO.HIGH)  # Buzzer OFF
GPIO.output(TRIG_PIN, False)

def get_distance():
    """Measure distance using ultrasonic sensor."""
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    timeout_start = time.time()
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()
        if pulse_start - timeout_start > 0.02:
            return None

    timeout_start = time.time()
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()
        if pulse_end - timeout_start > 0.02:
            return None

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    return round(distance, 2)

# Main loop
try:
    print("Monitoring IR, Ultrasonic, Tilt, and Touch sensors...")

    while True:
        ir_triggered = GPIO.input(IR_PIN) == 0
        tilt_triggered = GPIO.input(TILT_PIN) == 1  # HIGH = Tilted
        touch_triggered = GPIO.input(TOUCH_PIN) == 1  # HIGH = Touched
        distance = get_distance()
        ultrasonic_triggered = distance is not None and distance < 15

        if ir_triggered or ultrasonic_triggered or tilt_triggered or touch_triggered:
            if ir_triggered:
                print("IR: Obstacle detected!")
            if ultrasonic_triggered:
                print(f"Ultrasonic: Object at {distance} cm")
            if tilt_triggered:
                print("Tilt switch activated!")
            if touch_triggered:
                print("Touch switch activated!")

            GPIO.output(BUZZER_PIN, GPIO.LOW)  # Buzzer ON
            time.sleep(0.5)
            GPIO.output(BUZZER_PIN, GPIO.HIGH)  # Buzzer OFF
        else:
            print("No Obstacle, Tilt, or Touch detected.")
            GPIO.output(BUZZER_PIN, GPIO.HIGH)  # Ensure buzzer is OFF

        time.sleep(0.5)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()
