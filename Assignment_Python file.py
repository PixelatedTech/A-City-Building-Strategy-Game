def ValidateBuild(Option, Option1, Option2, Option3, Option4):
    '''--------------------------------------------------------------------------------------------------
    Given option to choose the building and it validate the building
    --------------------------------------------------------------------------------------------------'''

    global gCounter
    global gPlanGrid
    global gSamplingList
    global gSamplingCount
    while True:
        try:
            if Option == 1:
                building_choice = input('1st Option:')
            if Option == 2:
                building_choice = input('2nd Option:')
            if Option == 3:
                building_choice = input('3rd Option:')
            if Option == 4:
                building_choice = input('4th Option:')
            if Option == 5:
                building_choice = input('5th Option:')

            building_choice.upper()

        except ValueError:
            print('Value error')
            continue
        if ((building_choice != 'HSE') and (building_choice != 'BCH') and (building_choice != 'SHP') and (building_choice != 'HWY') and (building_choice != 'FAC') and (building_choice != 'MON') and (building_choice != 'PRK')):
            print('Invaild building')
            continue
        if ((building_choice == Option1) or (building_choice == Option2) or (building_choice == Option3) or (building_choice == Option4)):
            print('Building already taken')
            continue
        else:
          return building_choice
'''
def CityLayout():
    f = open("C:/Users/jyosh/Desktop/City layout.txt",'r')
    lines = f.read
    print(lines)
    f.close()
'''
def BuildingScore():
    '''--------------------------------------------------------------------------------------------------
    This function reutn the total scores of the 5 building
    --------------------------------------------------------------------------------------------------'''
    global gCounter
    global gPlanGrid
    global gSamplingList
    global gSamplingCount
    
    total_sum = 0
    for i in range(len(gSamplingList)):
        if gSamplingList[i] == 'BCH':
                    #print('B1','loop for BCH')
            SumOfBch = BCHScoring()
            total_sum = total_sum + SumOfBch
        elif gSamplingList[i] == 'HSE':
                    #print('B2','loop for HSE')
            SumOfHse = HSEScoring()
            total_sum = total_sum + SumOfHse
        elif gSamplingList[i] == 'FAC':
                    #print('B3','loop for FAC')
            SumOfFac = FACScoring()
            total_sum = total_sum + SumOfFac
        elif gSamplingList[i] == 'PRK':
                    #print('B4','loop for PRK')
            SumOfPrk = PRKScoring()
            total_sum = total_sum + SumOfPrk
        elif gSamplingList[i] == 'HWY':
                    #print('B5','loop for HWY')
            SumOfHwy = HWYScoring()
            total_sum = total_sum + SumOfHwy
        elif gSamplingList[i] == 'MON':
                    #print('B6','loop for MON')
            SumOfMon = MONScoring()
            total_sum = total_sum + SumOfMon
        elif gSamplingList[i] == 'SHP':
                    #print('B7','loop for SHP')
            SumOfShp = SHPScoring()
            total_sum = total_sum + SumOfShp
            
    print('\nTotal Score:',total_sum)
    return total_sum

def SaveGame():
    '''--------------------------------------------------------------------------------------------------
    This function save the  lastest game progress into a text file for retrival 
    --------------------------------------------------------------------------------------------------'''
    import pickle
    import os
    global gCounter
    global gPlanGrid
    global gSamplingList
    global gSamplingCount

    os.system('crl')
    f = open("C:\\Users\\jyosh\\Desktop\\IT - programmimg skills\\scoreing\\SimpCityProgess.txt", "wb") 
    global_list = [gCounter,gPlanGrid,gSamplingList,gSamplingCount]
    
    pickle.dump(global_list, f)
   
    f.close()
        

def LoadGame():
    '''--------------------------------------------------------------------------------------------------
    This function retrive the saved text file and insert the global variable in the program
    --------------------------------------------------------------------------------------------------'''
    global gCounter
    global gPlanGrid
    global gSamplingList
    global gSamplingCount

    
    import pickle
    import os
    os.system('crl')
    f = open("C:\\Users\\jyosh\\Desktop\\IT - programmimg skills\\scoreing\\SimpCityProgess.txt", "rb")
    Rec = pickle.load(f)
    #print('B0',Rec)
    gCounter = Rec[0]
    gPlanGrid = Rec[1]
    gSamplingList = Rec[2]
    gSamplingCount = Rec[3]
  
    f.close()
    
    

def StartGame(option1,option2,option3,option4,option5, IsSavedGame):
    '''--------------------------------------------------------------------------------------------------
    print the differnt building available and send the choosen building for validation
    Runs a loop for start game and print the menu and ask for user choice
    choice 1/2 ask the user for the grid locatioj to build and send the input fro validation and from appending
    choice 3 calls the function to print the curent score of the exitting building
    chouce 4 it brings it back to the main menu
    --------------------------------------------------------------------------------------------------'''
    global gCounter
    global gPlanGrid
    global gSamplingList
    global gSamplingCount
    ##### added gcounter as a parameter to pass
    if IsSavedGame == 'N':
        #print('A3',' The global varible are reset')
        gCounter = 0
        gSamplingList =[]
        gSamplingCount = [0,0,0,0,0]
        gPlanGrid = [  ['     ','     ','     ','     '],\
                      ['     ','     ','     ','     '],\
                      ['     ','     ','     ','     '],\
                      ['     ','     ','     ','     '] ]
        
        print('Choose five opttion for the list below (enter 3-word)')
        print('1. BCH(Beach)\n2. FAC(Factory)\n3. HSE(House)\n4. SHP(Shop)\n5. HWY(Highway)\n6. PRK(Park)\n7. MON(Monument)')
        ReturnVal = True

        option1 = ValidateBuild(1,option1,option2,option3,option4)
        option2 = ValidateBuild(2,option1,option2,option3,option4)
        option3 = ValidateBuild(3,option1,option2,option3,option4)
        option4 = ValidateBuild(4,option1,option2,option3,option4)
        option5 = ValidateBuild(5,option1,option2,option3,option4)
                   
        gSamplingList.append(option1)
        gSamplingList.append(option2)
        gSamplingList.append(option3)
        gSamplingList.append(option4)
        gSamplingList.append(option5)
        gCounter = 0
        
    print('Turn:',gCounter+1)

    BuildCity('', '',gCounter)
    
      
    for loop in range(gCounter+1,1000):
        import random

        random_building = random.sample(gSamplingList,2)
        #print(random_building)
        random1 = random_building[0]
        random2 = random_building[1]
        print('\n1. Build a',random1)
        print('2. Build a',random2)
        print('3. See current score\n4. Save game\n0. Exit to Main menu')
        choice = 0

        
        while True:
            try:
                choice = int(input('Your choice (Choose Number 1/2/3/4/0):?'))
            except ValueError:
                print('Not an Interger! Try again')
            if ((choice < 0) or (choice > 4)):
                print('Not an Interger! Try again')
                continue
            else:
                break
#           fi
#       end while 
          
        #choice = int(input('Your choice (Choose Number 1/2/3/0):?'))
        location = ''
        if choice == 0:
            break
        elif choice == 1 or choice == 2:
            
            while True:
                try:
                    location = input(('Build where?'))
                except ValueError:
                    print('Invalid cell')
                if (len(location) != 2):
                    if (location[0] != 'a'and 'b'and 'c'and'd'and'A'and'B'and'C'and'D') or (location[1] != '1'and '2'and'3'and'4'):
                        print('Invalid cell')
                        continue
                    else:
                        print('Invalid cell')
                        continue
#                   fi1
                else:
                    break
#               fi
#            end while

            choosen = random_building[int(choice) -1]
            
            if loop != 1 :
                ReturnVal=CheckValidity(location)
             
        elif choice == 3:
            BuildingScore()

            ReturnVal=False
            
        elif choice == 4:
            SaveGame()
            print('')
            print('')
            print('Game saved !')
            
            ReturnVal = False
            break

                       
        if ReturnVal == True:
            BuildCity(choosen, location, loop)
            gCounter=gCounter+1

            
        count = 0
        for i in range(len(gPlanGrid)):
            for x in range(len(gPlanGrid)):
                if gPlanGrid[i][x] != '     ':
                    count = count + 1
        
        if count == 16:
            print('\n')
#            BuildCity('','',gCounter)
            TOTAL_SUM =BuildingScore()
            print('')
            print('')
            
            HighScoreBoard(TOTAL_SUM)
            print('')
            print('')
            print('This game will retuen to main menu....')
            print('')
            print('')
            ReturnVal = False
            break

        #if ReturnVal == True:
            #BuildCity(choosen, location, loop)
            #gCounter=gCounter+1

            
        
           


    
def HighScoreBoard(total_sum):
    '''--------------------------------------------------------------------------------------------------
    Contains pre-set values and checks if the total score of the building at the end of the game is greater than the pre-set list. it appends the value accordingly
    print a highscore board when it is called at the main menu
    --------------------------------------------------------------------------------------------------'''
    global gCounter
    global gPlanGrid
    global gSamplingList
    global gSamplingCount
   
    number_list = ['1.','2.','3.','4.','5.','6.','7.','8.','9.','10.']
    player = ['Never','Gonna','Give','You','Up','Never','Gonna','Let','You','Down']
    score = [56,53,52,52,51,51,50,49,26,25]
    for i in range(len(gPlanGrid)):
        for x in range(len(gPlanGrid)):
            if gPlanGrid[i][x] == '     ':
                value = False

            elif total_sum < 25:
                value = False
            
            
            else:
                    
                value = True
    if value == False:

        print('--------- HIGH SCORES ---------')
        print('Pos Player                Score')
        print('--- ------                -----')

        for i in range(len(player)):
    
            print('{:^5s}{:<7s}{:^32d}'.format(number_list[i],player[i],score[i]))
    else:
        
        if total_sum > 25:
            score.append(total_sum)
        score.sort()
        score.remove(score[0])
#print(score)
        index = score.index(total_sum)
#print(index)
        position = 0

        if index == 0:
            position = 10
        else:
            position = 10-index
    
        print('Congratulations! You made the high score board at position {}!'.format(position))
        name = input('Please enter your name (max 20 chars):')
        player.remove(player[9])
        player.insert(position -1, name)
        print('--------- HIGH SCORES ---------')
        print('Pos Player                Score')
        print('--- ------                -----')
        score.sort(reverse = True)
        for i in range(len(player)):
    
            print('{:^5s}{:<7s}{:^32d}'.format(number_list[i],player[i],score[i]))


def BCHScoring():
    '''--------------------------------------------------------------------------------------------------
    Check the building beach in the PlanGrid and assign the score accordingly.
    --------------------------------------------------------------------------------------------------'''
    global gCounter
    global gPlanGrid
    global gSamplingList
    global gSamplingCount
    lCounter = 0
    list_bch = []
    for i in range(len(gPlanGrid)):
    #print('A1:',list_bch)
        for f in range(len(gPlanGrid)):
            if (gPlanGrid[f][i] == ' BCH '):
                if ((i == 0) or (i == 3)):
                    lCounter = 3
                    list_bch.append(lCounter)
                else:
                    lCounter = 1
                    list_bch.append(lCounter)
    if list_bch == []:
        print('BCH: 0')
        add_bch = 0
    else:
        
        list_bch.sort(reverse = True)
        add_bch = sum(list_bch)
        list_BCH = ' + '.join([str(item) for item in list_bch]) + ' = '+str(add_bch)

        print('BCH:',list_BCH)
    return add_bch 

def FACScoring():
    '''--------------------------------------------------------------------------------------------------
    Check the building Factory in the PlanGrid and assign the score accordingly.
    --------------------------------------------------------------------------------------------------'''
    global gCounter
    global gPlanGrid
    global gSamplingList
    global gSamplingCount
    lCounter = 0
    add = 0
    list_fac = []
    appending = []
    import math
    for i in range(len(gPlanGrid)):
        for f in range(len(gPlanGrid)):
            if (gPlanGrid[f][i] == ' FAC '):
                lCounter = 1
                list_fac.append(lCounter)

    if len(list_fac) < 5:
        for x in range(len(list_fac)):
        
            appending.append(len(list_fac))
    else:
        appending = [4, 4, 4, 4]
        for x in range(len(list_fac) - 4):
            appending.append(1)
    
    if appending == []:
        print('FAC: 0')
        add_fac = 0
    else:
        appending.sort(reverse = True)
        add_fac = sum(appending)
        list_FAC = ' + '.join([str(item) for item in appending]) + ' = '+ str(add_fac)
        print('FAC:',list_FAC)
    return add_fac

def HSEScoring():
    '''--------------------------------------------------------------------------------------------------
    Check the building House in the PlanGrid and assign the score accordingly.
    --------------------------------------------------------------------------------------------------'''
    global gCounter
    global gPlanGrid
    global gSamplingList
    global gSamplingCount
    list2 = []
    for i in range(len(gPlanGrid)):
        for f in range (len(gPlanGrid)):
            if gPlanGrid[i][f] == ' HSE ':
                list1 = [i,f]
                list2.append(list1)
    #print(list2)
    ##### adding the cell nest to the HSE cell
    LIST_RFRONT = []
    for i in range(len(list2)):
        appendinglist = []
        if list2[i][1] != 3:
            x =  list2[i][1] + 1
            y = list2[i][0]
            appendinglist.append(gPlanGrid[y][x])
            LIST_RFRONT.append(appendinglist)
        else:
            appendinglist = ['     ']
            LIST_RFRONT.append(appendinglist)
#print(LIST_RFRONT)
##### adding the cell BEFORE the HSE cell into a combined nested list
    for i in range(len(list2)):
        appendinglist = []
        if list2[i][1] != 0:
        
            x = list2[i][1] -1
            y = list2[i][0]
            LIST_RFRONT[i].append(gPlanGrid[y][x])
        #appendinglist.append(gPlanGrid[y][x])
        #LIST_RBACK.append(appendinglist)
        else:
            empty = '     '
            LIST_RFRONT[i].append(empty)

#print(LIST_RFRONT)
###### adding the cell INFRONT of the HSE cell
    for i in range(len(list2)):
        if list2[i][0] != 3:
            x = list2[i][0] + 1
            y = list2[i][1]
            LIST_RFRONT[i].append(gPlanGrid[x][y])
        else:
            empty = '    '
            LIST_RFRONT[i].append(empty)

#print(LIST_RFRONT)        
##### adding the cell BEHIND of the HSE cell
    for i in range(len(list2)):
    
        if list2[i][0] != 0:
            x = list2[i][0] - 1
            y = list2[i][1]
            LIST_RFRONT[i].append(gPlanGrid[x][y])
        else:
            empty = '     '
            LIST_RFRONT[i].append('     ')
#print(LIST_RFRONT)  
    hse_list = []

    for i in range(len(LIST_RFRONT)):
        list9 = []
        for x in range(len(LIST_RFRONT[i])):
        #list9 = []
            if LIST_RFRONT[i][x] == ' FAC ':
                list9.append(1)
            #print('fac')
            #hse_list.append(list9)
                break
            else:
                if LIST_RFRONT[i][x] == ' HSE ' or LIST_RFRONT[i][x] == ' SHP ':
                    list9.append(1)
                #print('hse/shp')
                elif LIST_RFRONT[i][x] == ' BCH ':
                    list9.append(2)
                #print('bsh')
                else:
                    list9.append(0)
                #print('nothing past that')
        hse_list.append(list9)
    
#print(hse_list)
    sum_list = []
    for i in range(len(hse_list)):
        add = 0
        for x in range(len(hse_list[i])):
            add = add + hse_list[i][x]
        sum_list.append(add)
#print(sum_list)

    if sum_list == []:
        print('HSE: 0')
        add_hse = 0
    else:
        add_hse = sum(sum_list)
        list_HSE = ' + '.join([str(item) for item in sum_list]) + ' = '+ str(add_hse)
        print('HSE:',list_HSE)
    return add_hse

def HWYScoring():
    '''--------------------------------------------------------------------------------------------------
    Check the building Highway in the PlanGrid and assign the score accordingly.
    --------------------------------------------------------------------------------------------------'''
    global gCounter
    global gPlanGrid
    global gSamplingList
    global gSamplingCount
    list_hwy_combine = []
    list_hwy_alone = []
    for i in range(len(gPlanGrid)):
        for f in range(len(gPlanGrid)):
            if gPlanGrid[i][f] == ' HWY ':
                if (f != 3 and gPlanGrid[i][f+1] == ' HWY ') or (f != 0 and gPlanGrid[i][f-1] == ' HWY '):
                    list_hwy_combine.append(i)
                else:
                    list_hwy_alone.append(i)
    list_HWY = [] 
    for i in range(len(gPlanGrid)):
        count = list_hwy_combine.count(i)
        if count > 0:
            for i in range(count):
                list_HWY.append(count)

            
    for x in range(len(list_hwy_alone)):
        list_HWY.append(1)
    

#print(list_HWY)
    if list_HWY == []:
        print('HWY: 0 ')
        add_hwy = 0
    else:
        
        add_hwy = sum(list_HWY)
        main_hwy = ' + '.join([str(item) for item in list_HWY]) + ' = '+ str(add_hwy)
        print('HWY:',main_hwy)
    return add_hwy

def MONScoring():
    '''--------------------------------------------------------------------------------------------------
    Check the building MON in the PlanGrid and assign the score accordingly.
    --------------------------------------------------------------------------------------------------'''
    global gCounter
    global gPlanGrid
    global gSamplingList
    global gSamplingCount
    lCounter = 0
    total_list = []
    corner_count = []
    list_mon = []
    for i in range(len(gPlanGrid)):
        for f in range(len(gPlanGrid)):
            if (gPlanGrid[i][f] == ' MON '):
                #print(gPlanGrid[i][f],i,f)
            
                if i == 0 and f == 0: 
                    corner_count.append(1)
                elif i == 0 and f == 3:
                    corner_count.append(1)
                elif i == 3 and f == 0:
                    corner_count.append(1)
                elif i == 3 and f == 3 :
                    corner_count.append(1)
                else :
                    total_list.append(1)
            #print('conrner:',corner_count)
            #print('total:',total_list)
                
    if sum(corner_count) >= 3:
        for x in range(len(corner_count) + len(total_list)):
            list_mon.append(4)
    else:
        for x in range(len(corner_count)):
            list_mon.append(2)
        for i in range(len(total_list)):
            list_mon.append(1)
    if list_mon == []:
        print('MON: 0')
        add_mon = 0
    else:
        
        list_mon.sort(reverse = True)
        add_mon = sum(list_mon)
        list_MON = ' + '.join([str(item) for item in list_mon]) + ' = '+ str(add_mon)
        print('MON:',list_MON)
    return add_mon


def PRKScoring():
    '''--------------------------------------------------------------------------------------------------
    Check the building park in the PlanGrid and assign the score accordingly.
    --------------------------------------------------------------------------------------------------'''
    global gCounter
    global gPlanGrid
    global gSamplingList
    global gSamplingCount
    nestedlist = []
    r_count_list = []
    r_rand_list = []
    lCounter = 0
    #col lists
    col_count_list = []
    col_rand_list = []

    #### goes by row
    for i in range(len(gPlanGrid)):
        for f in range(len(gPlanGrid)):
            if gPlanGrid[i][f] == ' PRK ':
                lCounter += 1
            
                if f != 3 and gPlanGrid[i][f+1] == ' PRK ':
                    nestedlist = [i,f]
                    r_count_list.append(nestedlist)
                elif f != 0 and gPlanGrid[i][f-1] == ' PRK ':
                    nestedlist = [i,f]
                
                    col_count_list.append(nestedlist)
                elif gPlanGrid[i][3] == ' PRK ' and gPlanGrid[i][2] == ' PRK ':
                    nestedlist = [i,3]
                    r_count_list.append(nestedlist)
                else :
                    nestedlist = [i,f]
                    r_rand_list.append(nestedlist)
                
    for i in range(len(gPlanGrid)):
        for f in range(len(gPlanGrid)):
            if gPlanGrid[f][i] == ' PRK ':
            #print(f,i)
                if f != 3 and gPlanGrid[f+1][i] == ' PRK ':
                    nestedlist = [f,i]
                #print('i != 3:',f,i)
                    col_count_list.append(nestedlist)
                elif f != 0 and gPlanGrid[f-1][i] == ' PRK ':
                    nestedlist = [f,i]
                
                    col_count_list.append(nestedlist)
                elif gPlanGrid[3][i] == ' PRK ' and gPlanGrid[2][i] == ' PRK ':
                    nestedlist = [3,i]
                    col_count_list.append(nestedlist)
                else:
                    nestedlist = [f,i]
                    col_rand_list.append(nestedlist)
    number = 0
    count = 0

    for j in range(len(col_count_list)):
        for x in range(len(r_count_list)):
        
            if col_count_list[j] ==  r_count_list[x]:
                number += 1


    score_continue = len(col_count_list) + len(r_count_list) - number



    for j in range(len(col_rand_list)):
        for x in range(len(r_rand_list)):
        
            if col_rand_list[j] == r_rand_list[x]:
               count += 1

    list1 = [[1,1],[2,3],[3,8],[4,16],[5,22],[6,23],[7,24],[8,25]]
    prk_score = []
    for x in range(len(list1)):
        if score_continue == list1[x][0]:
            prk_score.append(list1[x][1])
    for i in range(count):
        prk_score.append(1)
        
    if prk_score == []:
        print('PRK: 0')
        add_prk = 0
    else:
        
        prk_score.sort(reverse = True)
        add_prk = sum(prk_score)
        list_PRK =' + '.join([str(item) for item in prk_score]) + ' = '+ str(add_prk)
        print('PRK:',list_PRK)
    return add_prk

def SHPScoring():
    '''--------------------------------------------------------------------------------------------------
    Check the building shop in the PlanGrid and assign the score accordingly.
    --------------------------------------------------------------------------------------------------'''
    global gCounter
    global gPlanGrid
    global gSamplingList
    global gSamplingCount
    list2 = []
    for i in range(len(gPlanGrid)):
        for f in range(len(gPlanGrid)):
            if gPlanGrid[i][f] == ' SHP ':
                list1 = [i,f]
                list2.append(list1)
#print(list2)
##### adding the cell nest to the HSE cell
    LIST_RFRONT = []
    for i in range(len(list2)):
        appendinglist = []
        if list2[i][1] != 3:
            x =  list2[i][1] + 1
            y = list2[i][0]
            appendinglist.append(gPlanGrid[y][x])
            LIST_RFRONT.append(appendinglist)
        else:
            appendinglist = ['     ']
            LIST_RFRONT.append(appendinglist)
#print(LIST_RFRONT)
##### adding the cell BEFORE the HSE cell into a combined nested list
    for i in range(len(list2)):
        appendinglist = []
        if list2[i][1] != 0:
        
            x = list2[i][1] -1
            y = list2[i][0]
            LIST_RFRONT[i].append(gPlanGrid[y][x])
        #appendinglist.append(gPlanGrid[y][x])
        #LIST_RBACK.append(appendinglist)
        else:
            empty = '     '
            #LIST_RFRONT[i].append(empty)

#print(LIST_RFRONT)
###### adding the cell INFRONT of the HSE cell
    for i in range(len(list2)):
        if list2[i][0] != 3:
            x = list2[i][0] + 1
            y = list2[i][1]
            LIST_RFRONT[i].append(gPlanGrid[x][y])
        else:
            empty = '    '
        #LIST_RFRONT[i].append(empty)

#print(LIST_RFRONT)        
##### adding the cell BEHIND of the HSE cell
    for i in range(len(list2)):
    
        if list2[i][0] != 0:
            x = list2[i][0] - 1
            y = list2[i][1]
            LIST_RFRONT[i].append(gPlanGrid[x][y])
        else:
            empty = '     '
        #LIST_RFRONT[i].append('     ')
#print(LIST_RFRONT)  
    hse_list = []
    list9 = []
    for i in range(len(LIST_RFRONT)):
    
        list10 = list(dict.fromkeys(LIST_RFRONT[i]))
    
        list9.append(list10)
    
#print(list9)
    list_shp = []

    for i in range(len(list9)):
        list10 = []
        for x in range(len(list9[i])):
            if list9[i][x] == '     ':
                list10.append(0)
            else:
            
                list10.append(1)
        list_shp.append(list10)
            



    sum_list = []
    for i in range(len(list_shp)):
        add = 0
        for x in range(len(list_shp[i])):
            add = add + list_shp[i][x]
        sum_list.append(add)


    if sum_list == []:
        print('SHP: 0')
        add_shp = 0
    else:
        
        add_shp = sum(sum_list)
        list_SHP = ' + '.join([str(item) for item in sum_list]) + ' = '+ str(add_shp)
        print('SHP:',list_SHP)                
    return add_shp
 

def BuildCity(Build, GridLoc,Turn):
    '''--------------------------------------------------------------------------------------------------
    It gets the building(Build) and the location(GridLoc) and the number of turns and append the building accordingly.
    --------------------------------------------------------------------------------------------------'''
    global gCounter
    global gPlanGrid
    global gSamplingList
    global gSamplingCount
    iCount=0
 
    for x in range(len(gSamplingList)):
        gSamplingCount[x]=0
        

    GridLoc=GridLoc.upper()

    if Build != '':
        index = int(GridLoc[1]) - 1
        if GridLoc[0] == 'A':
            gPlanGrid[index][0] = ' {} '.format(Build)
        if GridLoc[0] == 'B':
            gPlanGrid[index][1] = ' {} '.format(Build)
        if GridLoc[0] == 'C':
            gPlanGrid[index][2] = ' {} '.format(Build)
        if GridLoc[0] == 'D':
            gPlanGrid[index][3] = ' {} '.format(Build)


        if Turn == 16:
            print('\n\nFinal layout of Simp City:')
            print('------------------------------------------------------\n')
        else:
            print('Turn',Turn + 1)

    rowln=' +'
    for row in range(len(gPlanGrid)):
        rowln=rowln+'-----+'

    print('     A     B     C     D        Building     Remaining')
    print('',rowln,'    --------     ---------')
    iCount=0
    for i in range(len(gPlanGrid)):
        rowdt="|"
        rd=''
        for j in range(len(gPlanGrid)):
            rowdt = rowdt + gPlanGrid[i][j] + '|'

            for k in range(len(gSamplingList)):
                gSamplingCount[k]=0
                for m in range(len(gPlanGrid)):
                    for n in range(len(gPlanGrid)):
                        if (gPlanGrid[m][n].strip() == gSamplingList[k].strip()):
                            gSamplingCount[k]+=1

        rd=str(i+1) + ' ' + rowdt

        if (i < 2):
            print(rd,'    ' + gSamplingList[iCount] + '          ' + str(8-gSamplingCount[iCount]))
            print(' ' + rowln + '     ' + gSamplingList[iCount+1] + '          ' + str(8-gSamplingCount[iCount+1]))
        elif (i == 2) :
            print(rd,'    ' + gSamplingList[iCount] + '          ' + str(8-gSamplingCount[iCount]))
            print(' ' + rowln)
        else:
            print(rd)
            print(' ' + rowln)
        iCount+=2

    return 


def CheckValidity(GridLocation):
    '''--------------------------------------------------------------------------------------------------
    Check the building location and will infrom if the placement of building is acceptable.
    --------------------------------------------------------------------------------------------------'''
    global gCounter
    global gPlanGrid
    global gSamplingList
    global gSamplingCount
    alphaS=GridLocation[0].upper()
    numberS=GridLocation[1]

    alpha = ord(alphaS)-65
    number=int(numberS) - 1
    list1 = []
    neighbore = []
 

    if gPlanGrid[number][alpha] != '     ':
        print('Cell Already Filled. Try with empty cell')
        return False

    if alpha + 1 < 4:
        neighbore.append(gPlanGrid[number][alpha + 1])
    if alpha - 1 > -1:
        neighbore.append(gPlanGrid[number][alpha -1])
    if number + 1 < 4:
        neighbore.append(gPlanGrid[number + 1][alpha])
    if number - 1 > -1:
        neighbore.append(gPlanGrid[number - 1][alpha])
        
    for x in range(len(neighbore)):
        if neighbore[x] !='     ':
            list1.append(neighbore[x])
        else:
            continue

    if len(list1) <= 0:
        print('Invalid Placement...')
        return False

    return True

###MAIN PROGRAM####    
#add diemension here
'''--------------------------------------------------------------------------------------------------
The main Program is written here, setting up global varibale and printing the main menu
Author: Jyoshika Barathimogan
Date: 9 Aug 2021
number: S10222388e
--------------------------------------------------------------------------------------------------'''
option1=''
option2=''
option3=''
option4=''
option5=''
ReturnVal=True

global gPlanGrid
global gSamplingList
global gSamplingCount
global gCounter



gPlanGrid = [  ['     ','     ','     ','     '],\
               ['     ','     ','     ','     '],\
               ['     ','     ','     ','     '],\
               ['     ','     ','     ','     '] ]

gSamplingList = []
gSamplingCount = [0,0,0,0,0]
gCounter = 0
answer = 1

while answer != 0:
    
    print('Welcome, Mayor of Simp City !')
    print('-----------------------------')

    print('1. Start a new game')
    print('2. Load saved game')
    print('3. Show high score')
    print('')
    print('')
    print('0. Exit')

    while True:
        try:
           answer = int(input('Your choice?'))
        except ValueError:
           print("Not an integer! Try again.")
           continue
        if ((answer < 0) or (answer > 4)):
            print('Valid values are 0 or 1 or 2 or 3. Enter valid value.')
            continue
        else:
           break
     
    if answer == 1:
        StartGame(option1,option2,option3,option4,option5,'N')
    elif answer == 2:
        LoadGame()

        print(gCounter)
        StartGame(option1,option2,option3,option4,option5,'Y')
    elif answer == 3:
        HighScoreBoard(0)
        
