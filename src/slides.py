# Classes for making pptx slides
from pptx import Presentation
from pptx.util import Inches


class Slide():
    SLD_LAYOUT_TITLE_SLIDE = 0
    SLD_LAYOUT_TITLE_AND_CONTENT = 1
    SLD_LAYOUT_PICTURE_WITH_CAPTION = 8

    slide_width = Inches(11)
    slide_height = Inches(8.5)

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
        image_slide_layout = pres.slide_layouts[self.SLD_LAYOUT_PICTURE_WITH_CAPTION]
        slide = pres.slides.add_slide(image_slide_layout)

        # self.format_slide(slide)

        pic_placeholder = slide.placeholders[1]
        pic_placeholder.insert_picture(self.image_path)

        title_placeholder = slide.shapes.title
        title_placeholder.text = self.title_text

        text_placeholder = slide.placeholders[2]
        text_placeholder.text = ''

    def format_slide(self, slide):
        # Access and customize the title placeholder
        title_placeholder = slide.shapes.title
        title_placeholder.text = "Custom Centered Title"
        title_placeholder.left = Inches(1)
        title_placeholder.top = Inches(0.5)
        title_placeholder.width = Slide.slide_width - Inches(2)
        title_placeholder.height = Inches(1)

        # Access and customize the content placeholder
        content_placeholder = slide.placeholders[1]
        content_placeholder.text = "This content is centered using a predefined layout."
        content_placeholder.left = Inches(1)
        content_placeholder.top = Inches(2)
        content_placeholder.width = Slide.slide_width - Inches(2)
        content_placeholder.height = Slide.slide_height - Inches(3)
