// single line comment 
// compile: g++ intro.cpp 
// run: ./a.out

#include <iostream>

int main() { // need a function named main 
  std::cout << "Hello World!" << std::endl; 
  std::cout << "This is a C++ file" << std::endl; 
  
  int z = 30;
  int x = 20, y = 10;
  std:: cout << "Divide x/y: " << x/y << std::endl;
  
  std::string s = "Hello, this is a string.";
  std::cout << s << " Add string" << std::endl;

  bool app = true;
  std::cout << app << std::endl;
  return 0;
}


// Data types
int myNum = 5;               // Integer (whole number)
float myFloatNum = 5.99;     // Floating point number (7 decimal digits)
double myDoubleNum = 9.909;   // Floating point number (15 decimal digits)
char myLetter = 'I';         // Character *single quote
bool myBoolean = true;       // Boolean
std::string myText = "Hello";     // String
