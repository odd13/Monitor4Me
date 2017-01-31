import spi
from time import sleep


#At the beginning of the program open up the SPI port.#At the beginning of the program open up the SPI port.
#this is port /dev/spidevX.Y
#Being called as as spi.SPI(X,Y)

a = spi.SPI(0,1)

print "PY: initialising SPI mode, reading data, reading length . . . \n"

#This is my data that I want sent through my SPI bus#This is my data that I want sent through my SPI bus




data = ["FF7F40009554"]



#Calculates the length, and devides by 2 for two bytes of data sent.#Calculates the length, and devides by 2 for two bytes of data sent.
length_data = len(data[0])/2

#transfers data string#transfers data string



print 'Value transfered to C spimodule:',data




a.transfer(data[0], length_data)



#At the end of your program close the SPI port#At the end of your program close the SPI port





a.close()