#include <wiringPi.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[]){
  char *p;
  const int PERIOD = 20000; // 50Hz

  if (argc != 3){
      printf("please specify: pulsewidth in useconds, amount of steps\n");
      return 0;
  }
  
  wiringPiSetup();
  pinMode (0, OUTPUT);

  int steps = strtol(argv[2], &p, 10);
  for (int i=0;i<steps;i++)
    {
      // wiring pi 21 should be BCM5
      // when using direct access (i.e. not AH phyton library), AH power needed and LEDs don't follow outputs
      int pin = 21;
      // LOW will send 5V pulse
      int pulse = strtol(argv[1], &p, 10);
      digitalWrite(pin, LOW);
      usleep(pulse);
      digitalWrite(pin,  HIGH);
      usleep(PERIOD-pulse);
    }
  return 0 ;
}
