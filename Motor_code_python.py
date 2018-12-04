from Solver import *
import serial

arduinoSerialData = serial.Serial('/dev/ttyACM0', 9600)

def foo (cubestring):
    solution = s.solve(cubestring)
    solution = solution.split(" ")
    del solution[-1]
    for x in solution:
        x +='x';
        x = x.encode()
        print(x)
        arduinoSerialData.write(x)
    print(solution)


if __name__ == '__main__':
    with open("solution.txt", 'r') as fp:
        foo(str(fp.read()))
