#include <SPI.h>
#include <MFRC522.h>


#define duration_time 2000
#define approvedPin 2
#define rejectedPin 4
#define RST 14
#define SS_SDA 5

const byte UID[] = {0xDA, 0x66, 0xB1, 0x68};
const byte UID1[] = {0x29, 0x66, 0xCA, 0x7A};



MFRC522 rfid(SS_SDA, RST);
MFRC522::MIFARE_Key key;
boolean state = false;
long time_;


void setup() {
  Serial.begin(115200);
  SPI.begin();
  rfid.PCD_Init();
  pinMode(2, OUTPUT);
  pinMode(4, OUTPUT);
}

void loop() {
  if(rfid.PICC_IsNewCardPresent() && rfid.PICC_ReadCardSerial()){
    if( rfid.uid.uidByte[0] == UID[0] &&
        rfid.uid.uidByte[0] == UID[0] && 
        rfid.uid.uidByte[0] == UID[0] &&
        rfid.uid.uidByte[0] == UID[0]){
          Serial.println("Authorization granted!");
          digitalWrite(2, HIGH);
          digitalWrite(4, LOW);
          state = true;
          time_ = millis() + duration_time;
        }
        else{
          Serial.println("Invalid credentials!");
          state = false;
          digitalWrite(4, HIGH);
          digitalWrite(2, LOW);
        }
        rfid.PICC_HaltA();
        rfid.PCD_StopCrypto1();
  }
  if(state && duration_time < millis()){
    state = false;
  }

}