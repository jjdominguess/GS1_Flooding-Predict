#include <Arduino.h>
#include <DHT.h>
#include <Adafruit_Sensor.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <PubSubClient.h>

// Definição dos pinos
#define TRIG_PIN 5   // Pino Trigger do HC-SR04
#define ECHO_PIN 18  // Pino Echo do HC-SR04
#define DHT_PIN 4    // Pino do DHT22
#define DHT_TYPE DHT22
#define LED_PIN 2 

// Inicializa os sensores
DHT dht(DHT_PIN, DHT_TYPE);
WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
    Serial.begin(9600);
    Serial.println("Conectando com WIFI...");
    WiFi.begin("Wokwi-GUEST", "",6);
    while (WiFi.status() != WL_CONNECTED) {
        delay(100);
        Serial.println(".");
    }
    Serial.println("Conectado ao WIFI!");
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
    Serial.println(distance_cm > 550? "Risco de Inundação": "Nível Normal");

    Serial.println("-----------------------");

    String payload = "{\"Chuva_mm\": " + String(distance_cm) +
                     ", \"Umidade_%\": " + String(humidity) +
                     ", \"Temperatura_C\": " + String(temperature) +
                     ", \"Nivel_rio_m\": " + String(distance_cm / 100) + "}";

    client.publish("enchente/sensores", payload.c_str());

    // Envia os dados para a API Flask via HTTP POST
    if (WiFi.status() == WL_CONNECTED) {
        HTTPClient http;
        if (http.begin(espClient, "host.wokwi.internal", 5000, "/predict")) {
            http.addHeader("Content-Type", "application/json");
            String json = "{\"Chuva_mm\": " + String(distance_cm) +
                        ", \"Umidade_%\": " + String(humidity) +
                        ", \"Temperatura_C\": " + String(temperature) +
                        ", \"Nivel_rio_m\": " + String(distance_cm / 100) + "}";
            Serial.println("Preparando para enviar para a API...");
            Serial.println(json);
            int httpResponseCode = http.POST(json);
            Serial.print("Resposta do servidor: ");
            Serial.print(http.errorToString(httpResponseCode));
            Serial.print("Código de resposta: ");
            Serial.println(httpResponseCode);
            Serial.println("Envio concluído.");
            http.end();
        }
    }

    delay(5000);
}
