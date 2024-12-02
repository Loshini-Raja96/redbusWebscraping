import streamlit as st
from sqlQueries import fetch_data_from_mysql
    
# Add custom CSS for the header and footer
st.markdown(
    """
    <style>
        /* Header Styles */
        .header {
            background-color: #4CAF50;  /* Green */
            color: white;
            font-size: 36px;
            text-align: center;
            padding: 20px;
            border-radius: 10px;
        }

        /* Footer Styles */
        .footer {
            background-color: #333;  /* Dark gray */
            color: white;
            font-size: 14px;
            text-align: center;
            padding: 10px;
            position: fixed;
            bottom: 0;
            width: 100%;
            left: 0;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar navigation
page = st.sidebar.radio("Navigation", ["Home", "RedBus Search"])

# Create header
#st.markdown('<div class="header">RedBus Data Scraping with Selenium</div>', unsafe_allow_html=True)

# Page: Home
if page == "Home":
    st.write("## Welcome to the RedBus Data Scraping App 🚍")
    st.write("Use the **RedBus Search** page to filter and search for bus details.")
    st.image("C:/Users/hp/OneDrive/Desktop/red.png")

# Page: RedBus Search
elif page == "RedBus Search":
    st.write("## RedBus Search 🚌")
    st.write("Use this page to search for buses based on your preferences.")

    # Filters
    Routes=fetch_data_from_mysql('SELECT Routes FROM route_name')
        
    st.sidebar.header("Search Filters")
    from_location = st.sidebar.selectbox("From Location", Routes)  
    to_location = st.sidebar.selectbox("To Location", Routes)  

    Filters=fetch_data_from_mysql('SELECT bus_type from bus_types')

    bus_type = st.sidebar.multiselect("Bus Type Filters",Filters,default=Filters)
    print(f'The selected bus type is {bus_type}')    

    min_rating = st.sidebar.slider("Minimum Star Rating", 0.0, 5.0, 3.0)
    max_price = st.sidebar.slider("Price Range", 0, 2000, 600)

    print(f'The min_rating is {min_rating}')
    print(f'The max_price is {max_price}')

    # Fetch and filter data
    data = fetch_data_from_mysql("SELECT * FROM bus_routes")

    # Filter by location
    filtered_data = data[
        (data["Route_Name"].str.contains(from_location, case=False)) & 
        (data["Route_Name"].str.contains(to_location, case=False))
    ]

    if bus_type:
        filtered_data['bus_type_normalized'] = filtered_data['Bus_Type'].str.lower().str.strip()
        print(f'Normalized bus is {filtered_data['bus_type_normalized']}')
        normalized_bus_type = [item.lower() for item in bus_type]
        filtered_data = filtered_data[filtered_data['bus_type_normalized'].apply(
            lambda x: any(bt in x for bt in normalized_bus_type)
        )]
    # if bus_type:
    #     filtered_data = filtered_data[filtered_data["Bus_Type"].isin(bus_type)]

    filtered_data = filtered_data[
        (filtered_data["Star_Rating"] >= min_rating) &
        (filtered_data["Price"] <= max_price)
    ]
    print(f'The filtered data is {filtered_data}')
    # if bus_type:
    #     filtered_data = filtered_data[filtered_data["Bus_Type"].isin(bus_type)]
        
    # print(f'The fil data is {filtered_data["Bus_Type"]}')

    # Display data
    st.write(f"### Search Results ({len(filtered_data)})")
    st.dataframe(filtered_data)

    # Download filtered data as CSV
    st.download_button(
        label="Download CSV",
        data=filtered_data.to_csv(index=False),
        file_name="filtered_bus_data.csv",
        mime="text/csv"
    )
   
# Create footer
st.markdown('<div class="footer">© 2024 RedBus Scraping App | All Rights Reserved</div>', unsafe_allow_html=True)
