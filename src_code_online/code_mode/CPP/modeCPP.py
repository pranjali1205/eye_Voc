#Gets speech recognition engine, Speak() function,
from Engine import *
from Engine import recognizer
import re
# Import CPP language syntaxes
from code_mode.CPP.syntaxCPP import *

# Importing Dictating mode
from typing_modes.dictate import *
from typing_modes.typetext import *

# Importing some Functionalities - Mouse, Keyboard, Apps, Special Symbols
from Fuctionalities.SpecialSymbols import *
from Fuctionalities.openApps import *
from Fuctionalities.mouse import *
from Fuctionalities.keyShorts import *    

   
def cpp_mode():
    """
    Type c++ code syntaxes based on spoken words, until the command "exit code mode" is given.
    """ 
    speak("c++ Code mode entered")
    text = ""
    while True:
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said: " + command)
            
            # Exit CPP mode
            if re.search("edit", command.lower()) or re.search("exit", command.lower()) or re.search("exit cpp", command.lower()) or re.search("exit code mode", command.lower()) or re.search("exit code more", command.lower()) or re.search("edit god mode", command.lower()) or re.search("god mode", command.lower()) or re.search("exit mode", command.lower()) or re.search("edit mode", command.lower()) or re.search("exhibit code mode", command.lower()):
                speak("exiting C code mode")
                break
            
            # CPP functions
            elif re.search("main function", command.lower()) or re.search("men function", command.lower()) or re.search("men functions", command.lower()):
                main_func()
            elif re.search("void function", command.lower()):
                void_func()
            elif re.search("initiate comments", command.lower()) or re.search("start comments", command.lower()):
                comnts()
            elif re.search("integer function", command.lower()):
                int_func()
            elif re.search("character function", command.lower()):
                char_func()
            
            elif re.search("boolean function", command.lower()):
                bool_func()
            elif re.search("float function", command.lower()):
                float_func()
            elif re.search("string function", command.lower()):
                string_func()
        ##printing basic template   
            elif re.search("import basic template", command.lower()):
                input_structure()
            elif re.search("empty template", command.lower()):
                structure_cpp()   
        ##arrays ,variables
            elif re.search("array", command.lower()) or re.search("a ray", command.lower()):
                array_cpp()  
            elif re.search("indeed function", command.lower()) or re.search("integer function", command.lower()):
                int_func()         
            elif re.search("integer variable", command.lower()) or re.search("indeed", command.lower()) or re.search("variable integer", command.lower()) or re.search("interior variable", command.lower()):
                int_var()

            elif re.search("float variable", command.lower()) or re.search("boat variable", command.lower()):
                float_var()
            elif re.search("boolean variable", command.lower()):
                bool_var()
            elif re.search("float array", command.lower()):
              array_1cpp()
            elif re.search("character array", command.lower()):
                array_2cpp()
            elif re.search("string array", command.lower()):
                array_3cpp()
            elif re.search("data pointer array", command.lower()):
                array_4cpp()
            elif re.search("create link list", command.lower()) or re.search("create linked list", command.lower()):
                array_5cpp()           
         
            elif re.search("using name", command.lower()) or re.search("using namespace", command.lower()) or re.search("namespace", command.lower()):
                array_52cpp()    
            elif re.search("main function", command.lower()):
                array_6cpp()
            elif re.search("next line", command.lower()):
                next_line()
                    
                
                

          ## including libraries
            elif re.search("include your stream", command.lower()) or re.search("include or stream", command.lower()) or re.search("include on stream", command.lower()) or re.search("include your steam", command.lower()) or re.search("include or steam", command.lower()) or re.search("include on steam", command.lower()):
                array_51cpp()
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
            elif re.search("for loop", command.lower()) or re.search("for look", command.lower()) or re.search("for luke", command.lower()):
                for_loop()
            elif re.search("do while loop", command.lower()) or re.search("do while luke", command.lower()) or re.search("do while look", command.lower()):
                do_while_loop()
            elif re.search("while loop", command.lower()) or re.search("while look", command.lower()) or re.search("while luke", command.lower()):
                while_loop()
            

          ##generally used syntax      
            elif re.search("using name space", command.lower()) or re.search("name space", command.lower()):
                name_space_std()
    
            elif re.search("return", command.lower()):
                return_statment()
            elif re.search("if", command.lower()) or re.search("write if", command.lower()):
                if_fun()
            elif re.search("else", command.lower()) or re.search("write else", command.lower()):
                if_fun()
            elif re.search("see out", command.lower()) or re.search("c out", command.lower()) or re.search("cout", command.lower()):
                cout()
        
            elif re.search("see in", command.lower()) or re.search("c in", command.lower()) or re.search("cin", command.lower()):
                cin()
            
                ## condition operaters
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
            elif re.search("move up", command.lower()) or re.search("go up", command.lower()):
                mov_up()
            elif re.search("move down", command.lower()) or re.search("go down", command.lower()):
                mov_down()
            elif re.search("move left", command.lower()) or re.search("go left", command.lower()):
                mov_lft()
            elif re.search("move right", command.lower()) or re.search("go right", command.lower()):
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
            elif re.search("change all occurances", command.lower()) or re.search("change all occurance",
                                                                                  command.lower()):
                chng_allOcuur()
            elif re.search("tab", command.lower()):
                tab()
            elif re.search("new tab", command.lower()) or re.search("new thing", command.lower()) or re.search(
                    "new damn", command.lower()) or re.search("new damm", command.lower()) or re.search("new dam",
                                                                                                        command.lower()):
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
            else:
               text += command
            #    pyautogui.typewrite(command + " ")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
       
