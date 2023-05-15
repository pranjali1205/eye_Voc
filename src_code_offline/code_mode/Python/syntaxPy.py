#Gets speech recognition engine, Speak() function,
from Engine import *
    
def import_pyttsx3():
    speak("importing pyttsx3 library")
    pyautogui.typewrite("import pyttsx3\n")

def import_pyautogui():
    speak("importing py auto graphical user interface")
    pyautogui.typewrite("import pyautogui\n")
 
def import_pyaydio():
    speak("importing py audio library")
    pyautogui.typewrite("import pyaudio\n")

def import_speech():
    speak("importing Speech Recognition module")
    pyautogui.typewrite("import speech_recognition")
     
def print_py():
    speak("calling print function")
    pyautogui.typewrite("print()")


def declare_intvariable_py():
    speak("Declaring int variable")
    pyautogui.typewrite("x=int()")


def declare_floatvariable_py():
    speak("Declaring float variable")
    pyautogui.typewrite("x=float()")


def declare_strgvariable_py():
    speak("Declaring string variable")
    pyautogui.typewrite("x=str()")


def typeOfVariable_py():
    speak("Writing type function ")
    pyautogui.typewrite("type()")


def list_py():
    speak("defining a list")
    pyautogui.typewrite('List =[""]')


def set_py():
    speak("defining a set")
    pyautogui.typewrite('set ={""}')


def string_py():
    speak("defining a string")
    pyautogui.typewrite('string =""')


def array_py():
    speak("defining a array in python")
    pyautogui.typewrite(A=[""])


def touple_py():
    speak("defining a touple in python")
    pyautogui.typewrite('t=("")')


def stack_py():
    speak("Defining a stack in python")
    pyautogui.typewrite("st=[]\n")
    pyautogui.typewrite("st.append('')\n")
    pyautogui.typewrite("st.append('')\n")
    pyautogui.typewrite("st.append('')\n")


def queue_py():
    speak("Defining a queue in python")
    pyautogui.typewrite("qu=[]\n")
    pyautogui.typewrite("qu.append('')\n")
    pyautogui.typewrite("qu.append('')\n")
    pyautogui.typewrite("qu.append('')\n")


def linkedlist_py():
    speak("Defining a linked list in python")
    pyautogui.typewrite("\nclass Node:\n\n    # Function to initialise the node object\n    def _init(self, data):\n        self.data = data  # Assign data\n        self.next = None  # Initialize next as null\n\n\n # Linked List class contains a Node object\n class LinkedList:\n\n    # Function to initialize head\n    def __init(self):\n        self.head = None\n\n    # This function prints contents of linked list\n    # starting from head\n    def printList(self):\n        temp = self.head\n        while (temp):\n            print(temp.data)\n            temp = temp.next\n\n\n # Code execution starts here\n if __name_ == '_main_':\n\n    # Start with the empty list \n    list = LinkedList()\n\n   list.head = Node(1)\n    second = Node(2)\n    third = Node(3)\n\n    list.head.next = second  # Link first node with second\n    second.next = third  # Link second node with the third node\n\n    list.printList()\n")


def createClass_py():
    speak("Creating a class in python")
    pyautogui.write("\n\nclass Person:\n  def _init_(mysillyobject, name, age):\n    mysillyobject.name = name\n    mysillyobject.age = age\n\n  def myfunc(abc):\n    print('Hello my name is ' + abc.name)\n\np1 = Person('John', 36)\np1.myfunc()\n")


def if_statement_py():
    speak("inititating if statement in python")
    pyautogui.typewrite("if():\n\t")


def elif_statement_py():
    speak("Initiating elif statement in python")
    pyautogui.typewrite("elif():\n\t")


def else_statement_py():
    speak("Initiating else statement in python")
    pyautogui.typewrite("else():\n\t")

def insert_py():
    speak("calling insert function in python")
    pyautogui.typewrite(".insert( , )")


def append_py():
    speak("calling append function in python")
    pyautogui.typewrite(".append()")


def extendlist_py():
    speak("calling extend function in python")
    pyautogui.typewrite(".extend()")


def removelist_py():
    speak("calling remove function in python")
    pyautogui.typewrite(".remove()")
# pop function can be used for both list and stack etc


def pop_py():
    speak("calling pop function in python")
    pyautogui.typwrite(".pop()")


def clear_py():
    speak("calling clear function in python")
    pyautogui.typewrite(".clear()")


def uppercase_py():
    speak("calling uppercase funtion in python")
    pyautogui.typewrite(".upper()")


def lowercase_py():
    speak("calling lowercase function in python")
    pyautogui.typewrite(".lower()")


def reverse_py():
    speak("calling reverse function in python")
    pyautogui.typewrite(".reverse()")


def sort_py():
    speak("calling sort function in python")
    pyautogui.typewrite(".sort()")

# desort is sort in descending order


def Desort_py():
    speak("calling descending sort function in python")
    pyautogui.typewrite("reverse = True")


def Customizesort_py():
    speak("calling customized sort function in python")
    pyautogui.typewrite(".sort(key=)")


def copy_py():
    speak("calling copy function in python")
    pyautogui.typewrite(".copy()")


def count_py():
    speak("calling count function in python")
    pyautogui.typewrite(".count()")


def length_py():
    speak("calling length function in python")
    pyautogui.typewrite("len()")


def index_py():
    speak("calling index function in python")
    pyautogui.typewrite("index()")

# set functions


def add_py():
    speak("calling add function in python")
    pyautogui.typewrite(".add()")


def update_py():
    speak("calling update function in python")
    pyautogui.typewrite(".upadte()")


def discard_py():
    speak("calling discard function in python")
    pyautogui.typewrite(".discard()")


def union_py():
    speak("calling union function in union")
    pyautogui.typewrite(".union()")


def forLoop_py():
    speak("initiaitng for loop in python ")
    pyautogui.typewrite("for i in range() : ")


def whileLoop_py():
    speak("initiaitng while loop in python ")
    pyautogui.typewrite("while():")


def createFunction_py():
    speak("Creating a funtion in python")
    pyautogui.typewrite("def myfunc():")


def datetime_py():
    speak("calling datetime function in python")
    pyautogui.typewrite("x = datetime.datetime.now()")
    
def min_py():
    speak("calling minimum function in python")
    pyautogui.typewrite("min( , , )")


def max_py():
    speak("calling maximum function in python")
    pyautogui.typewrite("max( , , )")


def abs_py():
    speak("calling absolute function in python")
    pyautogui.typewrite("abs( )")


def pow_py():
    speak("calling power function in python")
    pyautogui.typewrite("pow( , )")


def comnts_py():
    speak("initiating comments in python")
    pyautogui.hotkey("#")

def sqrt_py():
    speak("calling square root function in python")
    pyautogui.typewrite("math.sqrt( )")


def floor_py():
    speak("calling floor function in python")
    pyautogui.typewrite("math.floor( )")


def ceil_py():
    speak("calling ceil functino in python")
    pyautogui.typewrite("math.ceil( )")


def pi_py():
    speak("calling pi constant in python")
    pyautogui.typewrite("math.pi")


def tryExpect_py():
    speak("calling try statement in python")
    pyautogui.typewrite("try:\n\t  \nexcept:\n\t  \nfinally:\n")


def input_py():
    speak("calling input function in python")
    pyautogui.typewrite('input("")')


def open_py():
    speak("calling open function in python")
    pyautogui.typewrite('open("", "" )')


def close_py():
    speak("calling close function in python")
    pyautogui.typewrite('close(" ")')


def read_py():
    speak("calling read function in python")
    pyautogui.typewrite("read( )")


def readline_py():
    speak("calling readline function in python")
    pyautogui.typewrite("readline( )")


def writeToFile_py():
    speak("writing to an existing file in python")
    pyautogui.typewrite("f = open("", "")\nf.write("")\nf.close()")


def deleteFile_py():
    speak("Deleting existing file in python")
    pyautogui.typewrite(
        "if os.path.exists(''):\n  os.remove('')\nelse:\n  print('The file does not exist')")


def deleteFolder_py():
    speak("Deleting existing folder in python")
    pyautogui.typewrite("os.rmdir('')")
    
    
    
    
    
    