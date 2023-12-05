
SYSTEM_THREAD(ENABLED);
SYSTEM_MODE(SEMI_AUTOMATIC);


void setup() {
    Serial.begin(9600);
    Serial1.begin(9600); // Initialize serial communication

}

void loop() {
        Serial1.print("R");

        delay(1000);

        Serial.println(Serial1.readString());

}
