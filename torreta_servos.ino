
#include <Servo.h>
Servo servo1;
Servo servo2;
Servo servo3;
int s1 = 90;//inicia el valor del servo en 90 grados
int s2 = 90;//inicia el valor del servo en 90 grados
int s3 = 90;//inicia el valor del servo en 90 grados
int giro = 5;  //valor de giro general
int a = 11;   //pin servo 1
int b = 12;   //pin servo 2
int c = 13;   //pin servo 3
int receivedInt;
void setup() {
  // Iniciamos el monitor serie para mostrar el resultado
  Serial.begin(115200);

  // Iniciamos los servos
  servo1.attach(a);
  servo2.attach(b);
  servo3.attach(c);

  //giro los servo a 90 grados de forma inicial
  servo1.write(90); //izquierda superior
  servo2.write(90);//derecha superior
  servo3.write(90);//centro

}

void loop() {
   recvInt();       //llama a la funcion y lee el valor
 PrintByInput();   //cllama a la funcion SWITCH 
 
  
}
void recvInt() { 
 while(Serial.available() == 0) {  } //esperta una entrada
 receivedInt = Serial.parseInt();   // asigna valor a la variable
  
}

void PrintByInput() {
 if (receivedInt != NULL) {       //revisa que sea valido el numero

switch (receivedInt) {            //asiga el valor a caso correspondiente
    case 1:
      Serial.println("aumentando eje x");     
      girar_mas_1(); 
      girar_menos_2();  
   break;

    case 2:
       Serial.println("disminuyendo eje x");
      girar_menos_1();
      girar_mas_2();
     break;
     
    case 3:
   Serial.println("aumentando eje z");     
      girar_menos_3();
     
    break;

    case 4:
      Serial.println("disminuyendo eje z");
      girar_mas_3();
     
    break;

    
    default:
     Serial.println("valor no valido");
     //Serial.println(receivedInt);
      
  } 
 receivedInt = NULL;
 }
}

////////////////////////////////servo 1
void girar_mas_1() {//aumenta servo 1
  s1 = s1+giro;
  if(s1 >= 126){//limitador
    s1=125;
  }
  Serial.println(s1);
  servo1.write(s1);
}
void girar_menos_1() {//disminuye servo 1
  s1 = s1-giro;
  if(s1 <= 66){//limitador
    s1=65;
  }
  Serial.println(s1);
  servo1.write(s1);
}
//////////////////////////////servo 2
void girar_mas_2() {//aumenta servo 2
  s2 = s2+giro;
  if(s2 >= 116){//limitador
    s2=115;
  }
  Serial.println(s2);
  servo2.write(s2);
}
void girar_menos_2() {//disminuye servo 2
  s2 = s2-giro;
  if(s2 <= 56){//limitador
    s2=55;
  }
  Serial.println(s2);
  servo2.write(s2);
}
//////////////////////////////servo 3
void girar_mas_3() {//aumenta servo 3
  s3 = s3+giro;
  if(s3 >= 181){//limitador
    s3=180;
  }
  Serial.println(s3);
  servo3.write(s3);
}
void girar_menos_3() {//disminuye servo 3
  s3 = s3-giro;
  if(s3 <= -1){//limitador
    s3=0;
  }
  Serial.println(s3);
  servo3.write(s3);
}
