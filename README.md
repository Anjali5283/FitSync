FitSync AI - Your Personal Fitness Coach 🏋️‍♂️💪
FitSync AI is a smart fitness assistant that provides personalized fitness advice, meal plans, workout suggestions, and water intake tracking using AI (Gemini), Streamlit, and Python.

🚀 Features
✅ AI-Powered Fitness Advice – Get customized recommendations for workouts & fitness goals.
✅ Personalized Meal Plan – AI-generated daily meal plans based on BMI, calories, and dietary preferences.
✅ Water Intake Tracker – Log daily water consumption and track progress.
✅ Workout Video Suggestions – Get exercise videos for different workouts.
✅ Reminder System – Set reminders for workouts & hydration, with email notifications.

🛠️ Tech Stack
Frontend: Streamlit (Python-based web UI)
Backend: Google Gemini AI (LLaMA 3 API)
Email Notifications: SMTP (for sending workout/water reminders)
📦 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/Anjali5283/FitSync.git
cd FitSync
2️⃣ Set Up Virtual Environment
python -m venv venv
venv\Scripts\activate     # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Set Up API Keys
Replace your_gemini_api_key in backend.py with your actual Google Gemini API key.
(Optional) Set up SMTP credentials for email notifications.
5️⃣ Run the Application
streamlit run app.py
📌 Usage Guide
💪 Fitness Advice
Enter your workout details or ask fitness-related questions.
Click "Get Advice" to receive AI-generated fitness recommendations.
🍽️ Meal Plan Generator
Fill in your age, weight, height, gender, and dietary preferences.
Click "Get Personalized Meal Plan" to get a structured daily meal plan.
💧 Water Intake Tracker
Log your daily water intake by entering the amount in mL.
View progress toward your daily water goal (2000 mL).
⏰ Reminders & Email Notifications
Set reminders for workouts, hydration, or diet tracking.
Receive an email notification when a reminder is triggered.
🔧 Project Structure
📦 fitsync-ai
 ┣ 📂 assets/          # Static images, logos, UI assets
 ┣ 📂 models/          # (Optional) ML models if needed
 ┣ 📂 scripts/         # Utility scripts (if any)
 ┣ 📜 app.py           # Main Streamlit app (frontend)
 ┣ 📜 backend.py       # Backend logic (AI, calculations, email handling)
 ┣ 📜 requirements.txt # Required dependencies
 ┣ 📜 README.md        # Project documentation
 ┗ 📜 .gitignore       # Ignore unnecessary files
🚀 Future Enhancements
✅ User Authentication – Allow users to save workout history & meal logs.
✅ AI Chatbot – Integrate with ChatGPT/Gemini for real-time health coaching.
✅ Progress Visualization – Add graphs & charts to track progress.

👨‍💻 Contributing
Want to contribute? Follow these steps:

Fork the repository 🍴
Create a new branch (git checkout -b feature-new)
Commit your changes (git commit -m "Added new feature")
Push to your fork (git push origin feature-new)
Create a Pull Request 📩
📞 Contact & Support
🔹 Email: uppuanjali5283@gmail.com
🔹 GitHub Issues: Report a bug
