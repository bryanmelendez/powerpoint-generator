# Classes for making pptx slides
from pptx import Presentation
from pptx.util import Inches
from PIL import Image


class Slide():
    SLD_LAYOUT_TITLE_SLIDE = 0
    SLD_LAYOUT_TITLE_AND_CONTENT = 1
    SLD_LAYOUT_PICTURE_WITH_CAPTION = 8

    PICTURE_PLACEHOLDER_IDX = 13
    TEXT_PLACEHOLDER_IDX = 14

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
    def __init__(self, title_text, footer_text, image_path):
        self.image_path = image_path
        self.footer_text = footer_text
        super().__init__(title_text)

    def create_slide(self, pres):
        image_slide_layout = pres.slide_layouts[self.SLD_LAYOUT_TITLE_AND_CONTENT]
        slide = pres.slides.add_slide(image_slide_layout)

        # Debug template

        # for shape in slide.placeholders:
        #     print('%d %s' % (shape.placeholder_format.idx, shape.name))

        # quit()

        pic_placeholder = slide.placeholders[self.PICTURE_PLACEHOLDER_IDX]

        img = Image.open(self.image_path)
        img_width, img_height = img.size

        placeholder_width = pic_placeholder.width
        placeholder_height = pic_placeholder.height

        width_scale = placeholder_width / img_width
        height_scale = placeholder_height / img_height
        scaling_factor = min(width_scale, height_scale)

        new_width = int(img_width * scaling_factor)
        new_height = int(img_height * scaling_factor)

        # Get placeholder position
        ph_left = pic_placeholder.left
        ph_top = pic_placeholder.top

        # Adjust the position of the image so it's centered within the placeholder
        img_left = ph_left + (placeholder_width - new_width) // 2
        img_top = ph_top + (placeholder_height - new_height) // 2

        # Insert and resize the image
        slide.shapes.add_picture(self.image_path, img_left, img_top, 
                                 width=new_width, height=new_height)

        title_placeholder = slide.shapes.title
        title_placeholder.text = self.title_text

        text_placeholder = slide.placeholders[self.TEXT_PLACEHOLDER_IDX]
        text_placeholder.text = self.footer_text
