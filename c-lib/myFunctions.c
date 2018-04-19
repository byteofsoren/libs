#include <stdio.h>
#include <time.h>
#include <stdlib.h>
//#include "myFunctions.h"
#include "myFunctions.h"

int myRand(int min, int max){
// This is my random number generator
  int result = 0 , low = 0 ,hig = 0;
  static int oneTime = 0;   // Srand patch

  if ( min < max) {
    low = min;
    hig = max + 1;        // include the max result in the output
  }  else {
    low = max + 1;        // include the max result in the output
    hig = min;
  }
  if (oneTime == 0) {     // you only run srand 1 time.
    srand(time(NULL));
    oneTime++;
  }
  result = rand() % (hig - low)+ low;  /* What this do is better expalined with an exampel.
  Lest say you get;
    rand()=234532   hig=20    low=5
    first evaluet (hig-low)=15
    then 234532 % 15 = 7
    last 7 + 5 = 12  */
  return result;
}

int doitAgain(const char *prompt){
    // This function lets the programmer to "safly" ask the user if they want
    // to play the gama aiain. The promt variable in the input is wahats sown
    // on the screen. For example.
    // Do you want to play the game again (y/n):
    // if y for yes then  return 1 
    // if n for no then return 0
  char buffer[10];
  //char temp[1] = {' '};
  char tmp = ' ';
  int containsEnter = 0;
  do {
    printf("%s (y/n): ", prompt);
    fgets(buffer, 10, stdin);
    // After a user have enterd a string we check if the buffer contains an enter. if so then increase ContainsEnter and break.
    for (int i = 0; i <= 10; i++) {
      if (buffer[i] == '\n') {
        containsEnter++;
        break;
      } else if ( buffer[i] == '\0'){
        break;
      }
    }
    // This part of the code strips stdin of the buffer overflow if buffer did not contain an \n char.
    //printf("containsEnter=%d\n", containsEnter  );
    if (containsEnter == 0){
      printf("\e[38;5;9m[Hal9000]:\e[38;5;156m The input: \e[32m%s\e[38;5;208m", buffer);
      while (1){
        tmp = getchar();
        if( tmp == '\n') break;
        else if (tmp == '\0') break;
        printf("%c", tmp);
      }
      printf("\n\e[38;5;9m[Hal9000]:\e[38;5;156m Created an unfortunate buffer overflow.\n\e[37m" );
    }
    // The only way to exit this loop is to have the first char eater an y or n and also have an enter in the buffer.
    if ((buffer[0] == 'y' || buffer[0] == 'Y') && containsEnter != 0) {
      containsEnter = 0;
      return 1;
    }
    else if ((buffer[0] == 'n' || buffer[0] == 'N') && containsEnter != 0) {
      containsEnter = 0;
      return 0;
    }else{
      printf("\e[38;5;9m[Hal9000]:\e[38;5;156m I'm sorry, Dave. I'm afraid I \e[38;5;208mdon't \e[38;5;156muderstand you!\e[37m\n");
    }
  } while(1);
  containsEnter = 0;
  return 0;
}
