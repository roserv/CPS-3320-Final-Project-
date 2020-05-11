import random

# lists containing exercises based on muscle group 
back = ['renegade row', 'alternating single arm row', 'farmers carry', 'upright row', 'bentover reverse fly', 'resistance band face pulls', 
            'reverse snow angel', 'plank row', 'push up', 'extension plank', 'crab walk', 'resistance band pull apart', 'resistance band lat pulldown',
            'wide dumbell row', 'exercise ball hyperextension', 'plank renegade dumbbell row'  ]

biceps =  ['standing bicep curls', 'hammer curls', 'wide bicep curls', 'alternating bicep curls', 'reverse curls', 'zottman curls', 'crossbody curls', 'isolated single-arm curls',
            'weighted punches', 'seated bicep curls' ]

triceps = ['overhead extension', 'tricep kickbacks', 'skull crushers', 'resistance band tricep pull downs', 'tricep dips', 'tricep bow', ]

shoulders = ['side raises', 'front raises', 'shoulder shrugs', 'military press', 'arnold press', 'scarecrow press', 'arm circles' ]

chest = ['bentover chestfly', 'chest press', 'push ups', 'divebomb press-up' , 'incline push ups', 'standing chest fly', 'laying down chest fly', 'incline chest press']

lowerbody =  ['good mornings', 'deadlift', 'goblet squat', 'sumo squat', 'resistance band squats', 'sumo deadlift', 'squats', 'romanian deadlift', 'calf raises',
                'step-ups', 'side step resistance band squat', 'walking lunges', 'reverse lunges', 'curtsy lunge', 'glute bridges', 'squat jumps']

core = ['bicycle crunches', 'leg raises', 'heal touches', 'bird dog', 'knee to chest wood chop (each side)', 'spidermans', 'russian twists', 'sit ups', 
            'wide-legged alternating toe touch sit ups', 'flutter kicks', 'in and outs', 'v-up', 'sissors', 'roll ups', 'dead bugs', 'inch worms to plank',
            'seated around the world', 'standing around the world', 'raised straight leg alternating toe touch', 'side planks', 'burpes', 'plank shoulder taps',
            'plank up-downs', 'planks', 'forarm planks', 'spiderman planks']

circut = [['deadlift', 'hammer curl', 'squat', 'overhead press'], ['squat', 'alternating knee to chest'], ['deadlift', 'squat'] , ['step ups', 'knee to chest'], 
            ['front raise', 'side raise'], ['bicep curl', 'hammer curl'], ['plank updowns', 'plank shoulder taps'], ['russian twists', 'heal touches', 'toe taps']]



# function that returns a list of exercises based user input 
# takes the paremeters of a list of exercises and the number of exercises 
def returnExercises(list, num):
    exerciseList = []
    while num > 0:
        # selecting a random index from list
        exercise = random.choice(list)
        # to prevent duplicates
        # if exercise is already in exerciseList a new random value will be chosen utill there are no duplicates
        for i in exerciseList:
            while i == exercise:
                exercise = random.choice(list)
        # adding non-duplicated exercise to list 
        exerciseList.append(exercise)
        num = num-1

    # printing each element of exerciseList
    for i in exerciseList:
            print('-', i)
    
    
# function that pulls exercises from multiple groups 
def multipleGroups(list, num, numExercises):
    # to find how many exercises to pull for each group 
    numPerGroup = numExercises / num
    # calling returnExercises to randomly select exercises from the specific list at index i
    for i in list:
        returnExercises(i, numPerGroup)

# giving the user introduction to program
print('Welcome to the random workout generator!')  
print('You will be prompted with questions about the workout you would like. To make a selection, simply enter the number that corresponds to your selection.') 
print('Once all questions are answered you will recieve a generated random list of exercises to match your workout, so that you never get bored by the same routine') 
print()   
# Asking user exercise type and storing into variable 
print('What type of exercise would you like to do?')
print('\t1: stength training')
print('\t2: for circut training ')
exerciseType = input()

# if user chooses strength training, they are prompted with addtional choices 
if exerciseType == '1':
    print('What muscle group would you like to exercise? (upper body, lower body, full body, core) ')
    print('\t1: upper body')
    print('\t2: lower body')
    print('\t3: full body')
    print('\t4: core')
    muscleGroup = input()

    # if user chooses upper body, they are prompted with additional choices 
    if muscleGroup == '1':
        print('What type of upper body workout would you like?')
        print('\t1: All muscle groups')
        print('\t2: Push (chest, shoulders, triceps)')
        print('\t3: Pull (back & biceps)')
        print('\t4: A specific muscle group')
        selection = input()

        # if user selects all muscle groups
        if selection == '1':
            # prompting and retrieving number of exercises from user
            print('How many exercises would you like to do? (must be a multiple of 5. Ex. 5,10,15,20)')
            numExercises = input()
            numExercises = int(numExercises)

            print('\n', numExercises, 'upperbody exercises:')
            upperBodyGroups = [back, biceps, triceps, shoulders , chest]
            multipleGroups(upperBodyGroups, 5, numExercises)
            
        # if the user selects push
        if selection == '2':
            # prompting and retrieving number of exercises from user
            print('How many exercises would you like to do? (must be a multiple of 3. Ex. 3, 6, 9, 12, 15)')
            numExercises = input()
            numExercises = int(numExercises)
            
            print('\n', numExercises, 'push (chest, shoulders, triceps) exercises:')
            pushGroups = [triceps, shoulders, chest]
            multipleGroups(pushGroups, 3, numExercises)


        #  the user selects pull
        if selection == '3':
            # prompting and retrieving number of exercises from user
            print('How many exercises would you like to do? (must be a multiple of 2. Ex. 2, 4, 6, 8, 10)')
            numExercises = input()
            numExercises = int(numExercises)

            print('\n', numExercises, 'pull (back & biceps) exercises:')
            pullGroups = [back, biceps]
            multipleGroups(pullGroups, 3, numExercises)

        # if the user selects a specic muscle group 
        if selection == '4':
            # asking user to pick upper body muscle group from a list
            print('Pick a muscle group: ')
            print('\t1: Back')
            print('\t2: Biceps')
            print('\t3: Triceps ')
            print('\t4: Chest')
            print('\t5: Shoulders')
            group = input()

            # prompting and retrieving number of exercises from user
            print('How many exercises would you like to do?')
            numExercises = input()
            numExercises = int(numExercises)

            # if user selects back 
            if group == '1':
                print('\n', numExercises, 'back exercises:')
                returnExercises(back, numExercises)
            
            # if user selects biceps
            if group == '2':
                print('\n', numExercises, 'bicep exercises:')
                returnExercises(biceps, numExercises)

            # if user selects triceps
            if group == '3':
                print('\n', numExercises, 'triceps exercises:')
                returnExercises(triceps, numExercises)
            
            # if user selects chest
            if group == '4':
                print('\n', numExercises, 'chest exercises:')
                returnExercises(chest, numExercises)
            
            # if user selects shoulders
            if group == '5':
                print('\n', numExercises, 'shoulder exercises:')
                returnExercises(shoulders, numExercises)
    
    # if users selects lower body
    if muscleGroup == '2':
        # prompting and retrieving number of exercises from user
        print('How many exercises would you like to do?')
        numExercises = input()
        numExercises = int(numExercises)

        print('\n', numExercises, 'lowerbody exercises:')
        returnExercises(lowerbody, numExercises)

    # if user selects full body
    if muscleGroup == '3':
        # prompting and retrieving number of exercises from user
        print('How many exercises would you like to do? (must be a multiple of 7. Ex. 7, 14, 28)')
        numExercises = input()
        numExercises = int(numExercises)

        print('\n', numExercises, 'exercises for a full body workout:')
        fullBody = [back, biceps, triceps, chest, shoulders, lowerbody, core]
        multipleGroups(fullBody, 7, numExercises)
        
    # if user selects core
    if muscleGroup == '4':
        # prompting and retrieving number of exercises from user
        print('How many exercises would you like to do?')
        numExercises = input()
        numExercises = int(numExercises)

        print('\n', numExercises, 'core exercises:')
        returnExercises(core, numExercises)

# if the user selects circut training the are prompted with 2 options
if exerciseType == '2':
    # prompting and retrieving number of exercises from user
    print('How many exercises would you like to do?')
    numExercises = input()
    numExercises = int(numExercises)

    print('\n', numExercises, 'circut exercises:')
    returnExercises(circut, numExercises)

# Allowing the user to see any of the exercise lists for reference
print('\nWould you like to see the complete list of exercises for a specific muscle group?')
print('\t1: yes')
print('\t2: no')
completeList = input()

if completeList == '1':
    print('Which list would you like to print?')
    print('\t1: Back')
    print('\t2: Biceps')
    print('\t3: Triceps ')       
    print('\t4: Chest')
    print('\t5: Shoulders')
    print('\t6: lower body')
    print('\t7: core')
    print('\t8: circut')
    printList = input()
    printList = int(printList)

    allGroups = [back, biceps, triceps, chest, shoulders, lowerbody, core, circut]

    for i in allGroups[printList -1]:
        print('-', i)

if completeList == '2':
    print('Enjoy your workout!')




