import slides
import powerpoint_generator as pg


# params from gui:
# client name
# file path
# save name

# For testing:
ex_name = 'Bryan'
IMAGE_DIR = '/home/bryan/Documents/documents/pptx_examples/Example Exports/'
save_name = 'test'


def main():
    # powerpoint
    pp = pg.PowerpointGenerator(ex_name, IMAGE_DIR)
    pres = slides.Presentation()

    # Storing all of the slides in a list
    slides_list = []

    # generate the list of slides
    pp.generate_slide_list(slides_list)

    # add slides to presentation
    pp.generate_presentation(slides_list, pres)

    pres.save('{}.pptx'.format(save_name))


if __name__ == "__main__":
    main()
