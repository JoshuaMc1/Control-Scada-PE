#include <stdio.h>
#include <wiringPi.h>

#define GPIO_PIN_OFF 2
#define GPIO_PIN_ON 0

int status = 0;

int main(void) {
    if (wiringPiSetup() == -1) {
        fprintf(stderr, "WiringPi fallo\n");
        
        return 1;
    }

    pinMode(GPIO_PIN_OFF, OUTPUT);
    digitalWrite(GPIO_PIN_OFF, HIGH);

    pinMode(GPIO_PIN_ON, OUTPUT);
    digitalWrite(GPIO_PIN_ON, LOW);

    FILE *file = fopen("/home/sps/examen/status/status.txt", "w");

    if (file == NULL) {
        perror("Error al abrir el archivo");
        return 1;
    }

    fprintf(file, "%d\n", status);
    fclose(file);

    return 0;
}
