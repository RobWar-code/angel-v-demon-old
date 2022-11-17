"""
    Classes and Data for creating stories from templates
"""
import random


class TemplateHandler:

    """
        Add in the template_paragraphs dictionary
        and declare the token list
    """
    def __init__(self, template_paragraphs):
        self.template_paragraphs = template_paragraphs
        self.token_list = []

    def clear(self):
        self.token_list = []

    def get_num_paragraphs(self):
        return len(self.template_paragraphs)

    def get_sentence_texts(self, paragraph_num, sentence_num):
        # Get the angel's and demon's versions of the main sentence
        dual_text = self._get_angel_and_demon_text(paragraph_num, sentence_num)

    def _get_angel_and_demon_text(self, paragraph_num, sentence_num):
        angel_text = ""
        demon_text = ""
        sentence_data = self.template_paragraphs[paragraph_num][sentence_num]\
            ['main_sentence']
        template_text = sentence_data["template"]
        # Get number of words to choose
        num_opts = template_text.count("?")
        # For each alternative word option
        for alt in sentence_data["alternatives"]:
            demon_word = ""
            angel_word = ""
            # Check whether this is a token to be re-used
            if alt["acquired_id"] != "":
                demon_word = self._get_token(alt["acquired_id"], False)
                angel_word = self._get_token(alt["acquired_id"], True)
            else:
                word_choice = random.sample(alt["options"], 2)
                if alt["defined_id"] != "":
                    self._set_token(alt["defined_id"], word_choice)

    def _set_token(token_name, values):
        token_obj = [token_name, values[0], values[1]]
        self.token_list.push(token_obj)

    def _get_token(token_name, is_angel):
        for token in self.token_list:
            if token[0] == token_name:
                return token[1] if is_angel else token[2]
        # If token not found, then this is an error
        print(f"_get_token: token not found: {token_name}")
        raise systemExit()


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
