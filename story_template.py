"""
    Classes and Data for creating stories from templates
"""
import random


class TemplateHandler:

    """
        Add in the template_paragraphs dictionary
        and declare the token list
    """
    def __init__(self, template_paragraphs, max_differences_per_sentence):
        self.template_paragraphs = template_paragraphs
        self.token_list = []
        self.max_differences_per_sentence = max_differences_per_sentence

    def clear(self):
        self.token_list = []

    def get_num_paragraphs(self):
        return len(self.template_paragraphs)

    """
        Collect the angel and demon versions of a sentence as well as
        the good and ill consequence sentences
    """
    def get_sentence_texts(self, paragraph_num, sentence_num):
        # Get the angel's and demon's versions of the main sentence
        dual_text = self._get_angel_and_demon_text(paragraph_num, sentence_num)
        sentence_data = self.template_paragraphs[paragraph_num][sentence_num]
        ill_consequence = ""
        if (sentence_data["ill_consequence"]):
            ill_consequence = self._get_single_sentence_text(
                sentence_data["ill_consequence"], False)
        good_consequence = ""
        if (sentence_data["good_consequence"]):
            good_consequence = self._get_single_sentence_text(
                sentence_data["good_consequence"], True)
            # This is the final sentence of the paragraph, so clear tokens
            self.clear()

        return {
            "angel_text": dual_text[0],
            "demon_text": dual_text[1],
            "ill_consequence": ill_consequence,
            "good_consequence": good_consequence
        }

    """
        Perform the word substitutions for either the demon or the angel
    """
    def _get_single_sentence_text(self, sentence_data, is_angel):
        out_text = sentence_data["template"]
        alternatives = sentence_data["alternatives"]
        # Perform each substitution
        for alt in alternatives:
            word = ""
            # Check whether a token
            if alt["acquired_id"]:
                word = self._get_token(alt["acquired_id"], is_angel)
            else:
                word = random.choice(alt["options"])
            # Insert the word
            out_text = out_text.replace("?", word, 1)

        return out_text

    """
        Perform the word substitutions for both angel and demon to
        produce two sentences
    """
    def _get_angel_and_demon_text(self, paragraph_num, sentence_num):
        angel_text = ""
        demon_text = ""
        sentence_data = self.template_paragraphs[paragraph_num][sentence_num]\
            ['main_sentence']
        demon_text = sentence_data["template"]
        angel_text = sentence_data["template"]
        # Get set of word numbers in which the demon's choice is to be
        # different
        word_diff_list = []
        word_diff_list = self._get_word_diff_list(sentence_data["template"])
        print(word_diff_list)
        # For each alternative word option
        count = 0
        diff_count = 0
        for alt in sentence_data["alternatives"]:
            demon_word = ""
            angel_word = ""
            # Check whether this is a token to be re-used
            if alt["acquired_id"] != "":
                demon_word = self._get_token(alt["acquired_id"], False)
                angel_word = self._get_token(alt["acquired_id"], True)
            else:
                # Select the words from the list of alternatives
                word_choice = random.sample(alt["options"], 2)
                if alt["definitive_id"] != "":
                    self._set_token(alt["definitive_id"], word_choice)
                angel_word = word_choice[0]
                demon_word = word_choice[1]

            # Assign the words to the relevant sentences
            angel_text = angel_text.replace("?", angel_word, 1)
            # Check whether the demon's choice is different
            if diff_count < len(word_diff_list):
                if count == word_diff_list[diff_count]:
                    demon_text = demon_text.replace("?", demon_word, 1)
                    diff_count += 1
                else:
                    demon_text = demon_text.replace("?", angel_word, 1)
            else:
                demon_text = demon_text.replace("?", angel_word, 1)

            count += 1

        return [angel_text, demon_text]

    """
        Insert a token into the token list. This contains both the
        angel's and the demon's values
    """
    def _set_token(self, token_name, values):
        token_obj = [token_name, values[0], values[1]]
        self.token_list.append(token_obj)

    """
        Search and get the token (angel or demon value) from the token
        list
    """
    def _get_token(self, token_name, is_angel):
        for token in self.token_list:
            if token[0] == token_name:
                return token[1] if is_angel else token[2]
        # If token not found, then this is an error
        print(f"_get_token: token not found: {token_name}")
        raise SystemExit()

    """
        Get list of template word replacement numbers that are
        to be differenct between angel and demon
    """
    def _get_word_diff_list(self, template_text):
        num_substitutes = template_text.count("?")
        num_list = list(range(num_substitutes))
        # Select the word numbers to change
        if num_substitutes <= self.max_differences_per_sentence:
            return num_list

        # Otherwise, choose a subset and order it
        num_list = random.sample(num_list,
                                 self.max_differences_per_sentence)
        num_list.sort()
        return num_list


# --------------------------------------------------------------------
# Template Data
template_paragraphs = [
    [
        {
            "main_sentence": {
                "template": "The knight ? ?.",
                "alternatives": [
                    {
                        "definitive_id": "",
                        "acquired_id": "",
                        "options": ["walked", "ran", "trotted", "hurried"]
                    },
                    {
                        "definitive_id": "",
                        "acquired_id": "",
                        "options": ["left", "right", "forwards"]
                    }
                ]
            },
            "ill_consequence": {
                "template": "The knight ? to his ?",
                "alternatives": [
                    {
                        "definitive_id": "",
                        "acquired_id": "",
                        "options": ["plunged", "fell", "stumbled", "staggered"]
                    },
                    {
                        "definitive_id": "",
                        "acquired_id": "",
                        "options": ["doom", "fate", "death"]
                    }
                ]
            },
            "good_consequence": {}
        },
        {
            "main_sentence": {
                "template": "In the room was a ? ?.",
                "alternatives": [
                    {
                        "definitive_id": "",
                        "acquired_id": "",
                        "options": ["green", "black", "white", "red"]
                    },
                    {
                        "definitive_id": "monster",
                        "acquired_id": "",
                        "options": ["dragon", "bear", "sphinx", "leopard"]
                    }
                ]
            },
            "ill_consequence": {
                "template": "The knight was suprised by a ? as it ? him down.",
                "alternatives": [
                    {
                        "definitive_id": "",
                        "acquired_id": "monster",
                        "options": []
                    },
                    {
                        "definitive_id": "",
                        "acquired_id": "",
                        "options": ["struck", "knocked"]
                    }
                ]
            },
            "good_consequence": {}
        },
        {
            "main_sentence": {
                "template": "The knight ? the ? with his ? ?.",
                "alternatives": [
                    {
                        "definitive_id": "",
                        "acquired_id": "",
                        "options": ["struck", "hit", "swiped"]
                    },
                    {
                        "definitive_id": "",
                        "acquired_id": "monster",
                        "options": []
                    },
                    {
                        "definitive_id": "",
                        "acquired_id": "",
                        "options": ["silver", "bronze", "iron"]
                    },
                    {
                        "definitive_id": "",
                        "acquired_id": "",
                        "options": ["sword", "club", "dagger"]
                    }
                ]
            },
            "ill_consequence": {
                "template": "The ? ? the knight and ? him",
                "alternatives": [
                    {
                        "definitive_id": "",
                        "acquired_id": "monster",
                        "options": []
                    },
                    {
                        "definitive_id": "",
                        "acquired_id": "",
                        "options": ["bit", "swiped", "struck"]
                    },
                    {
                        "definitive_id": "",
                        "acquired_id": "",
                        "options": ["killed", "wasted", "destroyed"]
                    }
                ]
            },
            "good_consequence": {
                "template": "The ? ? dead.",
                "alternatives": [
                    {
                        "definitive_id": "",
                        "acquired_id": "monster",
                        "options": []
                    },
                    {
                        "definitive_id": "",
                        "acquired_id": "",
                        "options": ["dropped", "fell", "collapsed"]
                    }
                ]
            }
        },
    ]
]

# class StoryHandler(TemplateHandler, max_differences_per_sentence):
