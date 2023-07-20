import serial
import time


def main():

    ser = serial.Serial('COM5', 9600, timeout=1)
    try:
        while True:
            data = input("Enter the message to display on the Arduino LCD: ")
            ser.write(data.encode())
            time.sleep(1)
    except KeyboardInterrupt:
        ser.close()


if __name__ == '__main__':
    main()
