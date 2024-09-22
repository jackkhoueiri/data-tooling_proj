import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# Load the dataset with latitude and longitude
uploaded_file = st.sidebar.file_uploader("Upload your restaurant CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    # Sidebar for filtering options
    st.sidebar.subheader("Filter Restaurants")
    
    # Filter by cuisine (assuming your CSV has a 'cuisine' column)
    if 'cuisine' in data.columns:
        cuisine_type = st.sidebar.multiselect("Select Cuisine Type", data['cuisine'].unique())
    else:
        cuisine_type = []

    # Filter by rating (assuming your CSV has a 'rating' column)
    if 'rating' in data.columns:
        min_rating = st.sidebar.slider("Minimum Rating", 1, 5, 3)
    else:
        min_rating = 1

    # Filter dataset based on selections
    filtered_data = data[(data['rating'] >= min_rating)]
    
    if cuisine_type:
        filtered_data = filtered_data[filtered_data['cuisine'].isin(cuisine_type)]

    # Step 1: Add restaurant selection
    st.sidebar.subheader("Select a Restaurant")
    restaurant_name = st.sidebar.selectbox("Choose a restaurant", ['Show All'] + list(filtered_data['name'].unique()))
    
    # Step 2: Button to clear selection (reset the filter)
    clear_filter = st.sidebar.button("Clear Selection")

    # Step 3: If a restaurant is selected, filter the dataset to only show that restaurant on the map
    if restaurant_name != 'Show All' and not clear_filter:
        selected_restaurant = filtered_data[filtered_data['name'] == restaurant_name]
    else:
        selected_restaurant = filtered_data  # Show all restaurants if no filter or clear filter button is pressed

    # Step 4: Display the map with filtered or full data
    st.write("### Restaurants on the Map")
    center_lat = selected_restaurant['latitude'].mean()
    center_lon = selected_restaurant['longitude'].mean()
    
    restaurant_map = folium.Map(location=[center_lat, center_lon], zoom_start=12)

    # Add markers for selected restaurant(s)
    for index, row in selected_restaurant.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"{row['name']} - {row['address']}",
            tooltip=row['name']
        ).add_to(restaurant_map)

    # Display the map
    folium_static(restaurant_map)

    # Step 5: Display detailed information for selected restaurant
    if restaurant_name != 'Show All' and not clear_filter:
        st.write("### Restaurant Details")
        for col in selected_restaurant.columns:
            st.write(f"**{col}:** {selected_restaurant.iloc[0][col]}")

# Select columns to visualize (for simplicity, assuming 'rating' and 'cuisine' columns exist)
    if 'rating' in data.columns:
        # Group by rating and count the number of restaurants for each rating
        rating_counts = data['rating'].value_counts().sort_index()
        # Bar chart: Number of restaurants for each rating
        st.write("### Number of Restaurants for Each Rating")
        fig, ax = plt.subplots()
        sns.barplot(x=rating_counts.index, y=rating_counts.values, ax=ax)
        ax.set(xlabel="Rating", ylabel="Number of Restaurants")
        st.pyplot(fig)
        # Optional: Add an interactive version using Plotly
        st.write("### Interactive Bar Chart of Rating Distribution")
        fig_interactive = px.bar(x=rating_counts.index, y=rating_counts.values, labels={'x': 'Rating', 'y': 'Number of Restaurants'}, title="Number of Restaurants per Rating")
        st.plotly_chart(fig_interactive)

    else:
        st.error("The CSV file must contain a 'rating' column.")

    if 'rating' in data.columns and 'price' in data.columns and 'numberOfReviews' in data.columns:
        st.write("### Bubble Chart: Price vs. Rating vs. Reviews")
        fig_bubble = px.scatter(data, x='price', y='rating', size='numberOfReviews', color='rating',
                               title='Price vs. Rating vs. Reviews', hover_name='name')
        st.plotly_chart(fig_bubble)

else:
    st.write("Please upload a CSV file to view restaurant data.")