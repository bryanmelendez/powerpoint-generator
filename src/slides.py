# Classes for making pptx slides

from pptx import Presentation
from pptx.util import Inches

EXAMPLE_IMAGES = '/home/bryan/Documents/documents/pptx_examples/'


class Slide():
    SLD_LAYOUT_TITLE_SLIDE = 0
    SLD_LAYOUT_TITLE_AND_CONTENT = 1
    SLD_LAYOUT_PICTURE_WITH_CAPTION = 8

    # make class attributes stuff like slide dimensions, font sizes, etc

    def __init__(self, title_text):
        self.title_text = title_text


class TitleSlide(Slide):
    def __init__(self, title_text, subtitle_text):
        self.subtitle_text = subtitle_text
        super().__init__(title_text)

    def CreateSlide(self, pres):
        title_slide_layout = pres.slide_layouts[self.SLD_LAYOUT_TITLE_SLIDE]
        slide = pres.slides.add_slide(title_slide_layout)
        title = slide.shapes.title
        subtitle = slide.placeholders[1]
        title.text = self.title_text
        subtitle.text = self.subtitle_text


class ImageSlide(Slide):
    def __init__(self, title_text, image_path):
        self.image_path = image_path
        super().__init__(title_text)

    def CreateSlide(self, pres):
        image_slide_layout = pres.slide_layouts[self.SLD_LAYOUT_PICTURE_WITH_CAPTION]
        slide = pres.slides.add_slide(image_slide_layout)
        pic_placeholder = slide.placeholders[1]
        # check if i even need to store picture in a var
        picture = pic_placeholder.insert_picture(self.image_path)

        title_placeholder = slide.shapes.title
        title_placeholder.text = self.title_text

        text_placeholder = slide.placeholders[2]
        text_placeholder.text = ''
