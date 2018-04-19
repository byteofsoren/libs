#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int StringNumberCounter(const char *text){
  /*
    This funciton return the number of itiger chars an array contains
  */
  unsigned int numbers = 0;
  unsigned int slength = strlen(text);    // The lengt of the var is stored. Used in the for loop later.
  unsigned int startPos = 0;

  if (text[0] == '-') numbers++;  // This checs for a negative sign in the begining of the char array.
  for (unsigned int i = startPos; i < slength; i++) {     //Loop the array for numbers and if so count them.
    if (((text[i] >= '0') && (text[i] <= '9')) || text[i] == '.' || text[i] == ',') numbers++;
  }
  return numbers;
}

int StrToInt(const char *text, int *error){
  /*
    This function returns the char string as an string.
    the error is 0 if no problems ocured.
  */
  *error = 0;
  unsigned int numbers = 0;
  unsigned int slength = strlen(text);
  numbers = StringNumberCounter(text);
  if (numbers != slength ) *error = 1;
  return atoi(text);
}

float StrToFloat(const char *text, int *error){
  /*
    Same as abowe but for floats.
    it hawe an intresting bug/feature try TunaStrToFloat("12e123", error);
  */
  *error = 0;
  unsigned int numbers = 0;
  unsigned int slength = strlen(text);
  numbers = StringNumberCounter(text);
  if (numbers  != slength ) *error = 1;
  return atof(text);
}
