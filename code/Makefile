CC=gcc
CFLAGS=-Wall -lwiringPi
TARGET = servo

$(TARGET): $(TARGET).c
	gcc -o $@ $^ $(CFLAGS)

.PHONY: clean

clean:
	rm -f $(TARGET)
