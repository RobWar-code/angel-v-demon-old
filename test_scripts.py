import story_template

# Test Template
max_differences_per_sentence = 1
template = story_template.TemplateHandler(story_template.template_paragraphs,
                                          max_differences_per_sentence)
for i in range(3):
    template.get_sentence_texts(0, i)

# Test Story
num_paragraphs = 2
max_differences_per_sentence = 2
story = story_template.StoryHandler(story_template.template_paragraphs,
                                    num_paragraphs,
                                    max_differences_per_sentence,
                                    story_template.story_sentences)
story.create_story()
story.print_angel_story()
print("----------------------")
for i in range(5):
    story.print_demon_current_sentence()
    subs = input("Input Subs:")
    print(story.test_angel_substitutes(subs))

print("----------------------")
story.print_demon_previous_sentence()
print("----------------------")
print(story.test_angel_substitutes("red=blue  green=black   cat-leopard"))
print(story.test_angel_substitutes("(abc=lmnop"))
print(story.test_angel_substitutes("xabc=lmnop"))
