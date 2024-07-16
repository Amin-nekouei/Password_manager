# Password Manager

Welcome to the Password Manager project! This application allows users to securely generate, store, and retrieve passwords using a graphical user interface built with Python's Tkinter library.

## Features

- **Password Generation**: Easily create strong, customizable passwords.
- **Password Storage**: Save passwords securely in a JSON file.
- **Password Retrieval**: Quickly find and view stored passwords for specific websites.
- **Clipboard Support**: Automatically copy generated passwords to the clipboard for convenience.

## Project Structure

The project is organized into the following files:

- **`main.py`**: The main script that sets up and runs the Tkinter-based GUI.
- **`password_generator.py`**: Defines the `PasswordGenerator` class used for generating passwords.
- **`password_manager.py`**: Contains functions and logic for interacting with the JSON file for saving and retrieving passwords.


    ```

## Usage


2. **Generate a Password**:
    - Click on the **Generate Password** button.
    - Input the desired number of letters, symbols, and digits.
    - The generated password will appear in the password entry field and be copied to your clipboard.

3. **Save a Password**:
    - Fill in the fields for the website name, username, and the generated password.
    - Click the **Add** button to save this information.

4. **Search for a Password**:
    - Enter the website name in the search field.
    - Click the **Search** button to retrieve and display the stored username and password.


