"""
    angel-v-demon
    A command-line game for one player, presenting a story to be memorised by
    the player, and re-presented line by line with modifications for the
    player to correct.
"""
import os
import time
import story_template

# Globals
story = None


def main():
    global story
    hi_score = 0

    # Introduce the game
    display_introduction()
    games_ended = False
    while not games_ended:
        display_instructions()
        # Get number of paragraphs
        num_paragraphs = enter_num_paras()
        # Get player level
        player_level = enter_player_level()
        # Determine play parameters
        start_num_fairies = (4 - player_level) * num_paragraphs
        player_read_time = 12 * num_paragraphs / player_level
        expected_time_per_sentence = 20 / player_level
        # Set-up story object
        story = story_template.StoryHandler(
            story_template.template_paragraphs,
            num_paragraphs,
            max_differences_per_sentence,
            story_template.story_sentences)

        story.create_story()
        # Repeat game loop
        repeat_game_loop(num_paragraphs, expected_time_per_sentence)
        # debug
        games_ended = True


def repeat_game_loop(num_paragraphs, expected_time_per_sentence):
    global story
    game_repeat_finished = False
    while not game_repeat_finished:
        # Print the angel's story
        print()
        print("ANGEL'S STORY")
        print()
        story.print()
        # Display Count Down Loop
        # Determine total display time
        time_limit = Math.floor(
            expected_time_per_sentence * num_paragraphs * 3 / 2)
        display_time = str(time_limit).zfill(3)
        print(display_time, end="")
        while time_limit > 0:
            time.sleep(1)
            time_limit -= 1
            display_time = str(time_limit).zfill(3)
            print("\b\b\b" + display_time, end="")


def display_introduction():
    print("Welcome to Angel v Demon!")
    print()
    print("""In this game, you are presented with a story written for a
bold knight by an angel. However, before the knight can receive his fate,
a demon seizes the copy and modifies some words on each line. Your mission is
to restore it to its original form line by line and save the knight ...""")
    print()
    user_input = input("Click ENTER key to continue - Q to quit: ")
    if user_input == "Q" or user_input == "q":
        raise SystemExit()


def display_instructions():
    print("INSTRUCTIONS")
    print()
    print("""At the start of the game you will be presented with the angel's
version of the story. You will have a certain amount of time to
read and memorise it.""")
    print()
    print("""After this you will be presented with the demon's version of
the sentences in order, one at a time and will be prompted to enter
the corrections with each.""")
    print()
    print("""On a single input line, for each correction that you recall, type
in the word to be replaced, followed by an equals sign, followed by the word
to replace it. For Example:""")
    print("red=blue bear=dragon")
    print()
    print("You can leave the games any time by entering Q")
    user_input = input("ENTER to continue, Q to quit: ")
    if user_input == "Q" or user_input == "q":
        raise SystemExit()


def enter_num_paras():
    invalid = True
    while invalid:
        user_input = input("""Please enter number of paragraphs for \
the story (1 to 5): """)
        if user_input == "Q" or user_input == "q":
            raise SystemExit()
        if len(user_input) != 1:
            print("Value entered was not valid")
        elif user_input not in "12345":
            print("Number not valid")
        else:
            n = int(user_input)
            invalid = False
    return n


def enter_num_paras():
    invalid = True
    while invalid:
        user_input = input("""Please enter player level\
 (1 to 4, 1 easiest): """)
        if user_input == "Q" or user_input == "q":
            raise SystemExit()
        if len(user_input) != 1:
            print("Value entered was not valid")
        elif user_input not in "1234":
            print("Number not valid")
        else:
            n = int(user_input)
            invalid = False
    return n


main()
