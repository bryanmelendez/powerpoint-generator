# Classes for making pptx slides
from pptx import Presentation
from pptx.util import Inches


class Slide():
    SLD_LAYOUT_TITLE_SLIDE = 0
    SLD_LAYOUT_TITLE_AND_CONTENT = 1
    SLD_LAYOUT_PICTURE_WITH_CAPTION = 8

    PICTURE_PLACEHOLDER_IDX = 13

    def __init__(self, title_text):
        self.title_text = title_text


class TitleSlide(Slide):
    def __init__(self, title_text, subtitle_text):
        self.subtitle_text = subtitle_text
        super().__init__(title_text)

    def create_slide(self, pres):
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

    def create_slide(self, pres):
        image_slide_layout = pres.slide_layouts[self.SLD_LAYOUT_TITLE_AND_CONTENT]
        slide = pres.slides.add_slide(image_slide_layout)

        for shape in slide.placeholders:
            print('%d %s' % (shape.placeholder_format.idx, shape.name))

        quit()

        pic_placeholder = slide.placeholders[self.PICTURE_PLACEHOLDER_IDX]
        pic_placeholder.insert_picture(self.image_path)

        title_placeholder = slide.shapes.title
        title_placeholder.text = self.title_text

        # text_placeholder = slide.placeholders[2]
        # text_placeholder.text = ''
