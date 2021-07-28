import random
import time
import speech_recognition as sr

def recognize_speech_mic(recognizer, microphone):

    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # if a RequestEror or UnknownValueError exception is caught, update response
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unaviable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response

if __name__ == "__main__":
    NAMES = ["thomas", "pablo", "franklin", "james", "robert"]
    NUM_GUESSES = 3
    QLIMIT = len(NAMES) 

    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # random word from the list
    name = random.choice(NAMES)

    # format the instructions string
    instructions = (
        "I'm thinking of one of the these names:\n"
        "{names}\n"
        "You have {n} tries to guess which one.\n"
    ).format(names=', '.join(NAMES), n=NUM_GUESSES)


    # show instructions and wait 3 seconds before starting the game
    print(instructions)
    time.sleep(3)

#    for i in range(NUM_GUESSES):
#        guess = recognize_speech_mic(recognizer, microphone)
#        print('Guess {}. Speak!'.format(i+1))
#        for j in range(len(NAMES)):
#            if guess["transcription"]:
#                break
#            if not guess["success"]:
#                break
#            print("I didn't catch that. What did you say?\n")
#
#        if guess["error"]:
#            print("ERROR: {}".format(guess["error"]))


    for i in range(NUM_GUESSES-1):
        print('Guess {}. Speak!'.format(i+1))
        guess = recognize_speech_mic(recognizer, microphone)
        for j in range(QLIMIT):
            if guess["transcription"]:
                break
            if not guess["success"]:
                break
            print("I didn't catch that. Repeat please ... ")
            guess = recognize_speech_mic(recognizer, microphone)
            
        #if error then break the game
        if guess["error"]:
            print("EROR: {}".format(guess["error"]))
            break

        # show user guess
        print("You said: {}".format(guess["transcription"]))

        # calculate
        guess_is_correct = guess["transcription"].lower() == name.lower()


        if guess_is_correct:
            print("Correct! You win!".format(name))
            break
        elif i < NUM_GUESSES:
            print("Incorrect. Try again.\n")
        else:
            print("Sorry, you lose!\nThe answer was: '{}'".format(name))
        


