#include <LiquidCrystal.h>

LiquidCrystal lcd(4, 5, 6, 7, 8, 9);
const int padding = 0;
const int lcdWidth = 16;

void setup() {
  lcd.begin(16, 2);
  Serial.begin(9600);
}

void loop() {
  String welcomeMessage = "Welcome to news dashboard!";
  int welcomeMessageLenght = welcomeMessage.length();
  for (int i = 0; i <= welcomeMessageLenght - lcdWidth; i++) {
    lcd.setCursor(padding, 0);
    lcd.print(welcomeMessage.substring(i, i + lcdWidth));
    delay(500); 
  }

  delay(3000);

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
