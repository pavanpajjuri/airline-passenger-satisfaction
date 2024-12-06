import streamlit as st
import pandas as pd
from sqlalchemy import create_engine  # type: ignore

# Database URI for Airline Passenger Satisfaction database
db_uri = "postgresql+psycopg2://postgres:pavanpaj@127.0.0.1:5432/Passenger_Airline_Satisfaction"
engine = create_engine(db_uri)

def run_query(query, params=None):
    """Executes a SQL query and returns the results as a DataFrame."""
    with engine.connect() as connection:
        result = connection.execute(query, params)  # Execute query
        data = result.fetchall()  # Fetch the result
        columns = result.keys()  # Get column names from result
        return pd.DataFrame(data, columns=columns)  # Convert to DataFrame

# Streamlit app structure
st.title("Airline Passenger Satisfaction Database")

# Page navigation
page = st.sidebar.radio(
    "Go to",
    ["Passengers", "Flights", "Satisfaction Ratings", "Delays", "Overall Satisfaction", "Custom Query"]
)

# Passengers page
if page == "Passengers":
    st.header("Passengers Data")

    passengers_query_options = [
        "Passengers by Customer Type",
        "Passengers by Age Range"
    ]

    selected_passenger_query = st.selectbox("Select a query:", passengers_query_options)

    if selected_passenger_query == "Passengers by Customer Type":
        customer_type = st.text_input("Enter customer type (e.g., 'Loyal Customer'):")
        if customer_type:  # Ensure input is not empty
            passenger_query = """
            SELECT * FROM passengers WHERE customertype LIKE %s LIMIT 10;
            """
            params = (f"%{customer_type}%",)  # Use wildcards for partial matching
            passenger_df = run_query(passenger_query, params=params)
            st.write(passenger_df)

    elif selected_passenger_query == "Passengers by Age Range":
        min_age = st.number_input("Enter minimum age:", min_value=0)
        max_age = st.number_input("Enter maximum age:", min_value=0)
        if min_age and max_age:  # Ensure valid age range
            passenger_query = """
            SELECT * FROM passengers WHERE age BETWEEN %s AND %s LIMIT 10;
            """
            params = (min_age, max_age)  # Age range for the query
            passenger_df = run_query(passenger_query, params=params)
            st.write(passenger_df)

# Flights page
elif page == "Flights":
    st.header("Flights Data")

    flights_query_options = [
        "Flights by Type of Travel",
        "Flights by Class"
    ]

    selected_flights_query = st.selectbox("Select a query:", flights_query_options)

    if selected_flights_query == "Flights by Type of Travel":
        travel_type = st.text_input("Enter type of travel (e.g., 'Business Travel'):")
        if travel_type:  # Ensure input is not empty
            flights_query = """
            SELECT * FROM flights WHERE typeoftravel LIKE %s LIMIT 10;
            """
            params = (f"%{travel_type}%",)  # Use wildcards for partial matching
            flights_df = run_query(flights_query, params=params)
            st.write(flights_df)

    elif selected_flights_query == "Flights by Class":
        flight_class = st.text_input("Enter class (e.g., 'Business'):")
        if flight_class:  # Ensure input is not empty
            flights_query = """
            SELECT * FROM flights WHERE class LIKE %s LIMIT 10;
            """
            params = (f"%{flight_class}%",)  # Use wildcards for partial matching
            flights_df = run_query(flights_query, params=params)
            st.write(flights_df)

# Satisfaction Ratings page
elif page == "Satisfaction Ratings":
    st.header("Satisfaction Ratings Data")

    satisfaction_query_options = [
        "Ratings by Seat Comfort",
        "Ratings by Inflight Wi-Fi"
    ]

    selected_satisfaction_query = st.selectbox("Select a query:", satisfaction_query_options)

    if selected_satisfaction_query == "Ratings by Seat Comfort":
        seat_comfort = st.number_input("Enter Seat Comfort rating (1-5):", min_value=1, max_value=5)
        satisfaction_query = """
        SELECT * FROM satisfaction_ratings WHERE seatcomfort = %s LIMIT 10;
        """
        params = (seat_comfort,)  # Exact match for rating
        satisfaction_df = run_query(satisfaction_query, params=params)
        st.write(satisfaction_df)

    elif selected_satisfaction_query == "Ratings by Inflight Wi-Fi":
        wifi_rating = st.number_input("Enter Wi-Fi rating (1-5):", min_value=1, max_value=5)
        satisfaction_query = """
        SELECT * FROM satisfaction_ratings WHERE inflightwifiservice = %s LIMIT 10;
        """
        params = (wifi_rating,)  # Exact match for Wi-Fi service rating
        satisfaction_df = run_query(satisfaction_query, params=params)
        st.write(satisfaction_df)

# Delays page
elif page == "Delays":
    st.header("Delays Data")

    delays_query_options = [
        "Delays by Flight",
        "Delays by Departure Time"
    ]

    selected_delays_query = st.selectbox("Select a query:", delays_query_options)

    if selected_delays_query == "Delays by Flight":
        flight_id = st.number_input("Enter Flight ID (e.g., 123):", min_value=1)
        delays_query = """
        SELECT * FROM delays WHERE flightid = %s LIMIT 10;
        """
        params = (flight_id,)  # Exact match for flight ID
        delays_df = run_query(delays_query, params=params)
        st.write(delays_df)

    elif selected_delays_query == "Delays by Departure Time":
        departure_time = st.time_input("Enter departure time:")
        delays_query = """
        SELECT * FROM delays WHERE arrivaldelayinminutes > 0 AND EXTRACT(HOUR FROM departuretime) = %s LIMIT 10;
        """
        params = (departure_time.hour,)  # Filter by hour of departure
        delays_df = run_query(delays_query, params=params)
        st.write(delays_df)

# Overall Satisfaction page
elif page == "Overall Satisfaction":
    st.header("Overall Satisfaction Data")

    satisfaction_query_options = [
        "Satisfaction by Rating",
        "Satisfaction by Customer Type"
    ]

    selected_satisfaction_query = st.selectbox("Select a query:", satisfaction_query_options)

    if selected_satisfaction_query == "Satisfaction by Rating":
        satisfaction_rating = st.text_input("Enter Satisfaction rating (e.g., 'satisfied', 'neutral or dissatisfied'):")
        overall_satisfaction_query = """
        SELECT * FROM overall_satisfaction WHERE satisfaction = %s LIMIT 10;
        """
        params = (satisfaction_rating,)  # Exact match for satisfaction rating
        overall_satisfaction_df = run_query(overall_satisfaction_query, params=params)
        st.write(overall_satisfaction_df)

    elif selected_satisfaction_query == "Satisfaction by Customer Type":
        customer_type = st.text_input("Enter customer type (e.g., 'Loyal Customer'):")
        if customer_type:  # Ensure input is not empty
            overall_satisfaction_query = """
            SELECT * FROM overall_satisfaction WHERE passengerid IN (SELECT passengerid FROM passengers WHERE customertype LIKE %s);
            """
            params = (f"%{customer_type}%",)  # Use wildcards for partial matching
            overall_satisfaction_df = run_query(overall_satisfaction_query, params=params)
            st.write(overall_satisfaction_df)

# Custom Query page
elif page == "Custom Query":
    st.header("Custom Query")

    # Input box for user-defined SQL query
    user_query = st.text_area("Enter your SQL query here:", "")

    # Button to execute the query
    if st.button("Run Query"):
        if user_query.strip():  # Check if the user has entered a query
            try:
                # Run and display the user-defined query
                result_df = run_query(user_query)
                st.write(result_df)
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.error("Please enter a valid SQL query.")
