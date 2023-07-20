#include <LiquidCrystal.h>

LiquidCrystal lcd(4, 5, 6, 7, 8, 9);
const int padding = 0;
const int lcdWidth = 16;

void setup() {
  lcd.begin(16, 2);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String dataFromComputer = Serial.readString();

    int textLength = dataFromComputer.length();
    if (textLength <= lcdWidth) {
      lcd.setCursor(padding, 0);
      lcd.print(dataFromComputer);
    } else {
      for (int i = 0; i <= textLength - lcdWidth; i++) {
        lcd.setCursor(padding, 0);
        lcd.print(dataFromComputer.substring(i, i + lcdWidth));
        delay(500); 
      }
    }
  }
}
