'''
Builder: KoGandhi05 (hyungin0505)
Project: Utility - League of Legends Score Calculator
Support; Utility Head @KTH

START 2022-07-28 21:14:23
~
END 2022-07-29 01:58:17
'''

from tkinter import * # Use TKInter Module

win = Tk() # Entire Area with TK
win.title("LOL Team Score") # Program Name
win.geometry('630x550+200+200') # Setting Program Area
win.resizable(False, False) # (Widht, Height) Resize Unable

# Checked Button of each position
choice1  = IntVar() # Top
choice2  = IntVar() # JUG
choice3  = IntVar() # MID
choice4  = IntVar() # ADC
choice5  = IntVar() # SUP


# Frame
#################################################################################################
top_frame = Frame(win) # make 'Frame' for 'top_frame' in 'win' (Team Name, Grade, Result)
top_frame.grid(row = 0, column = 0, padx = (5, 0)) # Set 'Frame' Location

main_frame = Frame(win) # make 'Frame' for 'main_frame' in 'win' (Position)
main_frame.grid(row = 1, column = 0, pady = (10, 0)) # Set 'Frame' Location

last_frame = Frame(win)
last_frame.grid(row = 2, column = 0, pady = (10, 0))
#################################################################################################


# Team Name
######################################################################################
Team_name = Label(top_frame, # Set Label (Show Only)
    text = '팀명', # Show Text
    font = 'Dotum 16 bold', # Set Font
    bg = 'lightgray', # Set Background Color
    ## width = # Set Width
    height = 1, # Set Height
    padx = 5,
    highlightbackground = "gray", # Border Color -> gray
    highlightthickness = 1 # Border Weight -> 1
    )
Team_name.grid(row = 0, column = 0, padx = (2,2), pady = (5, 5)) # Show 'Team_name'

# Input Box (Non Effect)
T_W = Entry(top_frame,
    font = 'Dotum 16 bold', # Font -> Dotum for 16size to Bold style
    width = 35,
    highlightbackground = "gray",
    highlightthickness = 1
        
    )
T_W.grid(row = 0, column = 1, padx = (3, 15))
######################################################################################


# Student Grade
########################################################################
Grade = Label (top_frame,
    text = '학년', 
    font = 'Dotum  16 bold',
    bg = 'lightgray',
    padx = 5,
    highlightbackground = "gray",
    highlightthickness = 1
)
Grade.grid(row=0, column = 2)

# Input Box (Non Effect)
Y_W = Entry(top_frame,
    font = 'Dotum 16 bold',
    width = 3,
    highlightthickness = 1,
    highlightbackground = "gray",
    )
Y_W.grid(row = 0, column = 3, padx = (3, 3))
########################################################################


# Result
######################################################################################
Result = Label(top_frame,
    text = "결과",
    font = "Dotum 16 bold",
    bg = "lightgray",
    padx = 5,
    highlightbackground = "gray",
    highlightthickness = 1
    )
Result.grid(row = 1, column = 0)

R_W = Text(top_frame,
    font = "Dotum 16 bold",
    width = 45,
    height = 1,
    highlightbackground = "gray",
    highlightthickness = 1
    )
R_W.grid(row = 1, column = 1, columnspan = 3, padx = (0,0), pady = (5, 5))
######################################################################################





########################################################################
                      ### Position Score ###
########################################################################

#########
## TOP ##
#########
top = Label(main_frame, text = "탑(TOP)", font = "Dotum 14 bold", bg = "lightgray", width = 9, height =1, padx = 5,)
top.grid(row = 0, column = 0, padx = (10,5))

s_top = Text(main_frame, font = "Dotum 14 bold", width = 9, height = 1, padx = 5)
s_top.grid(row = 1, column = 0)

T_C = Radiobutton(main_frame, text = "GM/CH", variable = choice1, value = 1)
T_C.grid(row = 2, column = 0)
T_M = Radiobutton(main_frame, text = "D1,2/M", variable = choice1, value = 2)
T_M.grid(row = 3, column = 0)
T_D = Radiobutton(main_frame, text = "D3,4", variable = choice1, value = 3)
T_D.grid(row = 4, column = 0)
T_P = Radiobutton(main_frame, text = "P1,2", variable = choice1, value = 4)
T_P.grid(row = 5, column = 0)
T_PP = Radiobutton(main_frame, text = "P3,4", variable = choice1, value = 5)
T_PP.grid(row = 6, column = 0)
T_G = Radiobutton(main_frame, text = "G1,2", variable = choice1, value = 6)
T_G.grid(row = 7, column = 0)
T_GG = Radiobutton(main_frame, text = "G3,4", variable = choice1, value = 7)
T_GG.grid(row = 8, column = 0)
T_S = Radiobutton(main_frame, text = "S1,2", variable = choice1, value = 8)
T_S.grid(row = 9, column = 0)
T_SS = Radiobutton(main_frame, text = "S3,4", variable = choice1, value = 9)
T_SS.grid(row = 10, column = 0)
T_B = Radiobutton(main_frame, text = "B1,2", variable = choice1, value = 10)
T_B.grid(row = 11, column = 0)
T_BB = Radiobutton(main_frame, text = "B3,4", variable = choice1, value = 11)
T_BB.grid(row = 12, column = 0)
T_I = Radiobutton(main_frame, text = "I1,2", variable = choice1, value = 12)
T_I.grid(row = 13, column = 0)
T_II = Radiobutton(main_frame, text = "I3,4", variable = choice1, value = 13)
T_II.grid(row = 14, column = 0)
T_UN = Radiobutton(main_frame, text = "UNRANKED", variable = choice1, value = 14)
T_UN.grid(row = 15, column = 0)


#########
## JUG ##
#########
jug = Label(main_frame, text = "정글(JUG)", font = "Dotum 14 bold", bg = "lightgray", width = 9, height =1, padx = 5,)
jug.grid(row = 0, column = 1, padx = 5)

s_jug = Text(main_frame, font = "Dotum 14 bold", width = 9, height = 1, padx = 5)
s_jug.grid(row = 1, column = 1)

J_C = Radiobutton(main_frame, text = "GM/CH", variable = choice2, value = 1)
J_C.grid(row = 2, column = 1)
J_M = Radiobutton(main_frame, text = "D1,2/M", variable = choice2, value = 2)
J_M.grid(row = 3, column = 1)
J_D = Radiobutton(main_frame, text = "D3,4", variable = choice2, value = 3)
J_D.grid(row = 4, column = 1)
J_P = Radiobutton(main_frame, text = "P1,2", variable = choice2, value = 4)
J_P.grid(row = 5, column = 1)
J_PP = Radiobutton(main_frame, text = "P3,4", variable = choice2, value = 5)
J_PP.grid(row = 6, column = 1)
J_G = Radiobutton(main_frame, text = "G1,2", variable = choice2, value = 6)
J_G.grid(row = 7, column = 1)
J_GG = Radiobutton(main_frame, text = "G3,4", variable = choice2, value = 7)
J_GG.grid(row = 8, column = 1)
J_S = Radiobutton(main_frame, text = "S1,2", variable = choice2, value = 8)
J_S.grid(row = 9, column = 1)
J_SS = Radiobutton(main_frame, text = "S3,4", variable = choice2, value = 9)
J_SS.grid(row = 10, column = 1)
J_B = Radiobutton(main_frame, text = "B1,2", variable = choice2, value = 10)
J_B.grid(row = 11, column = 1)
J_BB = Radiobutton(main_frame, text = "B3,4", variable = choice2, value = 11)
J_BB.grid(row = 12, column = 1)
J_I = Radiobutton(main_frame, text = "I1,2", variable = choice2, value = 12)
J_I.grid(row = 13, column = 1)
J_II = Radiobutton(main_frame, text = "I3,4", variable = choice2, value = 13)
J_II.grid(row = 14, column = 1)
J_UN = Radiobutton(main_frame, text = "UNRANKED", variable = choice2, value = 14)
J_UN.grid(row = 15, column = 1)


#########
## MID ##
#########
mid = Label(main_frame, text = "미드(MID)", font = "Dotum 14 bold", bg = "lightgray", width = 9, height =1, padx = 5,)
mid.grid(row = 0, column = 2, padx = 5)

s_mid = Text(main_frame, font = "Dotum 14 bold", width = 9, height = 1, padx = 5)
s_mid.grid(row = 1, column = 2)

M_C = Radiobutton(main_frame, text = "GM/CH", variable = choice3, value = 1)
M_C.grid(row = 2, column = 2)
M_M = Radiobutton(main_frame, text = "D1,2/M", variable = choice3, value = 2)
M_M.grid(row = 3, column = 2)
M_D = Radiobutton(main_frame, text = "D3,4", variable = choice3, value = 3)
M_D.grid(row = 4, column = 2)
M_P = Radiobutton(main_frame, text = "P1,2", variable = choice3, value = 4)
M_P.grid(row = 5, column = 2)
M_PP = Radiobutton(main_frame, text = "P3,4", variable = choice3, value = 5)
M_PP.grid(row = 6, column = 2)
M_G = Radiobutton(main_frame, text = "G1,2", variable = choice3, value = 6)
M_G.grid(row = 7, column = 2)
M_GG = Radiobutton(main_frame, text = "G3,4", variable = choice3, value = 7)
M_GG.grid(row = 8, column = 2)
M_S = Radiobutton(main_frame, text = "S1,2", variable = choice3, value = 8)
M_S.grid(row = 9, column = 2)
M_SS = Radiobutton(main_frame, text = "S3,4", variable = choice3, value = 9)
M_SS.grid(row = 10, column = 2)
M_B = Radiobutton(main_frame, text = "B1,2", variable = choice3, value = 10)
M_B.grid(row = 11, column = 2)
M_BB = Radiobutton(main_frame, text = "B3,4", variable = choice3, value = 11)
M_BB.grid(row = 12, column = 2)
M_I = Radiobutton(main_frame, text = "I1,2", variable = choice3, value = 12)
M_I.grid(row = 13, column = 2)
M_II = Radiobutton(main_frame, text = "I3,4", variable = choice3, value = 13)
M_II.grid(row = 14, column = 2)
M_UN = Radiobutton(main_frame, text = "UNRANKED", variable = choice3, value = 14)
M_UN.grid(row = 15, column = 2)


#########
## ADC ##
#########
adc = Label(main_frame, text = "원딜(ADC)", font = "Dotum 14 bold", bg = "lightgray", width = 9, height =1, padx = 5,)
adc.grid(row = 0, column = 3, padx = 5)

s_adc = Text(main_frame, font = "Dotum 14 bold", width = 9, height = 1, padx = 5)
s_adc.grid(row = 1, column = 3)

A_C = Radiobutton(main_frame, text = "GM/CH", variable = choice4, value = 1)
A_C.grid(row = 2, column = 3)
A_M = Radiobutton(main_frame, text = "D1,2/M", variable = choice4, value = 2)
A_M.grid(row = 3, column = 3)
A_D = Radiobutton(main_frame, text = "D3,4", variable = choice4, value = 3)
A_D.grid(row = 4, column = 3)
A_P = Radiobutton(main_frame, text = "P1,2", variable = choice4, value = 4)
A_P.grid(row = 5, column = 3)
A_PP = Radiobutton(main_frame, text = "P3,4", variable = choice4, value = 5)
A_PP.grid(row = 6, column = 3)
A_G = Radiobutton(main_frame, text = "G1,2", variable = choice4, value = 6)
A_G.grid(row = 7, column = 3)
A_GG = Radiobutton(main_frame, text = "G3,4", variable = choice4, value = 7)
A_GG.grid(row = 8, column = 3)
A_S = Radiobutton(main_frame, text = "S1,2", variable = choice4, value = 8)
A_S.grid(row = 9, column = 3)
A_SS = Radiobutton(main_frame, text = "S3,4", variable = choice4, value = 9)
A_SS.grid(row = 10, column = 3)
A_B = Radiobutton(main_frame, text = "B1,2", variable = choice4, value = 10)
A_B.grid(row = 11, column = 3)
A_BB = Radiobutton(main_frame, text = "B3,4", variable = choice4, value = 11)
A_BB.grid(row = 12, column = 3)
A_I = Radiobutton(main_frame, text = "I1,2", variable = choice4, value = 12)
A_I.grid(row = 13, column = 3)
A_II = Radiobutton(main_frame, text = "I3,4", variable = choice4, value = 13)
A_II.grid(row = 14, column = 3)
A_UN = Radiobutton(main_frame, text = "UNRANKED", variable = choice4, value = 14)
A_UN.grid(row = 15, column = 3)


#########
## SUP ##
#########
sup = Label(main_frame, text = "서폿(SUP)", font = "Dotum 14 bold", bg = "lightgray", width = 9, height =1, padx = 5,)
sup.grid(row = 0, column = 4, padx = (5, 10))

s_sup = Text(main_frame, font = "Dotum 14 bold", width = 9, height = 1, padx = 5)
s_sup.grid(row = 1, column = 4)

S_C = Radiobutton(main_frame, text = "GM/CH", variable = choice5, value = 1)
S_C.grid(row = 2, column = 4)
S_M = Radiobutton(main_frame, text = "D1,2/M", variable = choice5, value = 2)
S_M.grid(row = 3, column = 4)
S_D = Radiobutton(main_frame, text = "D3,4", variable = choice5, value = 3)
S_D.grid(row = 4, column = 4)
S_P = Radiobutton(main_frame, text = "P1,2", variable = choice5, value = 4)
S_P.grid(row = 5, column = 4)
S_PP = Radiobutton(main_frame, text = "P3,4", variable = choice5, value = 5)
S_PP.grid(row = 6, column = 4)
S_G = Radiobutton(main_frame, text = "G1,2", variable = choice5, value = 6)
S_G.grid(row = 7, column = 4)
S_GG = Radiobutton(main_frame, text = "G3,4", variable = choice5, value = 7)
S_GG.grid(row = 8, column = 4)
S_S = Radiobutton(main_frame, text = "S1,2", variable = choice5, value = 8)
S_S.grid(row = 9, column = 4)
S_SS = Radiobutton(main_frame, text = "S3,4", variable = choice5, value = 9)
S_SS.grid(row = 10, column = 4)
S_B = Radiobutton(main_frame, text = "B1,2", variable = choice5, value = 10)
S_B.grid(row = 11, column = 4)
S_BB = Radiobutton(main_frame, text = "B3,4", variable = choice5, value = 11)
S_BB.grid(row = 12, column = 4)
S_I = Radiobutton(main_frame, text = "I1,2", variable = choice5, value = 12)
S_I.grid(row = 13, column = 4)
S_II = Radiobutton(main_frame, text = "I3,4", variable = choice5, value = 13)
S_II.grid(row = 14, column = 4)
S_UN = Radiobutton(main_frame, text = "UNRANKED", variable = choice5, value = 14)
S_UN.grid(row = 15, column = 4)

########################################################################
########################################################################


# Calculate Score Function
def score():
    #__init__ score
    s_top.delete("0.0", END)
    s_jug.delete("0.0", END)
    s_mid.delete("0.0", END)
    s_adc.delete("0.0", END)
    s_sup.delete("0.0", END)
    R_W.delete("0.0", END)
    
    
    # Get CheckBox Value
    S_top = choice1.get() 
    S_jug = choice2.get()
    S_mid = choice3.get()
    S_adc = choice4.get()
    S_sup = choice5.get()

    #################
    ### TOP Score ###
    #################
    if S_top == 1:
        s_top.insert(END, 48)
    if S_top == 2:
        s_top.insert(END, 41)
    if S_top == 3:
        s_top.insert(END, 35)
    if S_top == 4:
        s_top.insert(END, 30)
    if S_top == 5:
        s_top.insert(END, 25)
    if S_top == 6:
        s_top.insert(END, 21)
    if S_top == 7:
        s_top.insert(END, 18)
    if S_top == 8:
        s_top.insert(END, 16)
    if S_top == 9:
        s_top.insert(END, 12)
    if S_top == 10:
        s_top.insert(END, 8)
    if S_top == 11:
        s_top.insert(END, 5)
    if S_top == 12:
        s_top.insert(END, 2)
    if S_top == 13:
        s_top.insert(END, 0)
    if S_top == 14:
        s_top.insert(END, 6)


    #################
    ### JUG Score ###
    #################
    if S_jug == 1:
        s_jug.insert(END, 61)
    if S_jug == 2:
        s_jug.insert(END, 49)
    if S_jug == 3:
        s_jug.insert(END, 40)
    if S_jug == 4:
        s_jug.insert(END, 36)
    if S_jug == 5:
        s_jug.insert(END, 33)
    if S_jug == 6:
        s_jug.insert(END, 25)
    if S_jug == 7:
        s_jug.insert(END, 20)
    if S_jug == 8:
        s_jug.insert(END, 15)
    if S_jug == 9:
        s_jug.insert(END, 9)
    if S_jug == 10:
        s_jug.insert(END, 5)
    if S_jug == 11:
        s_jug.insert(END, 1)
    if S_jug == 12:
        s_jug.insert(END, 0)
    if S_jug == 13:
        s_jug.insert(END, -4)
    if S_jug == 14:
        s_jug.insert(END, 2)


    #################
    ### MID Score ###
    #################
    if S_mid == 1:
        s_mid.insert(END, 58)
    if S_mid == 2:
        s_mid.insert(END, 47)
    if S_mid == 3:
        s_mid.insert(END, 39)
    if S_mid == 4:
        s_mid.insert(END, 36)
    if S_mid == 5:
        s_mid.insert(END, 30)
    if S_mid == 6:
        s_mid.insert(END, 23)
    if S_mid == 7:
        s_mid.insert(END, 18)
    if S_mid == 8:
        s_mid.insert(END, 15)
    if S_mid == 9:
        s_mid.insert(END, 12)
    if S_mid == 10:
        s_mid.insert(END, 7)
    if S_mid == 11:
        s_mid.insert(END, 5)
    if S_mid == 12:
        s_mid.insert(END, 1)
    if S_mid == 13:
        s_mid.insert(END, -2)
    if S_mid == 14:
        s_mid.insert(END, 3)


    #################
    ### ADC Score ###
    #################
    if S_adc == 1:
        s_adc.insert(END, 53)
    if S_adc == 2:
        s_adc.insert(END, 42)
    if S_adc == 3:
        s_adc.insert(END, 35)
    if S_adc == 4:
        s_adc.insert(END, 30)
    if S_adc == 5:
        s_adc.insert(END, 25)
    if S_adc == 6:
        s_adc.insert(END, 21)
    if S_adc == 7:
        s_adc.insert(END, 17)
    if S_adc == 8:
        s_adc.insert(END, 15)
    if S_adc == 9:
        s_adc.insert(END, 11)
    if S_adc == 10:
        s_adc.insert(END, 8)
    if S_adc == 11:
        s_adc.insert(END, 4)
    if S_adc == 12:
        s_adc.insert(END, 1)
    if S_adc == 13:
        s_adc.insert(END, -1)
    if S_adc == 14:
        s_adc.insert(END, 4)


    #################
    ### SUP Score ###
    #################
    if S_sup == 1:
        s_sup.insert(END, 49)
    if S_sup == 2:
        s_sup.insert(END, 42)
    if S_sup == 3:
        s_sup.insert(END, 34)
    if S_sup == 4:
        s_sup.insert(END, 30)
    if S_sup == 5:
        s_sup.insert(END, 25)
    if S_sup == 6:
        s_sup.insert(END, 21)
    if S_sup == 7:
        s_sup.insert(END, 18)
    if S_sup == 8:
        s_sup.insert(END, 16)
    if S_sup == 9:
        s_sup.insert(END, 14)
    if S_sup == 10:
        s_sup.insert(END, 11)
    if S_sup == 11:
        s_sup.insert(END, 8)
    if S_sup == 12:
        s_sup.insert(END, 5)
    if S_sup == 13:
        s_sup.insert(END, 4)
    if S_sup == 14:
        s_sup.insert(END, 8)

    # def result():
    R_T = int(s_top.get("1.0", END))
    R_J = int(s_jug.get("1.0", END))
    R_M = int(s_mid.get("1.0", END))
    R_A = int(s_adc.get("1.0", END))
    R_S = int(s_sup.get("1.0", END))

    RES = R_T + R_J + R_M + R_A + R_S
    if RES <= 90:
        message = "점으로 참가 가능합니다."
    else: 
        message = "점으로 참가 불가능합니다."
    R_W.insert(END, str(RES) + message)

submit = Button(last_frame, text = '점수 계산하기', font = "Dotum 16 bold", bg = "gray", fg = "white", command = score)
submit.grid(row = 0, column = 0, padx = (0,10))

win.mainloop() 
# 정보)) 본 516번째 코드 라인은 아이유의 생일 5월 16일을 기념하기 위한 코드입니다.
