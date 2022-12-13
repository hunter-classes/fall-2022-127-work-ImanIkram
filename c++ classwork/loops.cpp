#include <iostream>

int main()
{
  int i;
  i = 0;
  while (i < 10){
    std::cout << i << ", ";
    i=i+1;
  }
  std::cout << std::endl;

  //While loop
  while (i > 0){
    i = i-1;
  std::cout << i << "\n";
    }
  std::cout << std::endl;

  // Eample
  char go_again = 'y';
  while (go_again =='y'){
    std::cout << "Continue? ";
    std::cin >> go_again; 
  }
  std::cout << std::endl; 

  // For loop
  for (int i = 0; i <10; i=i+1){
    std::cout << i << ", ";
  }
  std::cout << std::endl; 
  
  return 0;
}


