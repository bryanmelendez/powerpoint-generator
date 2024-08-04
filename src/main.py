from pptx import Presentation

class Slide(object):

    # make class attributes stuff like slide dimensions, font sizes, etc

    def __init__(self, title_text):
        self.title_text = title_text


class TitleSlide(Slide):
    def __init__(self, title_text, subtitle_text):
        self.subtitle_text = subtitle_text

        Slide.__init__(self, title_text)

    def CreateSlide(self):
        title_slide_layout = pres.slide_layouts[0]
        slide = pres.slides.add_slide(title_slide_layout)
        title = slide.shapes.title
        subtitle = slide.placeholders[1]
        title.text = self.title_text
        subtitle.text = self.subtitle_text

# Driver code
pres = Presentation()

slide = TitleSlide('Example title',
                   'Example subtitle')


slide.CreateSlide()

pres.save('test.pptx')
