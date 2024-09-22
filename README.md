Streamlit Restaurant Visualization App
This is a Streamlit web application designed for visualizing and analyzing restaurant data. The app allows users to view restaurants on an interactive map, filter restaurants based on ratings, and generate dynamic charts for data insights.

Features
Interactive Map: Displays restaurants on a Folium-based map.
Data Upload: Upload your own CSV file with restaurant data.
Data Visualization: Generate various graphs and charts (e.g., bar charts, rating distributions) using Plotly and Seaborn.
Filtering: Filter restaurants based on ratings and other criteria.
Responsive Interface: Simple and user-friendly layout built with Streamlit.
Installation
1. Clone the Repository
bash
Copy code
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Set up a Python Virtual Environment (optional but recommended)
bash
Copy code
python -m venv venv
source venv/bin/activate    # On Windows use: venv\Scripts\activate
3. Install Required Dependencies
bash
Copy code
pip install -r requirements.txt
4. Run the Streamlit App
bash
Copy code
streamlit run main_app.py
The app will now be accessible at http://localhost:8501 in your web browser.

Docker Instructions
To run the app in a Docker container, follow these steps:

1. Build the Docker Image
bash
Copy code
docker build -t my-streamlit-app .
2. Run the Docker Container
bash
Copy code
docker run -p 8501:8501 my-streamlit-app
Now, access the app in your browser at http://localhost:8501.

Usage
Upload a CSV File: Use the interface to upload your restaurant data in CSV format.
Interactive Map: The app shows the restaurants' locations on an interactive map.
Graphical Visualizations: Automatically generates bar charts and distribution charts based on restaurant ratings and other criteria.
Filtering: Filter restaurants based on rating or other factors provided in the dataset.
Example Data Format
Your CSV file should contain the following columns:

name: Restaurant name
bio: Short description of the restaurant
address: Physical address of the restaurant
rating: Restaurant rating (numerical value)
longitude: Longitude coordinate
latitude: Latitude coordinate
Sample row:

css
Copy code
name,bio,address,rating,longitude,latitude
Restaurant A,Italian cuisine,123 Main St,4.5,-0.1257,51.5085
Dependencies
The app uses the following Python libraries:

streamlit
pandas
folium
streamlit-folium
matplotlib
seaborn
plotly
These are listed in the requirements.txt file and can be installed by running:

bash
Copy code
pip install -r requirements.txt
Contributing
Contributions are welcome! Please feel free to submit issues or pull requests.

License
This project is licensed under the MIT License - see the LICENSE file for details.
