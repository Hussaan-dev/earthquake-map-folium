# My First Interactive Earthquake Map

## About This Project

Welcome to my very first Python project on GitHub! I built this interactive web map to visualize earthquake data from around the world. It was a really fun way to learn about using Python for mapping, and I'm excited to share it with you.

This map uses Python's `pandas` library to read earthquake data and `folium` to turn that data into a beautiful, clickable map that you can open right in your web browser.

## Features You'll See

* **Earthquakes by Strength:** Each earthquake marker changes color based on how strong it was (its magnitude):
    * `< 3.0`: Green (smaller quakes)
    * `< 5.0`: Orange
    * `< 6.0`: Red
    * `< 7.0`: Dark Red
    * `>= 7.0`: Black (the strongest ones!)
* **Click for Details:** Click on any earthquake marker to see a little popup with more info: its magnitude, where it happened, and when.
* **Tectonic Plate Overlay:** I've also added the major lines where Earth's tectonic plates meet – you'll notice many earthquakes happen along these lines!
* **Clean Map View:** If there are lots of earthquakes close together, the map groups them into "clusters" so it doesn't look too messy. Just zoom in to see individual quakes!
* **Toggle Layers:** There's a small control panel on the map where you can easily turn the earthquake markers or the tectonic plates on/off.

## See It in Action! (Screenshots)

Here are some glimpses of what the map looks like:

### Global View
[![Map Overview](images/Screenshot%202025-06-21%20113439.png)](images/Screenshot%202025-06-21%20113439.png)
*A look at the whole map, showing where earthquakes are spread out.*

### Closer Look at a Region
[![Zoomed-in Area](images/Screenshot%202025-06-21%20113624.png)](images/Screenshot%202025-06-21%20113624.png)
*Zoomed in to see more detail, with earthquake dots and plate lines.*

### Grouped Earthquakes (Clusters)
[![Marker Cluster Example](images/Screenshot%202025-06-21%20113717.png)](images/Screenshot%202025-06-21%20113717.png)
*This shows how lots of earthquakes close by get neatly grouped into one big circle.*

### Earthquake Details Popup
[![Popup Detail](images/Screenshot%202025-06-21%20113741.png)](images/Screenshot%202025-06-21%20113741.png)
*What you see when you click on an earthquake dot – its magnitude, where it was, and the time.*

*(**Pro Tip:** Clicking on any of these images will open them in full-size!)*

---

## How to Get Started (Easy Steps!)

Want to run this map on your own computer? It's pretty straightforward!

### 1. What You Need (Prerequisites)

Make sure you have Python installed. If you do, you just need two extra tools.

* **Open your command prompt or terminal.** (On Windows, search for "cmd"; on Mac/Linux, look for "Terminal").
* **Type this command and press Enter:**
    ```bash
    pip install pandas folium
    ```
    This will install the `pandas` and `folium` libraries your script uses.

### 2. Grab the Project Files

Make sure you have all the necessary files in one folder on your computer:

* `EarthquakeAndPlates.py` (This is the main Python script)
* `earthquakes.csv` (This is the raw data file for the earthquakes)
* `plates.json` (This file contains the data for the tectonic plates)
* **A folder named `images`** (inside your main project folder) that contains your four screenshots:
    * `Screenshot 2025-06-21 113439.png`
    * `Screenshot 2025-06-21 113624.png`
    * `Screenshot 2025-06-21 113717.png`
    * `Screenshot 2025-06-21 113741.png`

### 3. Run the Map!

Now for the fun part – creating the map.

1.  **Go to your project folder in the command prompt/terminal.**
    Type `cd` followed by the full path to your folder, then press Enter.
    * Example: `cd C:\Users\YourName\Desktop\MyEarthquakeMap`
2.  **Run the Python script.** Once you're in the right folder, type this and press Enter:
    ```bash
    python EarthquakeAndPlates.py
    ```
    The script will do its magic.

### 4. See Your Map in Action!

1.  **Look in your project folder.** After the script runs, you'll find a new file there called `earthquake.html`.
2.  **Open this HTML file in your web browser.** Just double-click `earthquake.html`, and your interactive earthquake map will pop right up!

---

## Data Sources

* `earthquakes.csv`: The earthquake data.
* `plates.json`: The data for the Earth's tectonic plates.

---

## License

This project is open-source, which means you can use and modify it! It's available under the [MIT License](https://opensource.org/licenses/MIT).

---

## Connect with Me!

* **Hussaan-dev** - [https://github.com/Hussaan-dev](https://github.com/Hussaan-dev)

---

**The absolute final and most important step to make the images appear on GitHub is this (if you haven't done it already):**

You **must upload the actual `.png` screenshot files** (`Screenshot 2025-06-21 113439.png`, etc.) into a folder named **`images`** on your GitHub repository, **using the GitHub website**.

Here are the simplified steps for that:

1.  **Go to your GitHub repository's main page** in your web browser.
2.  **Click on the `images` folder** if it already exists in your file list. If you *don't* see an `images` folder:
    * Click the **"Add file"** button.
    * Select **"Create new file"**.
    * In the "Name your file..." box, type: `images/dummy.txt` (this is just to create the folder).
    * Scroll down and click **"Commit new file"**.
    * Then, click on the newly created `images` folder to go inside it. (You can delete `dummy.txt` from there later if you wish).
3.  **Once you are *inside* the `images` folder on GitHub:**
    * Click the **"Add file"** button.
    * Select **"Upload files"**.
    * **Drag and drop your four `.png` screenshot files** from your computer into the upload area.
    * Scroll down, add a commit message (e.g., "Upload final screenshots"), and click **"Commit changes"**.

After you finish that last step and refresh your GitHub repository page, your `README.md` should finally display all your images!
