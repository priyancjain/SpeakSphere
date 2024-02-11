# backend.py

import sqlite3
import streamlit as st

# Function to create a database connection
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

# Function to create a new user
def create_user(conn, username, password,is_speaker,speaker_name, speaker_bio,
                                       linkedin_link, twitter_link, github_link,
                                       phone_number, past_experience, photo):
    
    sql = ''' INSERT INTO users(username,password,
    is_speaker,
            speaker_name,
            speaker_bio,
            linkedin_link,
            twitter_link,
            github_link,
            phone_number,
            past_experience,
            photo)
            VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
    
    cur = conn.cursor()
    cur.execute(f"SELECT past_experience FROM users")
    column_data = cur.fetchall()
    # Flatten the nested list
    flat_list = [item for sublist in column_data for item in sublist]

# Remove empty strings and duplicates
    names = list(filter(None, set(flat_list)))
    if username not in names:
        cur.execute(sql, (username, password,is_speaker, speaker_name, speaker_bio,
                                       linkedin_link, twitter_link, github_link,
                                       phone_number, past_experience, photo))
        conn.commit()
        st.success("Speaker profile updated successfully!")
        return cur.lastrowid
    else:
        st.error("username already exist")
        return None
# Function to authenticate a user
def authenticate_user(conn, username, password):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cur.fetchone()
    if user:
        if user[2] == password:
            return True
    return False

# Function to search for speakers or mentors
def search_users(conn, query):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE past_experience LIKE ?", ('%' + query + '%',))
    return cur.fetchall()

def update_speaker_profile(conn, username, speaker_name, speaker_bio):
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET speaker_name=?, speaker_bio=? WHERE username=?", (speaker_name, speaker_bio, username))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print("Error updating speaker profile:", e)
        return False
    
def update_speaker_profile(conn, username, speaker_name, speaker_bio,
                           linkedin_link, twitter_link, github_link,
                           phone_number, past_experience, photo):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE users SET 
            speaker_name=?,
            speaker_bio=?,
            linkedin_link=?,
            twitter_link=?,
            github_link=?,
            phone_number=?,
            past_experience=?,
            photo=?
            WHERE username=?
            """, (speaker_name, speaker_bio, linkedin_link, twitter_link, github_link,
                  phone_number, past_experience, photo, username))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print("Error updating speaker profile:", e)
        return False