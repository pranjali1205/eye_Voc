#Gets speech recognition engine, Speak() function,
from Engine import *
from Engine import recognizer
import re
# Import Java language syntaxes
from code_mode.Java.syntaxJava import *

# Importing Dictating mode
from typing_modes.dictate import *
from typing_modes.typetext import *

# Importing some Functionalities - Mouse, Keyboard, Apps, Special Symbols
from Fuctionalities.SpecialSymbols import *
from Fuctionalities.openApps import *
from Fuctionalities.mouse import *
from Fuctionalities.keyShorts import *


def java_mode():
    
    # Types java code syntaxes based on spoken words, until the command "exit code mode" is given.
  
    speak("java Code mode entered")
    text = ""
    while True:
        data = stream.read(4096)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            command = result["text"]
            print("You said: " + command)
            
            # Exit Java mode
            if re.search("edit", command.lower()) or re.search("exit", command.lower()) or re.search("exit java", command.lower()) or re.search("exit code mode", command.lower()) or re.search("exit code more", command.lower()) or re.search("edit god mode", command.lower()) or re.search("god mode", command.lower()) or re.search("exit mode", command.lower()) or re.search("edit mode", command.lower()) or re.search("exhibit code mode", command.lower()) or re.search("exit gold mode", command.lower()):
                speak("exiting Java code mode")
                break
            
               
            elif re.search("initiate comments", command.lower()):
                comnts_jav()
                
            # Java libraries
            elif re.search("import utility", command.lower()):
                util_java()
            elif re.search("import java effects", command.lower()):
                javafx_java()
            elif re.search("import sql", command.lower()):
                sql_java()
            elif re.search("import jackson", command.lower()):
                jackson_java()
            elif re.search("import j unit", command.lower()):
                junit_java()
            elif re.search("import mail", command.lower()):
                mail_java()
            elif re.search("import lang 3", command.lower()):
                lang3_java()
            
            
            # Java main,class,print,scan
            elif re.search("void function", command.lower()):
                Void_java()
            elif re.search("main class", command.lower()):
                main_java()
            elif re.search("print function", command.lower()):
                printfunction_java()
            elif re.search("scanner function", command.lower()):
                scanner_java()
                
            #Some Data Types
            elif re.search("integer variable", command.lower()):
                Int_java()
            elif re.search("double variable", command.lower()):
                Double_java()
            elif re.search("character variable", command.lower()):
                Int_java()
            elif re.search("boolean variable", command.lower()):
                Boolean_java()
            elif re.search("string variable", command.lower()):
                String_java()
            elif re.search("create object", command.lower()) or re.search("object", command.lower()):
                Object_java()
            
            # Some Useful Functions
            elif re.search("create array", command.lower()) or re.search("array", command.lower()) or re.search("a ray", command.lower()):
                array_java()
            elif re.search("create matrix", command.lower()):
                Matrix_java()
            elif re.search("create array List", command.lower()):
                ArrayList_java()
            elif re.search("create linked list", command.lower()) or re.search("create link list", command.lower()) or re.search("link list", command.lower()):
                LinkedList_java()
            elif re.search("import linked list", command.lower()) or re.search("import link list", command.lower()):
                import_LinkedList_java()
            elif re.search("create stack", command.lower()) or re.search("stack", command.lower()):
                Stack_java()
            elif re.search("create queue", command.lower()) or re.search("queue", command.lower()):
                Queue_java()
            # Heapifiers
            elif re.search("create minimum heap", command.lower()) or re.search("minimum heap", command.lower()):
                minHeap_java()
            elif re.search("create maximum heap", command.lower()) or re.search("maximum heap", command.lower()):
                maxHeap_java()
            # Hash
            elif re.search("create hashset", command.lower()) or re.search("hashset", command.lower()):
                HashSet_java()
            elif re.search("create hashmap", command.lower()) or re.search("hashmap", command.lower()):
                HashMap_java()
            # Graph
            elif re.search("create graph", command.lower()) or re.search("graph", command.lower()):
                 graph_java()
                 
            # Binary Trees
            elif re.search("create binary tree", command.lower()) or re.search("binary tree", command.lower()):
                 Binarytree_java()
            elif re.search("create binary search tree", command.lower()) or re.search("binary search tree", command.lower()):
                 BinarySearchtree_java()
            elif re.search("create tyre", command.lower()) or re.search("tyre", command.lower()) or re.search("tire", command.lower()) or re.search("create tired", command.lower()):
                Trie_java()
            ##modes
            elif re.search("public", command.lower()):
                public_java()
            elif re.search("private", command.lower()):
                private_java()
            elif re.search("protect", command.lower()):
                protected_java()
            elif re.search("protected", command.lower()):
                protected_java()
            

            ## including libraries
            elif re.search("include bits library", command.lower()):
                bits_lib()
            elif re.search("include math library", command.lower()):
                math_lib()
            elif re.search("include max library", command.lower()):
                math_lib()
            elif re.search("include vector library", command.lower()):
                vector_lib()
            elif re.search("include nector library", command.lower()):
                vector_lib()
            elif re.search("include queue library", command.lower()):
                queue_lib()
            elif re.search("include q library", command.lower()):
                queue_lib()
            elif re.search("include you library", command.lower()):
                queue_lib()
            elif re.search("include u library", command.lower()):
                queue_lib()
            elif re.search("include string library", command.lower()):
                string_lib()
            ##loops
            elif re.search("for loop", command.lower()):
                for_loop()
            elif re.search("for look", command.lower()):
                for_loop()
            elif re.search("for luke", command.lower()):
                for_loop()
            elif re.search("do while loop", command.lower()):
                do_while_loop()
            elif re.search("do while luke", command.lower()):
                do_while_loop()
            elif re.search("do while look", command.lower()):
                do_while_loop()
            elif re.search("while loop", command.lower()):
                while_loop()
            elif re.search("while look", command.lower()):
                while_loop()
            elif re.search("while luke", command.lower()):
                while_loop()
            

          ##generally used syntax      
            elif re.search("using name space", command.lower()):
                name_space_std()
            elif re.search("name space", command.lower()):
                name_space_std()
            elif re.search("return", command.lower()):
                return_statment()
            elif re.search("if", command.lower()):
                if_fun()
            elif re.search("write if", command.lower()):
                if_fun()
            elif re.search("else", command.lower()):
                if_fun()
            elif re.search("write else", command.lower()):
                if_fun()
            elif re.search("see out", command.lower()):
                pyautogui.typewrite("cout<<")
            elif re.search("c out", command.lower()):
                pyautogui.typewrite("cout<<")
            elif re.search("see in", command.lower()):
                pyautogui.typewrite("cout<<")
            elif re.search("c in", command.lower()):
                pyautogui.typewrite("cout<<")
            elif re.search("and condition", command.lower()):
                pyautogui.typewrite("&&")
            elif re.search("or condition", command.lower()):
                pyautogui.typewrite("&")
            elif re.search("logical condition", command.lower()):
                pyautogui.typewrite("&&")
            elif re.search("logical condition", command.lower()):
                pyautogui.typewrite("|")
            elif re.search("not equal to", command.lower()):
                pyautogui.typewrite("!=")
            elif re.search("not of", command.lower()):
                pyautogui.typewrite("!()")
            elif re.search("end of", command.lower()):
                pyautogui.typewrite("endl;")
            elif re.search("end l", command.lower()):
                pyautogui.typewrite("endl;")  
                
                
    # Dictation mode
            elif re.search("dictation mode", command.lower()) or re.search("dictation node", command.lower()):
                dictate_mode()
        

            # Tping text mode
            elif re.search("start typing", command.lower()):
                type_text()

            #   Cursor movements
            elif re.search("move left by word", command.lower()):
                mov_lftWord()
            elif re.search("move right by word", command.lower()):
                mov_rgtWord()
            elif re.search("move up", command.lower()):
                mov_up()
            elif re.search("move down", command.lower()):
                mov_down()
            elif re.search("move left", command.lower()):
                mov_lft()
            elif re.search("move right", command.lower()):
                mov_rgt()

            # Opening and closing Apps
            elif re.search("close google", command.lower()):
                close_google()
            elif re.search("open google", command.lower()) or re.search("google", command.lower()):
                open_google()

            elif re.search("close notepad", command.lower()) or re.search("close note bad", command.lower()):
                close_notepad()
            elif re.search("open notepad", command.lower()) or re.search("open not bad", command.lower()) or re.search("not bad", command.lower()):
                open_notepad()
            elif re.search("open mouse", command.lower()) or re.search("open mouth", command.lower()):
                open_eviacam()
            elif re.search("close mouse", command.lower()) or re.search("close mouth", command.lower()):
                close_eviacam()
            elif re.search("close what's up", command.lower()):
                close_watsap()
            elif re.search("open what's up", command.lower()) or re.search("what's up", command.lower()):
                open_watsap()
            elif re.search("close keyboard", command.lower()):
                close_osk()
            elif re.search("open keyboard", command.lower()) or re.search("keyboard", command.lower()):
                open_osk()
            
        
            

            # Mouse Functions
            elif re.search("right click", command.lower()) or re.search("right lick", command.lower()):
                right_click()
            elif re.search("double click", command.lower()) or re.search("double lick", command.lower()):
                double_click()
            elif re.search("left click", command.lower()) or re.search("left lick", command.lower()) or re.search(
                    "left leg", command.lower()):
                left_click()

            elif re.search("release drag", command.lower()):
                release_leftButt()
            elif re.search("drag", command.lower()):
                drag()
            elif re.search("stop drag", command.lower()):
                release_leftButt()
            elif re.search("hold left button", command.lower()):
                hold_leftButt()
            elif re.search("release left button", command.lower()):
                release_leftButt()

            #  Volume
            elif re.search("decrease volume", command.lower()):
                dec_vol()
            elif re.search("increase volume", command.lower()):
                inc_vol()
            elif re.search("mute volume", command.lower()):
                mute()
            elif re.search("mute", command.lower()):
                mute()
            elif re.search("previous track", command.lower()):
                prev_trck()
            elif re.search("next track", command.lower()):
                nxt_trck()
            elif re.search("pause track", command.lower()):
                pause()

            # Clear Functions
            elif re.search("backspace", command.lower()) or re.search("backstage", command.lower()):
                clr_pword()
            elif re.search("clear previous word", command.lower()):
                clr_pword()
            elif re.search("delete previous word", command.lower()):
                clr_pword()
            elif re.search("clear next word", command.lower()):
                clr_nxtword()
            elif re.search("clear entire line", command.lower()):
                clr_line()

            # Keyboard Fuctionalities
            # Window related activities

            elif re.search("open new window", command.lower()) or re.search("new window", command.lower()):
                url = command.lower().replace("open window", "").strip()
                open_window(url)

            elif re.search("minimise window", command.lower()) or re.search("minimize window", command.lower()):
                minimize_window()

            elif re.search("maximize window", command.lower()) or re.search("maximise window", command.lower()):
                maximize_window()

            elif re.search("resize window", command.lower()):
                demaximize_window()

            elif re.search("change window", command.lower()):
                change_window()

            elif re.search("close window", command.lower()):
                close_window()

            elif re.search("open new tab" or "new tab", command.lower()):
                open_tab()

            elif re.search("open new tab in browser", command.lower()):
                new_browsTab()

            elif re.search("close tab", command.lower()):
                close_tab()
            elif re.search("change tab", command.lower()):
                change_tab()

            # Some keyboards shortcuts
            elif re.search("scroll up", command.lower()):
                scroll_up()
            elif re.search("scroll down", command.lower()):
                scroll_down()
            elif re.search("page up", command.lower()):
                page_up()
            elif re.search("page down", command.lower()):
                page_down()
            elif re.search("press tab", command.lower()) or re.search("tab", command.lower()) or re.search("damn", command.lower()) or re.search("damm", command.lower()) or re.search("dam", command.lower()):
                tab()
            elif re.search("enter", command.lower()):
                enter()
            elif re.search("print screen", command.lower()) or re.search("take screenshot", command.lower()):
                print_screen()
            elif re.search("scroll up", command.lower()):
                page_up()
            elif re.search("scroll down", command.lower()):
                page_down()

            # File related functionalities
            elif re.search("open file", command.lower()):
                open_file()
            elif re.search("save file", command.lower()):
                save_file()
            elif re.search("rename", command.lower()):
                rename()
            elif re.search("change all occurances", command.lower()) or re.search("change all occurance", command.lower()):
                chng_allOcuur()
            elif re.search("tab", command.lower()):
                tab()
            elif re.search("new tab", command.lower()) or re.search("new thing", command.lower()) or re.search("new damn", command.lower()) or re.search("new damm", command.lower()) or re.search("new dam", command.lower()):
                open_tab()
            elif re.search("undo", command.lower()) or re.search("and do", command.lower()):
                undo()
            elif re.search("redo", command.lower()):
                redo()
            elif re.search("hold alter", command.lower()) or re.search("navigate", command.lower()):
                hold_alt()
            elif re.search("release alter", command.lower()):
                release_alt()
            elif re.search("initiate comments", command.lower()):
                comnts()

            # Special symbols
            elif re.search("exclaimation", command.lower()):
                exclaim()
            elif re.search("single quote", command.lower()):
                single_quotes()
            elif re.search("double quotes", command.lower()):
                double_quotes()
            elif re.search("double quote", command.lower()):
                double_quotes()
            elif re.search("hash", command.lower()) or re.search("ash", command.lower()):
                hash()
            elif re.search("at the rate symbol", command.lower()):
                at_rate()
            elif re.search("dollar", command.lower()):
                dollar()
            elif re.search("ampersand", command.lower()):
                Amper()
            elif re.search("and symobol", command.lower()):
                Amper()
            elif re.search("percent", command.lower()):
                percent()
            elif re.search("open bracket", command.lower()):
                open_brac()
            elif re.search("close bracket", command.lower()):
                close_brac()
            elif re.search("open flower bracket", command.lower()):
                open_flowerbrac()
            elif re.search("close flower bracket", command.lower()):
                close_flowerbrac()
            elif re.search("open rectangle bracket", command.lower()):
                open_Rectbrac()
            elif re.search("close rectangle bracket", command.lower()):
                close_Rectbrac()
            elif re.search("asterisk", command.lower()):
                asterisk()
            elif re.search("back tick", command.lower()):
                back_tick()
            elif re.search("similar to", command.lower()):
                similar_to()
            elif re.search("equal to", command.lower()):
                equal_to()
            elif re.search("not equal to", command.lower()):
                nt_eq()
            elif re.search("greater than equal to", command.lower()):
                gt_eq()
            elif re.search("less than equal to", command.lower()):
                lt_eq()
            elif re.search("check equality", command.lower()) or re.search("double equal to", command.lower()):
                check_eql()
            elif re.search("modulus", command.lower()):
                modulus()
            elif re.search("exponent", command.lower()):
                exponent()
            elif re.search("floor division", command.lower()):
                floor_div()
            elif re.search("minus", command.lower()):
                minus()
            elif re.search("plus", command.lower()):
                plus()
            elif re.search("divide", command.lower()):
                divide()
            elif re.search("multiply", command.lower()):
                multiply()
            elif re.search("coma", command.lower()):
                coma()
            elif re.search("greater than", command.lower()):
                gt()
            elif re.search("less than", command.lower()):
                lt()
            elif re.search("dot", command.lower()):
                full_stop()
            elif re.search("forward slash", command.lower()):
                f_slash()
            elif re.search("backward slash", command.lower()):
                b_slash()
            elif re.search("colon", command.lower()):
                colon()
            elif re.search("semi colon", command.lower()):
                semi_colon()
            elif re.search("under score", command.lower()):
                under_score()

            #  Selection
            elif re.search("select entire area", command.lower()) or re.search("select all", command.lower()):
                entire_area()
            elif re.search("select area", command.lower()):
                select_area()
            elif re.search("select line", command.lower()):
                select_line()
            elif re.search("convert to comments", command.lower()):
                convert_comnts()
            elif re.search("move window up", command.lower()):
                win_up()
            elif re.search("move window down", command.lower()):
                win_dwn()
            elif re.search("move window right", command.lower()):
                win_rgt()
            elif re.search("move window left", command.lower()):
                win_left()
            elif re.search("action center", command.lower()):
                spl_setings()
            elif re.search("stop execution", command.lower()):
                stp_exectn()
            elif re.search("copy command", command.lower()) or re.search("control c", command.lower()):
                copy()

            elif re.search("cut command", command.lower()) or re.search("control x", command.lower()):
                cut()

            elif re.search("paste command", command.lower()) or re.search("control v", command.lower()):
                paste()
                
            # Types the words other than above keywords
            else:
                text += command
                # pyautogui.typewrite(command + " ")
        