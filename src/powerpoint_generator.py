import slides
import os
from pptx import Presentation
from pptx.util import Inches


class PowerpointGenerator:
    def __init__(self, client_name, image_directory):
        self.client_name = client_name
        self.image_directory = image_directory

    def generate_slide_list(self, slides_list):
        # Number in file name
        option_num = 1
        # Letter in file name
        pic_letter = 'A'

        options_left = True

        # Looping until there are no more options left
        while options_left:
            current_option_pics = True

            # Create title
            title = 'Option {} A'.format(option_num)
            initial_check = '{}.jpg'.format(os.path.join(self.image_directory, title))

            print("Checking: {}".format(initial_check))
            if not os.path.exists(initial_check):
                print("No more slides to be made")
                options_left = False
                current_option_pics = False
                break

            # Create a title page for each option iteration
            new_slide = slides.TitleSlide(
                '{} Remodel\nOption {}'.format(self.client_name, option_num).upper(),
                'layout concept design by cara mia designs'.upper())

            slides_list.append(new_slide)

            new_plan_view_title = 'Option {} plan view'.format(option_num)
            # if plan view exists put it here
            new_slide = slides.ImageSlide(
                new_plan_view_title.upper(),
                '{}.jpg'.format(os.path.join(self.image_directory, new_plan_view_title)))

            slides_list.append(new_slide)

            # Looping until there are no more pictures for each option
            while current_option_pics:
                # Update title
                title = 'Option {} {}'.format(option_num, pic_letter)

                image_path = '{}.jpg'.format(os.path.join(self.image_directory, title))
                print(image_path)

                # Check if path exists
                if os.path.exists(image_path):
                    print("File exists")
                    new_slide = slides.ImageSlide(title, image_path)
                    slides_list.append(new_slide)
                else:
                    print("Path does not exist. Breaking loop.")
                    current_option_pics = False

                # increment the character
                pic_letter = chr(ord(pic_letter) + 1)
                if pic_letter > 'Z':
                    break

            option_num += 1

            pic_letter = 'A'

    # Generates a pptx slide for each object in slides_list
    def generate_presentation(self, slides_list, pres):
        pres.slide_width = slides.Slide.slide_width
        pres.slide_height = slides.Slide.slide_height

        for slide in slides_list:
            slide.create_slide(pres)
            print("Creating slide titled: {}".format(slide.title_text))
