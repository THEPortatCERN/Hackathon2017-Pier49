CC=gcc
CFLAGS=-Wall -lwiringPi
TARGET = blink

$(TARGET): $(TARGET).c
	gcc -o $@ $^ $(CFLAGS)

.PHONY: clean

clean:
	rm -f $(TARGET)
