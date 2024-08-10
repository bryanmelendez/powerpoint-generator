import slides
import powerpoint_generator as pg
import gui
import status_gui
import os


def main():
    # user interface
    app = gui.GUI()
    app.start_gui()

    client_name = app.get_client_name()
    image_directory = '{}/'.format(app.get_directory_path())
    print(image_directory)
    template = 'assets/template.pptx'
    print(template)
    save_name = app.get_file_name()

    # powerpoint
    pp = pg.PowerpointGenerator(client_name, image_directory)
    pres = slides.Presentation(template)

    # Storing all of the slides in a list
    slides_list = []

    # generate the list of slides
    pp.generate_slide_list(slides_list)

    # add slides to presentation
    pp.generate_presentation(slides_list, pres)

    # If slides are successful, save the file
    if len(slides_list):
        save_path = os.path.join(image_directory, save_name)
        status_message = "Successful generation! Saving powerpoint at:\n {}".format(save_path)
        print(status_message)
        pres.save('{}.pptx'.format(save_path))
    else:
        status_message = "No slides in list. Aborting program"
        print(status_message)
        # pop up error window

    status_gui.StatusGui(status_message)


if __name__ == "__main__":
    main()
