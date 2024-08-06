import os
import slides


def main():
    # For testing:
    ex_name = 'Bryan'

    pres = slides.Presentation()

    # Storing all of the slides in a list
    slides_list = []

    # Number in file name
    option_num = 1
    # Letter in file name
    pic_letter = 'A'

    options_left = True

    while options_left:
        current_option_pics = True

        # Create a title page for each option iteration
        new_slide = slides.TitleSlide('{} Remodel Option {}'.format(ex_name, option_num).upper(),
                                      'layout concept design by cara mia designs'.upper())
        slides_list.append(new_slide)

        while current_option_pics:
            # Create title
            title = 'Option {} {}'.format(option_num, pic_letter)

            # Generate image path
            image_path = '{}Example Exports/Option {} {}.jpg'.format(
                slides.EXAMPLE_IMAGES,
                option_num,
                pic_letter)

            print(image_path)

            if pic_letter == 'A' and not os.path.exists(image_path):
                print("No more slides to be made")
                options_left = False
                current_option_pics = False
                break

            # Check if path exits
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

    for slide in slides_list:
        slide.CreateSlide(pres)
        print("Creating slide titled: {}".format(slide.title_text))

    pres.save('test.pptx')


if __name__ == "__main__":
    main()
