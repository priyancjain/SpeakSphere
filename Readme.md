# SpeakerSphere

SpeakerSphere is a Streamlit-based web application that connects users with speakers and mentors.  
It allows users to create detailed speaker profiles, search for experts, and book sessions directly.

## Features
- **User Registration & Login** – Secure signup and authentication.
- **Speaker Profiles** – Add bio, social media links, past experience, and profile photo.
- **Search Functionality** – Find speakers/mentors by their expertise.
- **Booking Integration** – Book sessions via Calendly links.
- **SQLite Database** – Stores user and speaker information.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/priyancjain/SpeakSphere.git
   cd SpeakSphere
   ```
   
## 2.Install dependencies:
```bash
   pip install -r requirements.txt
```

## 3.Run the app:
```bash
   streamlit run app.py
```

## 4.Project Structure

```bash
.
├── app.py          # Main Streamlit application
├── backend.py      # Database operations & user management
├── requirements.txt
└── speakers.db     # SQLite database (auto-created if not present)
```

## 5.Tech Stack
Frontend/UI: Streamlit
Backend: Python (SQLite for storage)
Integrations: Calendly for booking



```https://speakersphere.streamlit.app/```

![image](https://github.com/user-attachments/assets/5988613f-3e7c-407c-8c3f-84ee6abfeabf)
