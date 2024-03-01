# Wiki 

This repository contains my solution for the Wiki assignment as part of CS50’s Web Programming with Python and JavaScript course. The assignment required implementing
a Wikipedia-like online encyclopedia with various features such as entry page rendering, search functionality, entry creation, editing, deletion and more.

## Features

- **Entry Page**: Visiting /wiki/TITLE renders a page displaying the contents of the encyclopedia entry with the given title. If the entry does not exist, an error page is displayed.
  
- **Index Page**: Updated index.html allows users to click on any entry name to be taken directly to that entry page.
  
- **Search**: Users can type a query into the search box to search for encyclopedia entries. Matching entries are displayed, and clicking on an entry name takes the user to that entry's page.
  
- **New Page**: Users can create a new encyclopedia entry by clicking "Create New Page" in the sidebar. They can enter a title and Markdown content, which is then saved to disk.
  
- **Edit Page**: Users can edit an entry's Markdown content by clicking a link on the entry page. The existing content is pre-populated in a textarea for editing, and changes can be saved.
  
- **Delete Page**: Users can delete an entry by clicking a link on the entry page. The entry is removed from the encyclopedia.
  
- **Random Page**: Clicking "Random Page" in the sidebar takes the user to a random encyclopedia entry.
  
- **Markdown to HTML Conversion**: Markdown content in entry files is converted to HTML using the python-markdown2 package before being displayed.

## Installation

To run this project locally, follow these steps:

1. Clone the repository: https://github.com/husseinalasadi/Wiki.git
2. Navigate to the project directory: cd Wiki
3. Install the required packages: pip install -r requirements.txt
4. Run the application: python manage.py runserver
5. Open a web browser and go to http://127.0.0.1:8000/ to view the application.

## Technologies Used

- Python
- Django
- HTML
- CSS
- JavaScript

## Credits

This project was completed as part of an assignment for CS50’s Web Programming with Python and JavaScript course offered by Harvard University.
I extend my gratitude to the CS50 staff for providing high-quality learning materials.
