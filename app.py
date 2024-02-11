import streamlit as st
from backend import create_connection, create_user, authenticate_user, search_users, update_speaker_profile
import webbrowser
# Remove Streamlit footer
custom_css = """
<style>
footer {
    display: none;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Define a session state object
def complete_details(conn,username,new_password):
            st.header("Speaker Details")
            speaker_name = st.text_input("Speaker Name",value="",placeholder = None)
            speaker_bio = st.text_area("Speaker Bio",value="",placeholder = None)
            linkedin_link = st.text_input("LinkedIn Link",value="",placeholder = None)
            twitter_link = st.text_input("Twitter Link",value="",placeholder = None)
            github_link = st.text_input("GitHub Link",value="",placeholder = None)
            phone_number = st.text_input("Phone Number",value="",placeholder = None)
            is_speaker = st.number_input("Is speaker",value=0)
            past_experience = st.text_area("Past Experience",value="",placeholder = None)
            photo = st.file_uploader("Upload Photo", type=["jpg", "png"])
            if photo != None:
                 photo = photo.read()

            if st.button("Submit"):
                create_user(conn, username,new_password, is_speaker,speaker_name, speaker_bio,
                                       linkedin_link, twitter_link, github_link,
                                       phone_number, past_experience, photo )
                

st.title("SpeakerSphere")
# Create a database connection
conn = create_connection("speakers.db")
if conn is not None:
    # Create users table if it doesn't exist
    create_table_sql = '''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY,
                            username TEXT NOT NULL,
                            password TEXT NOT NULL,
                            is_speaker INTEGER DEFAULT 0,
                            speaker_name TEXT,
                            speaker_bio TEXT,
                            linkedin_link TEXT,
                            twitter_link TEXT,
                            github_link TEXT,
                            phone_number TEXT,
                            past_experience TEXT,
                            photo BLOB
                        );'''
    conn.execute(create_table_sql)
    # Toggle Menu Navigation Bar
    st.sidebar.title("Navigation")
    menu_options = ["Home", "Login", "Signup", "Find"]
    selected_menu_item = st.sidebar.radio("Home", menu_options)
    # Display selected section based on the menu item

    if selected_menu_item == "Home":
        st.subheader("Welcome to the Home Page!")
        st.write("This is the home page of the application.")
        # st.set_page_config(page_title="SpeakerSphere", page_icon="🔊", layout="wide")
        st.markdown(
        """
        <style>
        .reportview-container {
            background: url('your_background_image_url_here');
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

        # Add title and introductory text
        st.title("Welcome to SpeakerSphere!")
        st.write("Connect with speakers and mentors around the globe.")

        # Add sections with more information
        st.header("What is SpeakerSphere?")
        st.write("SpeakerSphere is a platform designed to help you find speakers and mentors in various fields, including technology, business, science, and more.")

        st.header("Why SpeakerSphere?")
        st.write("Whether you're looking for guidance, inspiration, or collaboration, SpeakerSphere connects you with experienced professionals who can help you achieve your goals.")

        st.header("Get Started")
        st.write("Join SpeakerSphere today to start exploring, connecting, and learning!")

        # Add a call-to-action button for signup
        if st.button("Join SpeakerSphere"):
            st.write("Sign up for an account to get started!")


    elif selected_menu_item == "Login":
        st.header("Login")
        username_input = st.text_input("Username",value="",placeholder = None)
        password_input = st.text_input("Password", type="password",value="",placeholder = None)
        if st.button("Login"):
            if authenticate_user(conn, username_input, password_input):
                st.success("Logged in successfully!")
            else:
                st.error("Invalid username or password.")

    elif selected_menu_item == "Signup":
        st.header("Signup")
        new_username = st.text_input("Choose a username",value="",placeholder = None)
        new_password = st.text_input("Choose a password", type="password",value="",placeholder = None)
        complete_details(conn,new_username,new_password) 
            
    elif selected_menu_item == "Find":
        st.header("Search Speakers/Mentors")
        search_query = st.text_input("Enter the name of the speaker or mentor or just click search:")
        if st.button("Search"):
            search_results = search_users(conn, search_query)
            if search_results:
                st.write("Search Results:")
                # Apply the function to the 'Profile Link' column
                
            # Remove the third column from the search results
                modified_results = [result[:2] + result[3:] for result in search_results]
                st.table(modified_results)  # Assuming username is stored in the second column
            else:
                st.write("No results found.")
        col1, col2 = st.columns(2)

            # Add buttons to the first column
        with col1:
            if st.button("Book 1"):
                webbrowser.open("https://calendly.com/monishkanungo23/speakersphere")
        
        # Add buttons to the second column
        with col2:
            if st.button("Book 2"):
                webbrowser.open("https://calendly.com/monishkanungo23/speakersphere")