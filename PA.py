
print("loading")
import speech_recognition as sr 
import pyttsx3 as tts
import os 
import random
import pyaudio as audio
import ssl
import smtplib 
import hashlib
engine = tts.init() 
print('done initializing of speech-engine')

print('setting up parameters for speech-engine')
speechRate = 118
speechVolume = 2.0
engine.setProperty('rate', speechRate)
engine.setProperty('volume', speechVolume)
voices = engine.getProperty('voices')
#engine.setProperty('voice', voice[0].id)
print('speech-engine set-up complete')
engine.say("Speech engine is online")
engine.runAndWait()

print('rounding up settings for mainloop')
access = False
controlToken = random.randint(1, 999999)
alfaList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
f = open("UserConfig.txt","r")
fl = f.readlines()
splitUserEmail = fl[0].split(";")
user_email = splitUserEmail[1] 
tripleHashedPassword = "e7cf4d3d282290d468c3d47d0da919a0aa689633aab7da72b035114a6c41b592"
masterPassword = ""
#-8270611463877889932
def contactList(addperson='',addemail=''):   #FORMAT will be: {naam, email}
    contactsLibrary = {}
    if addperson != '' and addemail != '': contactsLibrary.update({addperson:addemail})
    return(contactsLibrary)

def tripleHash(plaintext):
    hash1 = hashlib.sha256(str(plaintext).encode('utf-8'))
    view = hash1.hexdigest()
    return(view)

def securekeyGenerator(controlToken=controlToken, alfaList=alfaList):
    r = str(controlToken)
    rL = alfaList[(random.randint(1, 25))]
    splitL = []
    for i in r:
        splitL.append(i)
    splitL.insert(1, rL)
    securityKey = ''.join(splitL)
    return securityKey 

controlSecureKey = str(securekeyGenerator())
#print(controlSecureKey)        #testing purposes only

def emailSender(message, receiverEmail, emailerPassword=masterPassword):
    content = message
    sender_email = "ctrcG285192044py@gmail.com"
    password = emailerPassword
    receiver_email = receiverEmail
    port = 587
    smtp_server = "smtp.gmail.com"
    mail = smtplib.SMTP(smtp_server, port)
    mail.ehlo()
    mail.starttls()
    mail.login(sender_email, password)
    mail.sendmail(sender_email, receiver_email, content)

def initFace(Type):
    if Type == 'listening':
        print("", '\n' * 50)
        print("########################################################", '\n'
"####################****************####################", '\n'
"#################********************###################", '\n'
"###############**********************###################", '\n'
"##############*****__*********__******##################", '\n'
"##############************************##################", '\n'
"#############******/\*********/\******##################", '\n'
"#############******\/*********\/******##################", '\n'
"#############***********| ************##################", '\n'
"#############**********/  ************##################", '\n'
"#############*********/__*************##################", '\n'
"##############***********************###################", '\n'
"###############*********************####################", '\n'
"################*****=======*******#####################", '\n'
"##################****************######################", '\n'
"####################************########################", '\n'
"########################################################")
        print("", '\n' * 10)
    elif Type == 'sleeping':
        print("", '\n' * 50)
        print("########################################################", '\n'
"####################****************####################", '\n'
"#################********************###################", '\n'
"###############**********************###################", '\n'
"##############************************##################", '\n'
"##############*****__*********__******##################", '\n'
"#############*************************##################", '\n'
"#############******\/*********\/******##################", '\n'
"#############***********| ************##################", '\n'
"#############**********/  ************##################", '\n'
"#############*********/__*************##################", '\n'
"##############***********************###################", '\n'
"###############*********************####################", '\n'
"################*****_______*******#####################", '\n'
"##################****************######################", '\n'
"####################************########################", '\n'
"########################################################")
        print("", '\n' * 10)
    elif Type == 'speaking':
        print("", '\n' * 50)
        print("########################################################", '\n'
"####################****************####################", '\n'
"#################********************###################", '\n'
"###############**********************###################", '\n'
"##############*****__*********__******##################", '\n'
"##############************************##################", '\n'
"#############******/\*********/\******##################", '\n'
"#############******\/*********\/******##################", '\n'
"#############***********| ************##################", '\n'
"#############**********/  ************##################", '\n'
"#############*********/__*************##################", '\n'
"##############***********************###################", '\n'
"###############*******_______*******####################", '\n'
"################******\_____/******#####################", '\n'
"##################****************######################", '\n'
"####################************########################", '\n'
"########################################################")
        print("", '\n' * 10)

def speak(audiostring):
    print(audiostring)
    engine.say(audiostring)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    source = sr.Microphone()
    try:
        sound = r.listen(source, 10)
    except:
        speak("I can't hear you")

def centricMainCore(access):
    active = True

    def listen():
        initFace('listening')
        textI = ""
        r = sr.Recognizer()
        source =  sr.Microphone()
        sound = r.listen(source, 10)
        try:
            textI = r.recognize_sphinx(sound)
            print("     ", textI)
        except:
            speak("Sorry, I can't hear you")
        if textI != "":
            return(textI)
    
    #defining alle andere core functionalities van Centric hier binnen MainCore
    #functie afmaken om centric zinnen te laten filteren op zelfstandige naamwoorden, bijvoeglijke naamwoorden, namen, nummers en voorzetsels
    #ook basis standaardcommando's toevoegen als 'ja' en 'nee'
    def askForInput(questionstring):
        speak(questionstring)
        answer = listen()
        returnBool = False
        userAnswer = ""
        if answer != '':
            if answer == 'yes': returnBool = True
            elif answer == 'no': returnBool = False
            userAnswer = str(returnBool)
        return userAnswer

    def textToDigit(string):
        listOfNumbers = string.split(' ')
        onesDict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
        betweensDict = {'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19}
        tensDict = {'ten':10, 'twenty':20, 'thirty':30, 'forty':40, 'fifty':50, 'sixty':60, 'seventy':70, 'eigty':80, 'ninety':90}
        greatsDict = {'hundred':100, 'thousand':1000, 'million':1000000}
        #de SR geeft aan de hand van de gebruikte dictionary een string bestaande uit deze string-variabelen.
        numberOfElements = len(listOfNumbers) #geeft aantal elementen van het getal bijvoorbeeld [1, 2, 3] --> 3
        sort = ''
        placeIndex = 0
        subList = []
        fullList = []
        digitversion = 0
        for element in listOfNumbers:
            if element in onesDict: 
                sort='ones'
                digitversion = onesDict[element]
            elif element in betweensDict: 
                sort='betweens'
                digitversion = betweensDict[element]
            elif element in tensDict: 
                sort='tens'
                digitversion = tensDict[element]
            elif element in greatsDict: 
                sort='greats'
                digitversion = greatsDict[element]
            if sort != '':
                subList.append(digitversion)  #was eerst element
                subList.append(sort)
                subList.append(placeIndex)     #sublist is nu bijvoorbeeld [4,'ones',1]
            placeIndex += 1
            fullList.append(subList)           #fullList is nu dan bijvoorbeeld [[20,'betweens',0],[4,'ones',1]]
        eindCijfer = 0
        CijfersEnHandelingen = []
        try:
            while i < len(fullList): 
                tussenLijst = []
                next = i+1
                handeling = ''
                if fullList[i[1]] == 'ones' and fullList[next[1]] == 'greats': handeling='*'       #2 100 = 200
                elif fullList[i[1]] == 'tens' and fullList[next[1]] == 'ones': handeling='+'       #20 2 = 22
                elif fullList[i[1]] == 'tens' and fullList[next[1]] == 'greats': handeling='*'     #30 1000 = 30000
                elif fullList[i[1]] == 'betweens' and fullList[next[1]] == 'greats': handeling='*' #13 100 = 1300
                first = fullList[i[0]]
                second = fullList[next[0]]

                tussenLijst.append(first)
                if handeling != '': tussenLijst.append(handeling)
                tussenLijst.append(second)
                cijfersEnHandelingen.append(tussenLijst)
                ####....
                i += 2
        except:
            #alleen voor laatste item in de lijst
            #dit cijfer moet dan achteraan CijfersEnHandelingen[] opgeslagen worden met handeling '+'
            #hierna kan alles verwerkt worden naar eindCijfer
            lastIndex = (len(fullList) - 1)
            i = lastIndex
            tussenLijst = []
            cijfer = fullList[i[0]]
            tussenLijst.append(cijfer)
            tussenLijst.append('+')
            #tussenLijst.append(0)
            cijfersEnHandelingen.append(tussenLijst)  # nu moet deze lijst uitzien als [[6,*,1000],[2,*,100],[50,+,2]]  of [[2,*,100],[2,+]]
            done = True

        if cijfersEnHandelingen != []:
            for element in cijfersEnHandelingen:
                if len(element) == 3:
                    if element[1] == '*':
                        eindCijfer = eidCijfer + (element[0] * element[2])
                    elif element[1] == '+':
                        eindCijfer = eindCijfer + (element[0] + element[2])
                elif len(element) == 2:
                    eindCijfer = eindCijfer + element[1]   #omdat het laatste getal altijd opgeteld wordt als het apart staat ([2,+])
        else:
            print('There was an error while proccessing spoken number! sorry.')

        return(eindCijfer)


    #(alle commandofuncties komen hier)

    def protocol(string):
        splitString = string.split(' ')

    def search(string):
        splitString = string.split(' ')

    def contact(masterPassword=masterPassword):   #line 33 contacts function
        persons = contactList()
        speak("please type the contact name")
        name = raw_input(':> ')
        try:
            gegevenEmail = persons[name]
            speak("please tell me your message")
            textToSend = listen()
            emailSender(textToSend, gegevenEmail, masterPassword)
        except:
            print("Sorry, this person is not in your contact list")
            gegeven = ''
            speak("Sorry, i can not find that person")
            addPersonBool = askForInput("Would you like me to add this person to your list")
            if addPersonBool == "True":
                speak("please enter the name and mail")
                naamVanPersoon = input('Naam: ')
                mailVanPersoon = input('Mail: ')
                contactList(naamVanPersoon, mailVanPersoon)

    def sentenceAnalyzer(string):
        splitString = string.split(' ')
        lidWoordLibrary = ['the','a','an']
        vraagWoordLibrary = ['what', 'when', 'where', 'who', 'how']  #keyWordLibraries vullen met woorden voor 'betekenisherkenning'
        vraagWoordLibraryCounter = {'what':'what', 
                                    'when':'time', 
                                    'where':'place',
                                    'who':'person', 
                                    'how':'how'} #what en how niet echt te vertalen naar een kernwoord
        #meestal komt een werkwoord na een vraagwoord
        tussenvoegLibrary = ['of', 'in', 'about']
        commandLibrary = ['contact', 'search','protocol'] #commando's toevoegen die centric kan gebruiken
        werkWoordLibrary = []   #dictionary voor werkwoorden en vervoegingen
        #werkwoorden noteren als [['walk','walks','walking'],['eat','eats','eating']]

        entriesLidwoorden = []
        entriesVraagwoorden = []
        entriesCommands = []
        entriesTussenvoeg = []
        entriesWerkWoord = []
        keyWords = []
        for i in range(len(splitString)):
            intermediateList = []
            position = i
            word = splitString[i]
            intermediateList.append(word)
            intermediateList.append(position) #geeft bijvoorbeeld ['the', 2]
            if word in lidWoordLibrary:
                entriesLidwoorden.append(intermediateList)
            elif word in vraagWoordLibrary:
                entriesVraagwoorden.append(intermediateList)
            elif word in tussenvoegLibrary:
                entriesTussenvoeg.append(intermediateList)
            elif word in commandLibrary:
                entriesCommands.append(intermediateList)
            else:
                for z in werkWoordLibrary:
                    if splitString[i] in z:
                        infinitifWerkwoord = z[0]
                        entriesWerkWoord.append(infinitifWerkwoord)

        try:                                          #voorbeeld: "search how old can a horse get?"
            for j in entriesLidwoorden:                        #het eerste woord na een lidwoord opslaan
                positionOfLidwoord = int(j[1])        
                positionOfNextWord = positionOfLidwoord + 1
                actualNextWord = splitString[positionOfNextWord]
                keyWords.append(actualNextWord)
            for k in entriesVraagwoorden:                     #het eerste woord na een vraagwoord opslaan
                positionOfVraagwoord = int(k[1])
                positionOfNextWord = positionOfVraagwoord + 1
                actualNextWord = splitString[positionOfNextWord]
                keyWords.append(actualNextWord)
            for l in entriesTussenvoeg:
                positionOfTussenvoeg = int(l[1])              #het eerste woord na een tussenvoegsel opslaan
                positionOfNextWord = positionOfTussenvoeg + 1
                actualNextWord = splitString[positionOfNextWord]
                keyWords.append(actualNextWord)
            for m in entriesWerkwoorden:
                keyWords.append(m)
            for n in entriesCommands:
                keyWords.insert(0,n)      #zorgen dat het commandowoord altijd als eerste in de opdracht staat.
        except:                                     #dit moet nu geven "search how horse old"
            print('error while building search term grammatics. Not necessarily a bad thing!')

        #alle vraagwoorden in de keyWords[] vervangen door hun Counter IN k-for-loop!!
        newKeyWords = []
        for word in keyWords:
            if word in vraagWoordLibrary:
                counter = vraagWoordLibraryCounter[word]
                newKeyWords.append(counter)
            else:
                newKeyWords.append(word)
        keyWords = newKeyWords                      #nu moet er (in dit geval nogsteeds) "search how horse old" staan
        #de keywordList omzetten naar een commando en een rest
        command = keyWords[0]
        keyWords.remove(command)
        rest = ' '.join(keyWords)
        #entriesCommands verwerken in de zin en commando's omzetten naar instructies
        return command, rest

    print("Entered Main Program Loop!")
    speak("welcome")
    while active:
        text = listen() #de text die hier uit volgt moet een string zijn. deze zou gesplit kunnen worden per woord.
        #splitten van een lijst:    index[0] = commando, rest = indeling afhankelijk van werking specifieke commando
        givenCommand, givenParameters = sentenceAnalyzer(text)
        if givenCommand == 'contact': contact()
        elif givenCommand == 'protocol': protocol(givenParameters)
        elif givenCommand == 'search': search(givenParameters)


speak("please log in to use the engine")
masterPassword = raw_input("give masterpassword: ")
#invoeren wachtwoord voor toegang 
hashedInput = tripleHash(masterPassword)
if hashedInput == tripleHashedPassword:
    emailSender(controlSecureKey, user_email, masterPassword)
    print("password correct,")  #gebruiker krijgt mail toegestuurd met toegangscode voor programma
    token = raw_input("enter received token: ")
    #print(token)
    if token == controlSecureKey: 
        access = True
        speak("correct log in details")
        centricMainCore(access)
    else:
        speak("incorrect log in")
        speak("please restart services")

print("End")