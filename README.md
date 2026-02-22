# Discord Startup Notifier

lightweight program that sends a notif to a discord webhook whenever laptop/pc is opened. (lowk made this last time when my laptop was stolen)
did it in python instead of C++ is cause of simplicity 
some laptops may take longer to connect to the internet on startup so feel free to tweak the settings 

note: do NOT move or delete the dist folder after running the setup script or windows task schedular will no longer be able to find the executable

##  Features
. It runs immediately at startup, it will NOT be visible on taskmanager but it will be visible on task schedular to avoid the black cmd prompt that pops up

## how to install

1. **clone the repository:**
   ```cmd
   git clone https://github.com/urbancheese/Laptop-monitoring.git
   cd Laptop-monitoring
   ```

2. **add your webhook:**
   open `startup.py` and replace `YOUR_WEBHOOK_URL_HERE` on line 6 with your actual discord webhook url

3. **compile the executable:**
   you will need `pyinstaller` to compile the script into a standalone background executable
   ```cmd
   pip install pyinstaller
   pyinstaller --noconsole --onefile startup.py
   ```
   *this will create a `startup.exe` file inside your new `dist` folder*

4. **register the task:**
   run the included `setup_task.py` script as an **administrator** to register the executable with windows task schedular
   - open cmd as administrator
   - navigate to the project directory
   - run: `python setup_task.py`

## uninstallation
to remove the startup notification simply just open the windows **task scheduler** app, locate `DiscordLaptopStartupNotification` in the library right-click, and select **Delete**
