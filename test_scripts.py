import story_template

max_differences_per_sentence = 1
template = story_template.TemplateHandler(story_template.template_paragraphs,
                                          max_differences_per_sentence)

for i in range(3):
    template.get_sentence_texts(0, i)
