# Countdown Timer Application

The Countdown Timer is a simple desktop application built with Python and Tkinter. It allows users to set a countdown timer for 10 or 20 minutes, with options to reset or configure the time. Upon reaching zero, the application window flashes multiple colors, signaling the end of the countdown.

## Features

- Simple and intuitive user interface.
- Countdown set options for 10 and 20 minutes.
- Flashing window at the end of the countdown.
- Customizable countdown times.
- Always on top window option.

## Prerequisites

Before you can run or build the Countdown Timer application, you must install Python on your system. Python 3.6 or higher is recommended. You can download Python from [python.org](https://www.python.org/downloads/).

## Running the Application

To run the application directly from the source code:

1. Clone this repository or download the source code.
2. Navigate to the directory containing `countdown_app.py`.
3. Run the command: `python countdown_app.py`

## Building the Executable

To create an executable version of the Countdown Timer application for Windows:

1. Install PyInstaller: Run `pip install pyinstaller` in your command line or terminal.
2. Navigate to the directory containing your `countdown_app.py` file.
3. Run the following command to create the executable:

    ```shell
    pyinstaller --onefile --windowed --icon=app_icon.ico countdown_app.py
    ```

    - `--onefile` packages everything into a single executable.
    - `--windowed` prevents a command prompt window from appearing alongside your GUI application (optional).
    - `--icon` specifies the path to your application's icon file (optional).

4. After the build process completes, find your `.exe` file in the `dist` directory.

## Customizing Countdown Times

The application allows custom countdown times via the configuration menu, accessible from the main window. Default times are 10 and 20 minutes, but these can be adjusted to user preference.

## Contributing

Contributions to the Countdown Timer application are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is open source and available under the [MIT License](LICENSE.md).
 
