void setup() {
// シリアルポートを開き,通信速度を9600bpsに設定
Serial.begin(9600);
}
void loop() {
// 1000ms(1秒待ち)
delay(1000);
// シリアル通信でtestを改行ありで出力(改行なしの場合はSerial.print)
Serial.println("test");
}

int val=0; //入力される値を格納する為の変数
void setup() {
Serial.begin(9800); //モニターに出力するための設定
}
void loop() {
//ANALOG INの0番ピンからデータを受け付ける
val=analogRead(0);
Serial.println(val/4); //入力された値をモニターに出力
delay(100);
}