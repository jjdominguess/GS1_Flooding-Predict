#include <Arduino.h>
#include <DHT.h>
#include <Adafruit_Sensor.h>

// Definição dos pinos
#define TRIG_PIN 5   // Pino Trigger do HC-SR04
#define ECHO_PIN 18  // Pino Echo do HC-SR04
#define DHT_PIN 4    // Pino do DHT22
#define DHT_TYPE DHT22
#define LED_PIN 2 
// Inicializa os sensores
DHT dht(DHT_PIN, DHT_TYPE);

void setup() {
    Serial.begin(115200);
    pinMode(TRIG_PIN, OUTPUT);
    pinMode(ECHO_PIN, INPUT);
    pinMode(LED_PIN, OUTPUT);
    dht.begin();
}

void loop() {
    // Medindo distância do HC-SR04
    digitalWrite(TRIG_PIN, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG_PIN, LOW);

    long duration = pulseIn(ECHO_PIN, HIGH);
    float distance_cm = (duration * 0.034 / 2) + (random(-10, 35) * 10); // Converte tempo de pulso para cm
    
    if (distance_cm > 550) {
        digitalWrite(LED_PIN, HIGH);
    } else {
        digitalWrite(LED_PIN, LOW);
    }

    // Leitura do DHT22
    int temperature = dht.readTemperature() + (random(-8, 8)/10);
    float humidity = dht.readHumidity() + random(0, 40);

    // Exibe os dados no monitor serial
    Serial.print("Nivel do Rio: ");
    Serial.print(distance_cm);
    Serial.println(" cm");

    Serial.print("Temperatura: ");
    Serial.print(temperature);
    Serial.println(" °C");

    Serial.print("Umidade: ");
    Serial.print(humidity);
    Serial.println(" %");

    Serial.print("LED: ");
    Serial.print(distance_cm > 550? "Risco de Inundação": "Nível Normal");

    Serial.println("-----------------------");
    delay(2000); // Aguarde antes da próxima leitura
}
