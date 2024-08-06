import os
import slides


def main():
    pres = slides.Presentation()

    # Example code

    slides_list = []
    new_slide = slides.TitleSlide('<Name> Remodel Option <number>'.upper(),
                                  'layout concept design by cara mia designs'.upper())
    slides_list.append(new_slide)

    # image_slide = slides.ImageSlide('Image slide title',
    #                                 '{}Example Exports/Option 1 A.jpg'.format(slides.EXAMPLE_IMAGES))
    # image_slide.CreateSlide(pres)

    # Number in file name
    option_num = 1
    # Letter in file name
    pic_letter = 'A'

    current_option_pics = True

    while current_option_pics:
        # Create title
        title = 'Option {} {}'.format(option_num, pic_letter)

        # Generate image path
        image_path = '{}Example Exports/Option {} {}.jpg'.format(
                                                    slides.EXAMPLE_IMAGES,
                                                    option_num,
                                                    pic_letter)

        print(image_path)

        # Check if path exits
        if os.path.exists(image_path):
            print("File exists")
            new_slide = slides.ImageSlide(title, image_path)
            slides_list.append(new_slide)
        else:
            print("Path does not exist. Breaking loop.")
            current_option_pics = False

        pic_letter = chr(ord(pic_letter) + 1)
        if pic_letter > 'Z':
            break

    for slide in slides_list:
        slide.CreateSlide(pres)
        print("Creating slide titled: {}".format(slide.title_text))

    pres.save('test.pptx')


if __name__ == "__main__":
    main()
