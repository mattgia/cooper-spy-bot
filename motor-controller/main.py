from dotenv import load_dotenv
load_dotenv()


import motor_service
from time import sleep

motor_service.forward()
sleep(1)
motor_service.backward()
sleep(2)
motor_service.forward()
sleep(1)

motor_service.gpio_reset()
