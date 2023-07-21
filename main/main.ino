#include <LiquidCrystal.h>
#include <OneWire.h>
#include <DallasTemperature.h>

# define ONE_WIRE_BUS 2

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

LiquidCrystal lcd(4, 5, 6, 7, 8, 9);
const int padding = 0;
const int lcdWidth = 16;

void setup() {
  lcd.begin(16, 2);
  Serial.begin(9600);
}

void scrollText(int textLength, String text) {
    for (int i = 0; i <= textLength - lcdWidth; i++) {
    lcd.setCursor(padding, 0);
    lcd.print(text.substring(i, i + lcdWidth));
    delay(500); 
  }
}

void loop() {

  lcd.setCursor(0, 1);
  sensors.requestTemperatures();
  lcd.print(sensors.getTempCByIndex(0));
  lcd.setCursor(6, 1);
  lcd.print(("st. C"));
  delay(1000);

  String welcomeMessage = "Welcome to news dashboard!";
  int welcomeMessageLenght = welcomeMessage.length();

  scrollText(welcomeMessageLenght, welcomeMessage);
  delay(3000);

  if (Serial.available() > 0) {
    String dataFromComputer = Serial.readString();
    int textLength = dataFromComputer.length();
    if (textLength <= lcdWidth) {
      lcd.setCursor(padding, 0);
      lcd.print(dataFromComputer);
    } else {
      scrollText(textLength, dataFromComputer);
    }
  }



}
