### Design
- Option Title Page
- As built (optional)
- Option Plan view
  - Suggested layout option. Not for construction use.
- Option pages (variable amount)

### Tools
- Python
- Tkinter 
- python-pptx

### Resources
- https://stackoverflow.com/questions/2933/create-a-directly-executable-cross-platform-gui-app-using-python
- https://python-pptx.readthedocs.io/en/latest/


### Pseudocode
- create the presentation
- search for image files within image directory
  - create tuples with the image path
  - parse the file name to obtain page title
  - keep searching for images until one is not found
- Loop:
  - each loop corresponds with an option
  - create a page
  - add title from tuple
  - add image from file path

