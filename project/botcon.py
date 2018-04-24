import time
import argparse
import os
from utils import *
from dialogue_manager import DialogueManager

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--token', type=str, default='')
    return parser.parse_args()

def main():
    #args = parse_args()

    #################################################################
    
    # Your task is to complete dialogue_manager.py and use your 
    # advanced DialogueManager instead of SimpleDialogueManager. 
    
    # This is the point where you plug it into the Telegram bot. 
    # Do not forget to import all needed dependencies when you do so.
    
    dm = DialogueManager(RESOURCE_PATH)
    #bot = BotHandler(token, simple_manager)
    
    ###############################################################

    print("Ready to talk!")
    offset = 0
    while True:
        question = input('> ')
        answer = dm.generate_answer(question)
        print(answer)

if __name__ == "__main__":
    main()
