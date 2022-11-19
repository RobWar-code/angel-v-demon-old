"""
    angel-v-demon
    A command-line game for one player, presenting a story to be memorised by
    the player, and re-presented line by line with modifications for the
    player to correct.
"""
import math
import platform
import os
import time
import story_template

# Globals
story = None
hi_score = 0


def main():
    global story

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
        max_differences_per_sentence = player_level
        # Set-up story object
        story = story_template.StoryHandler(
            story_template.template_paragraphs,
            num_paragraphs,
            max_differences_per_sentence,
            story_template.story_sentences)

        story.create_story()
        # Repeat game loop
        new_game = repeat_game_loop(num_paragraphs, player_level,
                                    expected_time_per_sentence,
                                    start_num_fairies)
        if not new_game:
            games_ended = True


def repeat_game_loop(num_paragraphs, player_level, expected_time_per_sentence,
                     start_num_fairies):
    global story
    game_repeat_finished = False
    while not game_repeat_finished:
        # Print the angel's story
        print()
        print("ANGEL'S STORY")
        print()
        story.print_angel_story()
        # Display Count Down Loop
        # Determine total display time
        time_limit = math.floor(
            expected_time_per_sentence * num_paragraphs * 3 / 2)
        display_timer(time_limit)
        # Clear the display
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

        # Do the demon's sentence display
        game_opts = sentence_loop(num_paragraphs, player_level,
                                  start_num_fairies,
                                  expected_time_per_sentence)
        if not game_opts["replay"]:
            game_repeat_finished = True

    return game_opts["new_game"]


def sentence_loop(num_paragraphs, player_level, start_num_fairies,
                  expected_time_per_sentence):
    global story, hi_score
    fairy_count = 0
    paragraph_count = 0
    got_sentence = True
    failed = False
    new_game = False
    replay = False
    # Set the time counter for scoring
    time_start = math.ceil(time.time())
    while not failed and got_sentence:
        # Print the next demon's sentence
        print("The Demon says:-")
        paragraph_end = story.print_demon_current_sentence()
        if paragraph_end:
            paragraph_count += 1
        # Get and check user corrections
        failed = word_loop()

        if (paragraph_end and not failed):
            # Print the consequence
            print("The angel cheers:- ")
            story.print_good_consequence()
            if paragraph_count >= num_paragraphs:
                got_sentence = False

    if failed:
        user_input = input("Enter Y to replay game else ENTER: ")
        if user_input == "Q" or user_input == "q":
            raise SystemExit()
        if user_input == "Y" or user_input == "y":
            replay = True
        else:
            user_input = input("Enter Y play a new game else ENTER: ")
            if user_input == "Q" or user_input == "q":
                raise SystemExit()
            if user_input == "Y" or user_input == "y":
                new_game = True

    else:
        print("The crowd cheers")
        # Calculate Score
        time_end = math.ceil(time.time())
        diff_time = time_end - time_start
        target = num_paragraphs * 3 * expected_time_per_sentence
        score = player_level * (200 + target - diff_time)
        score_string = "Your Score is: " + str(score)
        if hi_score > 0:
            score_string += " High Score was: " + str(hi_score)
        if score > hi_score:
            hi_score = score
        print()
        print(score_string)

        # Offer of new game
        print()
        user_input = input("Play another game Y or Q to quit: ")
        if user_input == "Y" or user_input == "y":
            new_game = True
        else:
            raise SystemExit()

    return {"new_game": new_game, "replay": replay}


def word_loop():
    try_again = True
    while try_again:
        # Get user replacement words
        failed = get_user_corrections()
        if (failed):
            print("WRONG - The demon chuckles..")
            if (fairy_count > 0):
                # The fairy intervenes
                if math.random() < 0.5:
                    print("A fairy gives you another chance")
                    story.print_demon_previous_sentence()
                else:
                    print("The fairy saves the knight's life")
                    try_again = False
                    failed = False
            else:
                story.print_ill_consequence()
                try_again = False

    return failed


def get_user_corrections():
    global story
    invalid = True
    failed = False
    while invalid:
        print()
        user_input = input("Enter corrections: ")
        if user_input == "Q" or user_input == "q":
            raise SystemExit()
        # Check the input against the angel's sentence
        result = story.test_angel_substitutes(user_input)
        if (result == "match"):
            invalid = false
        elif (result == "no match"):
            invalid = False
            failed = True
        else:
            print("Invalid corrections, use red=blue bear=angel etc")

    return failed


def display_timer(time_limit):
    """
        Display a numeric timer for time_limit seconds
    """
    print()
    print("Count Down: ", end="")
    display_time = str(time_limit).zfill(3)
    print(display_time, end="")
    while time_limit > 0:
        time.sleep(1)
        time_limit -= 1
        display_time = str(time_limit).zfill(3)
        print("\b\b\b" + display_time, end="", flush=True)
        time_limit -= 1
    print()


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
    print()
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
        print()
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


def enter_player_level():
    invalid = True
    while invalid:
        print()
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
