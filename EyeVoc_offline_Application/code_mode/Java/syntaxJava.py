#Gets speech recognition engine, Speak() function, and pylibraries 
from Engine import *


# Following are some Fuctions that prints corresponding syntaxes in Java

def comnts_jav():
    speak("initiating comments in java")
    pyautogui.typewrite("//   Comments // ")
    
def private_java():
    speak("public")
    pyautogui.typewrite("private")

def protected_java():
    speak("protected")
    pyautogui.typewrite("protected")
    
def public_java():
    speak("public")
    pyautogui.typewrite("public")
def for_loop():
    speak("for loop")
    pyautogui.typewrite("for (int i = 0; i < 5; i++) {\ncout << i;\n}" )
    
def while_loop():
    speak("while loop")
    pyautogui.typewrite("while(){\n\n\t}" )
    
def do_while_loop():
    speak("do while loop")
    pyautogui.typewrite("do(){\n\n\t}while()" )
    
def util_java():
    speak("initialize library in java")
    pyautogui.typewrite('import java.util.*;')
    
def sql_java():
    speak("initialize sql in java")
    pyautogui.typewrite('import java.sql.*;')
    
def javafx_java():
    speak("initialize javafx in java")
    pyautogui.typewrite('import javafx.*;')

def lang3_java():
    speak("initialize lang3 in java")
    pyautogui.typewrite('import org.apache.commons.lang3.*;')

def jackson_java():
    speak("initialize jackson in java")
    pyautogui.typewrite('import com.fasterxml.jackson.*;')
    
def junit_java():
    speak("initialize junit in java")
    pyautogui.typewrite('import org.junit.*;')
    
def mail_java():
    speak("initialize mail in java")
    pyautogui.typewrite('import javax.mail.*;')

def array_java():
    speak("create array ")
    pyautogui.typewrite('dataType[] arrayName = new dataType[arraySize];')
    
def ArrayList_java():
    speak("create array List ")
    pyautogui.typewrite('ArrayList<dataType> listName = new ArrayList<>();')

def import_LinkedList_java():
    speak("importing linked List ")
    pyautogui.typewrite('import java.util.LinkedList;')
    
def LinkedList_java():
    speak("create Linked List ")
    pyautogui.typewrite('LinkedList<dataType> listName = new LinkedList<>();')
    
def Stack_java():
    speak("create  Stack")
    pyautogui.typewrite('Stack<dataType> stackName = new Stack<>();')
    
def Queue_java():
    speak("create Queue ")
    pyautogui.typewrite('Queue<dataType> queueName = new LinkedList<>();')
    
def HashSet_java():
    speak("create HashSet ")
    pyautogui.typewrite('HashSet<dataType> setName = new HashSet<>();')
    
def HashMap_java():
    speak("create HashMap ")
    pyautogui.typewrite('HashMap<keyType, valueType> mapName = new HashMap<>();')
    
def main_java():
    speak("create  Main class ")
    pyautogui.typewrite('class <ClassName> { \n public static void main(String[] args) {\n System.out.println("Hello, World!");\n   }\n  }')
    
def printfunction_java():
    speak("create Print function ")
    pyautogui.typewrite('System.out.println("HI");')
    
def scanner_java():
    speak("create Scanner function ")
    pyautogui.typewrite('Scanner sc=new Scanner(System.in);')

def graph_part1():
    pyautogui.typewrite(' class Graph {\nint V; // Number of vertices in the graph\nLinkedList<Integer>[] adjList; // Adjacency List for each vertex\nGraph(int V) {\nthis.V = V;\nadjList = new LinkedList[V];\nfor (int i = 0; i < V; i++) {\nadjList[i] = new LinkedList<>();\n  } \n}\n}') 
    
def graph_part2():
    pyautogui.typewrite(' void addEdge(int src, int dest) {\nadjList[src].add(dest);\nadjList[dest].add(src);\n}')
    

def graph_java():
    speak("creating graph")
    graph_part1()
    graph_part2()
    
    
def Binarytree_java():
    speak("create Binary Tree ")
    pyautogui.typewrite(' class Node {\nint data;\n Node left, right;\n Node(int data) {\n this.data = data;\n left = right = null;\n}\n}')

def BinarySearchtree_part1():
    pyautogui.typewrite('  class Node {\nint data;\nNode left, right;\nNode(int data) {\nthis.data = data;\nleft = right = null;\n}} }')
    
    
def BinarySearchtree_part2():
    pyautogui.typewrite('class BinarySearchTree {\nNode root;\nBinarySearchTree() {\nroot = null;\n}}')

def BinarySearchtree_part3():
    pyautogui.typewrite(' void insert(int key) {\nroot = insertNode(root, key);\n}')
    
def BinarySearchtree_part4():
    pyautogui.typewrite('  Node insertNode(Node root, int Key){\n if (root == null) {\n root = new Node(key);\n return root;\n}\n if (key < root.data) {\n root.left = insertNode(root.left, key);\n } else if (key > root.data) {root.right = insertNode(root.right, key);\n}\nreturn root;\n}')
    
    
def BinarySearchtree_java():
    speak("creating Binary Search Tree ")
    BinarySearchtree_part1()
    BinarySearchtree_part2()
    BinarySearchtree_part3()
    BinarySearchtree_part4()


def void_func():
    speak("creating a void function")
    pyautogui.typewrite("void function() {\n//define function here \n    return 0;\n}")
#include <bits/stdc++.h>
def bits_lib():
    speak("including library")
    pyautogui.typewrite("include <bits/stdc++.h>")
    
def math_lib():
    speak("including math library")
    pyautogui.typewrite("#include<math>")
    
def vector_lib():
    speak("including vector library")
    pyautogui.typewrite("#include<vector>")
    
def string_lib():
    speak("including math library")
    pyautogui.typewrite("#include<string>")
    
def queue_lib():
    speak("including math library")
    pyautogui.typewrite("#include<string>")
    
def if_fun():
    speak("writing if")
    pyautogui.typewrite("if(){\n\n}")

def else_fun():
    speak("writing else")
    pyautogui.typewrite("else{\n\n}")
    
def name_space_std():
    speak("writing namespace")
    pyautogui.typewrite("using namespace std;")
    
def return_statment():
    speak("adding return")
    pyautogui.typewrite("return 0;")
    
def int_func():
    speak("creating an integer function")
    pyautogui.typewrite("int function() {\n    //define function here\n    return 0;\n} ")
    
def float_func():
    speak("creating an integer function")
    pyautogui.typewrite("float function() {\n    //define function here\n    return 0;\n} ")
    
def char_func():
    speak("creating a char function")
    pyautogui.typewrite("char function() {\n    //define function here\n    return 0;\n} ")
    
def bool_func():
    speak("creating a boolean function")
    pyautogui.typewrite("boolean function() {\n    //define function here\n    return 0;\n} ")
    
def string_func():
    speak("creating an integer function")
    pyautogui.typewrite("String function() {\n    //define function here\n    return 0;\n} ")





def Int_java():
    speak("Integer in java")
    pyautogui.typewrite('int myInt =   ;')
    
    
def Double_java():
    speak("initialize Double in java")
    pyautogui.typewrite('double myDouble = ;')
    
def Boolean_java():
    speak("initialize Boolean in java")
    pyautogui.typewrite('boolean myBool = ;')
    
        
def Char_java():
    speak("initialize Char in java")
    pyautogui.typewrite('char myChar = ' ';')
    
def String_java():
    speak("initialize String in java")
    pyautogui.typewrite('String myString = "  ";')
    
def Object_java():
    speak("initialize Object in java")
    pyautogui.typewrite('MyClass myObj = new MyClass();')
    
def Void_java():
    speak("initialize Void in java")
    pyautogui.typewrite(' void myVoidMethod() {\n// Code for the method goes here\n}')

def Matrix_java():
    speak("initialize Matrix in java")
    pyautogui.typewrite('// Declare and initialize a 2D array with 3 rows and 4 columns\nint[][] matrix = { {1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12} };')
    
def Trie_part1():
    pyautogui.typewrite('class TrieNode {\n// The number of children nodes\nprivate final int ALPHABET_SIZE = 26;\nprivate TrieNode[] children = new TrieNode[ALPHABET_SIZE];\nprivate boolean isEndOfWord;\n}\n}')
    
    
def Trie_part2():
    pyautogui.typewrite('// Constructor\npublic TrieNode() {\nisEndOfWord = false;\nfor (int i = 0; i < ALPHABET_SIZE; i++) {\nchildren[i] = null;\n }\n}')

def Trie_part3():
    pyautogui.typewrite(' // Getters and setters\npublic boolean isEndOfWord() {\nreturn isEndOfWord;\n}\npublic void setEndOfWord(boolean endOfWord) {\nisEndOfWord = endOfWord;\n }\npublic TrieNode[] getChildren() {\nreturn children;\n }\n}\n')
    
def Trie_part4():
    pyautogui.typewrite('class Trie {\n private TrieNode root;\n    // Constructor\npublic Trie() {\nroot = new TrieNode();\n }\n}')
    
def Trie_part5():
    pyautogui.typewrite('class Trie {/ Inserts a word into the Trie\npublic void insert(String word) {\nTrieNode current = root;\nfor (int i= 0; i < word.length(); i++) {\nchar c = word.charAt(i); \nint index = c - "a"; \nif (current.getChildren()[index] == null) {\ncurrent.getChildren()[index] = new TrieNode();\n} \n current = current.getChildren()[index];\n  }\ncurrent.setEndOfWord(true);\n}')
    
def Trie_part6():
    pyautogui.typewrite('//Searches for a word in the Trie\npublic boolean search(String word) {\nTrieNode current = root;\n for (int i = 0; i < word.length(); i++) {\nchar c = word.charAt(i);\n int index = c - "a";\nif (current.getChildren()[index] == null) {\nreturn false;\n }\ncurrent = current.getChildren()[index];\n }\nreturn current != null && current.isEndOfWord(); \n }')
    
def Trie_part7():
    pyautogui.typewrite('// Checks whether a prefix exists in the Trie\npublic boolean startsWith(String prefix) {\nTrieNode current = root;\n for (int i = 0; i < prefix.length(); i++) {\nchar c = prefix.charAt(i);\nint index = c - "a";\nif (current.getChildren()[index] == null) {\nreturn false;\n}\n current = current.getChildren()[index];\n }\nreturn true;\n}') 
    
def Trie_java():
    speak("initialize Trie in java")
    Trie_part1()
    Trie_part2()
    Trie_part3()
    Trie_part4()
    Trie_part5()
    Trie_part6()
    Trie_part7()

def minHeap_java():
    speak("initialize  minHeap in java")
    pyautogui.typewrite('PriorityQueue<Integer> minHeap = new PriorityQueue<Integer>();')
    
def maxHeap_java():
    speak("initialize  maxHeap in java")
    pyautogui.typewrite('PriorityQueue<Integer> maxHeap = new PriorityQueue<Integer>(Collections.reverseOrder());')
    
    
    
    