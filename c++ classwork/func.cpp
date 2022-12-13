#include <iostream>


void print_hello(){ // use void to not use return 
  std::cout << "Hello World!\n";
  //return; // return nothing 
}


int add_two_numbers(int a, int b){
int c;
  c = a+b;
  return c;
  
}

int main()
{
// call function in main
print_hello();
int result = add_two_numbers(5,8);
std::cout << result << "\n";

  
  return 0;
}