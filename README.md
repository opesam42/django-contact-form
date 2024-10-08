# Django Form Handling Project

## Introduction
This project is a Django-based web application designed to handle user queries through a form. It features a user-friendly interface for submitting queries, including fields for the user's name, email, query method, and message. The application also incorporates form validation, custom error messages, and a confirmation page that displays the submitted data.

## Key Features
- **Form Handling:** A structured form that allows users to submit queries through a straightforward interface.
- **Validation:** Both server-side and client-side validations are implemented to ensure that the form data is accurate and complete before submission.
- **Custom Error Messages:** Clear and customized error messages provide users with specific feedback when the form is not filled out correctly.
- **Success Page:** After successful form submission, users are redirected to a confirmation page.
- **Responsive Design:** The form is fully responsive, providing a seamless experience across various devices, including desktops, tablets, and mobile phones.

## Screenshots
Here are some screenshots of the application in action:

- **Form Page:**
  ![Form Page](./assets/form-page.png)
  *The initial page where users enter their queries.*

- **Success Page:**
  ![Success Page](./assets/success-page.png)
  *The confirmation page displayed after successful form submission.*

- **Error State:**
  ![Error State](./assets/error-state.png)
  *Example of an error state showing validation feedback to users.*

## Challenges Faced
- **Form Validation:** Ensuring that all fields were correctly validated and that custom error messages were displayed appropriately.
- **Radio Buttons Handling:** Managing radio buttons, especially hiding the default blank option, required careful CSS manipulation to maintain a clean UI.
- **Git and GitHub Integration:** Learning to use Git for version control and successfully pushing the project to GitHub with a repository name different from the Django directory name.
- **Connecting to an External MySQL Database**: Django's default database backend is SQLite, which is suitable for development but not recommended for production. To use MySQL, which provides better performance and scalability for production environments, the Django project needed to be configured to work with MySQL, so I utilized PyMySQL.
- **Deploying and Fixing Configuration Bugs:** When deploying the application, discrepancies between local development and production environments caused bugs and unexpected behavior.

## Learning Outcomes
- **Django Form Handling:** Gained a deep understanding of Django’s form processing, validation, and data management.
- **Responsive Web Design:** Developed skills in creating responsive forms that adapt to various screen sizes using CSS media queries..
- **Version Control:** Enhanced proficiency with Git, including managing branches, commits, and remote repositories on GitHub.
- **Database Integration:** Configuring Django to work with MySQL instead of the default SQLite taught me about the nuances of database backends and the importance of selecting the right database for production.
- **Deployment Challenges:** Deploying a Django application on Vercel highlighted the complexities of handling static files and adapting to platforms designed primarily for static sites.
- **External Resources:** Integrating external resources like stylesheets from GitHub improved my understanding of how to leverage third-party assets and manage browser caching.
- **Environment Configuration:** Learned the importance of aligning local and production configurations. Managed environment-specific settings and resolved issues arising from differences between development and production environments.
- **Debugging and Troubleshooting:** Enhanced skills in debugging deployment issues and configuring applications for different environments, which are crucial for maintaining and scaling web applications.

## How to Run the Project Locally

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/opesam42/django-contact-form.git
    cd django-contact-form
    ```

2. **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Database Settings:**
   Update the DATABASES setting in settings.py with your MySQL database credentials.

5. **Run Migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Start the Development Server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the Application:** Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Deployment
- https://django-contact-form-three.vercel.app/
## Author
- Website - [Gbenga Opeyemi](https://github.com/opesam42)
- Frontend Mentor - [@opesam42](https://www.frontendmentor.io/profile/opesam42)
- Twitter - [@gbengaope04](https://www.twitter.com/@gbengaope04)
- LinkedIn - [Opeyemi Oluwagbemiga](www.linkedin.com/in/opeyemi-oluwagbemiga-2ba61423b)

## Conclusion
This project was a valuable learning experience, providing insights into Django's form handling, responsive design, and deployment. The challenges encountered helped solidify understanding and enhanced skills in these areas. The successful completion of this project lays a strong foundation for future web development endeavors.
