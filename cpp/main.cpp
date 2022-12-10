#include <iostream>

// function that understands an if statement 
void evenOdd(int num){
  if (num%2 == 0){
    std::cout << num << " is even.\n";
  }
  else {
    std::cout << num << " is odd.\n";
  } 
}

// function that understands a loop 
int countUpto (int num){
  int i = 0;
  while (i < num){
   std::cout << i << ", ";
   i = i+1;
  }
  std::cout << std::endl;
  return i;
}

int main()
{ 
  std::cout << "Hello World!\n"; // prints hello word
  evenOdd(198356); // calls evenOdd function
  countUpto(16); // calls countUp fucntion 
return 0;  
}

