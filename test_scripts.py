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
