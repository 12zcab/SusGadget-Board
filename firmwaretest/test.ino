#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

// 0.91 inch OLED Display Configuration
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 32  // Changed to 32 for 0.91" screen
#define OLED_RESET     -1 
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// I2C Pin Definitions
const int SDA_PIN = 1;
const int SCL_PIN = 2;

// Peripherals Pin Definitions
const int BUZZER_PIN = 8;
const int POT_PIN = 9;

// JS5208 Joystick Mapped Pins
const int JS_PIN_1 = 4;
const int JS_PIN_2 = 3;
const int JS_PIN_4 = 5;
const int JS_PIN_5 = 6;
const int JS_PIN_6 = 7;

void setup() {
  Serial.begin(115200);

  // Configure Joystick Inputs (Using Pullup)
  pinMode(JS_PIN_1, INPUT_PULLUP);
  pinMode(JS_PIN_2, INPUT_PULLUP);
  pinMode(JS_PIN_4, INPUT_PULLUP);
  pinMode(JS_PIN_5, INPUT_PULLUP);
  pinMode(JS_PIN_6, INPUT_PULLUP);

  // Configure Outputs and Analog Inputs
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(POT_PIN, INPUT);

  // Initialize Custom I2C Bus
  Wire.begin(SDA_PIN, SCL_PIN);

  // Initialize OLED Display (0.91" usually uses I2C address 0x3C)
  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println(F("OLED 128x32 initialization failed!"));
    for(;;); 
  }

  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0,12); // Vertically centered for the first message
  display.println(F("System Ready..."));
  display.display();
  delay(1000);
}

void loop() {
  // Read Potentiometer
  int potValue = analogRead(POT_PIN);

  // Read Joystick States (LOW = Pressed)
  bool js1 = digitalRead(JS_PIN_1) == LOW;
  bool js2 = digitalRead(JS_PIN_2) == LOW;
  bool js4 = digitalRead(JS_PIN_4) == LOW;
  bool js5 = digitalRead(JS_PIN_5) == LOW;
  bool js6 = digitalRead(JS_PIN_6) == LOW;

  // Sound Buzzer if Joystick 1 is pressed
  if (js1) {
    digitalWrite(BUZZER_PIN, HIGH);
  } else {
    digitalWrite(BUZZER_PIN, LOW);
  }

  // Update 128x32 OLED Screen
  display.clearDisplay();
  display.setCursor(0, 0);
  
  // Line 1: Potentiometer data
  display.print(F("POT: "));
  display.println(potValue);
  
  // Line 2: Joystick active states grouped tightly to fit the 32px height
  display.print(F("JS: "));
  display.printf("%d %d %d %d %d", js1, js2, js4, js5, js6);
  
  // Line 3: Small visual status bar based on Potentiometer value
  int barWidth = map(potValue, 0, 4095, 0, 128);
  display.fillRect(0, 26, barWidth, 4, SSD1306_WHITE);
  
  display.display();
  delay(100); 
}
