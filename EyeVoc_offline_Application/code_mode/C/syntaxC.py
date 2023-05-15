#Gets speech recognition engine, Speak() function,
from Engine import *


def void_func():
    speak("creating a void function")
    pyautogui.typewrite("void function() {\n//define function here \n    return 0;\n}")
    
def return_statment():
    speak("adding return")
    pyautogui.typewrite("return 0;")
    
def if_fun():
    speak("writing if")
    pyautogui.typewrite("if(){\n\n}")

def else_fun():
    speak("writing else")
    pyautogui.typewrite("else{\n\n}")
    
# def name_space_std():
#     speak("writing namespace")
#     pyautogui.typewrite("using namespace std;")
    
def int_func():
    speak("creating an integer function")
    pyautogui.typewrite("int function() {\n    //define function here\n    return 0;\n} ")
    
def char_func():
    speak("creating a char function")
    pyautogui.typewrite("char function() {\n    //define function here\n    return 0;\n} ")
    
def bool_func():
    speak("creating a boolean function")
    pyautogui.typewrite("bool function() {\n    //define function here\n    return 0;\n} ")
    
def main_func():
    speak("creating a main function")
    pyautogui.typewrite("int main() {\n    //define function here\n    return 0;\n} ")
    
def calc_C():
    speak("Writing a C program to perform basic arithmetic operations\n")
    pyautogui.typewrite('#include <stdio.h>\n\nint main() {\n   char operator;\n   double num1, num2, result;\n\n   printf("Enter an operator (+, -, , /): ");\n   scanf("%c", &operator);\n\n   printf("Enter two numbers: ");\n   scanf("%lf %lf", &num1, &num2);\n\n   switch(operator) {\n      case \'+\':\n         result = num1 + num2;\n         printf("%.2lf + %.2lf = %.2lf", num1, num2, result);\n         break;\n      case \'-\':\n         result = num1 - num2;\n         printf("%.2lf - %.2lf = %.2lf", num1, num2, result);\n         break;\n      case \'\':\n         result = num1 * num2;\n         printf("%.2lf * %.2lf = %.2lf", num1, num2, result);\n         break;\n      case \'/\':\n         if(num2 == 0)\n            printf("Error: Division by zero");\n         else {\n            result = num1 / num2;\n            printf("%.2lf / %.2lf = %.2lf", num1, num2, result);\n         }\n         break;\n      default:\n         printf("Error: Invalid operator");\n   }\n   return 0;\n}')

def array_C():
    speak("Performing operations on an array with user-specified length in C\n")
    pyautogui.typewrite('#include <stdio.h>\n\nint main() {\n   int length, i, sum = 0, max = 0;\n   \n   printf("Enter the length of the array: ");\n   scanf("%d", &length);\n   \n   int myArray[length];\n   \n   printf("Enter the elements of the array: ");\n   for(i = 0; i < length; i++) {\n      scanf("%d", &myArray[i]);\n      sum += myArray[i];\n      if(myArray[i] > max) {\n         max = myArray[i];\n      }\n   }\n   \n   printf("The elements of the array are: ");\n   for(i = 0; i < length; i++) {\n      printf("%d ", myArray[i]);\n   }\n   \n   printf("\\n");\n   printf("The sum of the elements of the array is %d\\n", sum);\n   printf("The maximum element of the array is %d\\n", max);\n   \n   return 0;\n}')

def area_C():
    speak("Calculating the area of a circle in C\n")
    pyautogui.typewrite('#include <stdio.h>\n#include <math.h>\n\nint main() {\n   float radius, area;\n   \n   printf("Enter the radius of the circle: ");\n   scanf("%f", &radius);\n   \n   area = M_PI * radius * radius;\n   \n   printf("The area of the circle is %.2f\\n", area);\n   \n   return 0;\n}')

def stdio_C():
    speak("Including the stdio.h library in C\n")
    pyautogui.typewrite('#include <stdio.h>\n')
    
def stdlib_C():
    speak("Including the stdlib.h library in C\n")
    pyautogui.typewrite('#include <stdlib.h>\n')

def string_C():
    speak("Including the string.h library in C\n")
    pyautogui.typewrite('#include <string.h>\n')

def math_C():
    speak("Including the math.h library in C\n")
    pyautogui.typewrite('#include <math.h>\n')

def time_C():
    speak("Including the time.h library in C\n")
    pyautogui.typewrite('#include <time.h>\n')

