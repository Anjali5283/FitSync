import streamlit as st
from backend import (
    get_ai_response, add_reminder, get_reminders, send_email,
    log_water, get_water_progress, calculate_bmi, interpret_bmi, 
    calculate_calories, get_food_suggestion, get_water_intake, get_exercise_video_id
)


# Streamlit app
def main():
    st.title("FitSync AI - Your Personal Fitness Coach")
    st.write("Welcome to FitSync AI! Get personalized fitness advice, meal plans, and workout suggestions tailored to your health and goals.")

    # Health Details Sidebar
    st.sidebar.title("Health Details")
    with st.sidebar.expander("📝 Enter Health Details"):
        age = st.number_input("Age", min_value=1, value=25, key="age")
        weight = st.number_input("Weight (kg)", min_value=1, step=1, format="%d", value=70, key="weight")
        height = st.number_input("Height (cm)", min_value=1, value=170, key="height")
        gender = st.selectbox("Gender", ["Male", "Female"], key="gender")
        activity_level = st.selectbox("Activity Level", [
            "Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extra Active"
        ], key="activity")
        diseases = st.text_input("Any diseases (e.g., diabetes, hypertension)", key="diseases")
        allergies = st.text_input("Any allergies (e.g., gluten, nuts)", key="allergies")
        diet = st.text_input("Any dietary preferences (e.g., vegetarian, vegan)", key="diet")

    # Prepare health details
    health_details = f"Age: {age}, Weight: {weight} kg, Height: {height} cm, Gender: {gender}, Activity Level: {activity_level}, Diseases: {diseases}, Allergies: {allergies}, Diet: {diet}"

    # Fitness Advice Section
    st.header("Fitness Advice")
    user_input = st.text_area("Enter your fitness question or workout data below:", height=150)

    if st.button('Get Advice'):
        if user_input:
            with st.spinner('Fetching your personalized advice...'):
                st.session_state.fitness_advice = get_ai_response(user_input, health_details)
        else:
            st.error("Please enter some input to get advice.")

    # Display stored fitness advice
    if "fitness_advice" in st.session_state:
        st.success("Here's your advice:")
        st.write(st.session_state.fitness_advice)

    # Food Suggestion Section
    st.header("🍽️ Food Suggestion")
    if st.button("Get Personalized Meal Plan"):
        with st.spinner('Generating your personalized meal plan...'):
            bmi = calculate_bmi(weight, height)
            calories = calculate_calories(age, weight, height, gender, activity_level)
            water_intake = get_water_intake()
            st.session_state.food_suggestion = get_food_suggestion(bmi, calories, water_intake, user_input, health_details)

    # Display stored food suggestion
    if "food_suggestion" in st.session_state:
        st.success("Here's your personalized meal plan:")
        st.write(st.session_state.food_suggestion)

    # Water Intake Tracker
    st.sidebar.header("💧 Water Intake Tracker")
    water_amount = st.sidebar.number_input("Amount of water (ml)", min_value=0, value=500, key="water")
    if st.sidebar.button("Log Water Intake"):
        log_water(water_amount)
        st.sidebar.success(f"Logged {water_amount} ml of water!")
    st.sidebar.write(f"Daily Goal: {2000} ml")
    st.sidebar.progress(get_water_progress() / 100)

    # Reminder Section
    st.sidebar.header("⏰ Set Progress Reminders")
    user_id = st.sidebar.number_input("User ID", min_value=1, value=1, key="user_id")
    reminder_time = st.sidebar.time_input("Reminder Time", key="reminder_time")
    frequency = st.sidebar.selectbox("Frequency", ["daily", "weekly", "monthly"], key="frequency")
    message = st.sidebar.text_input("Reminder Message", "Log your workout for today!", key="message")
    email = st.sidebar.text_input("Your Email", "user@example.com", key="email")

    if st.sidebar.button('Set Reminder'):
        add_reminder(user_id, reminder_time.strftime('%H:%M'), frequency, message, email)
        st.sidebar.success("Reminder set successfully!")
        if send_email(email, "FitSync Reminder", f"Reminder: {message}\nTime: {reminder_time.strftime('%H:%M')}\nFrequency: {frequency}"):
            st.sidebar.success("Email notification sent!")
        else:
            st.sidebar.error("Failed to send email notification.")

    # Display Active Reminders
    st.header("📅 Active Reminders")
    user_reminders = get_reminders(user_id)
    if user_reminders:
        for reminder in user_reminders:
            st.write(f"Time: {reminder['reminder_time']}, Frequency: {reminder['frequency']}, Message: {reminder['message']}")
    else:
        st.write("No reminders set.")

    # Exercise Video Section
    st.header("🎥 Exercise Video")
    exercise_name = st.text_input("Enter the exercise you want to see as a video (e.g., push-ups, squats):")

    if exercise_name:
        video_id = get_exercise_video_id(exercise_name)
        if video_id:
            st.success(f"Here's the video for {exercise_name}:")
            st.video(f"https://www.youtube.com/watch?v={video_id}")
        else:
            st.error(f"No video found for the exercise: {exercise_name}")

if __name__ == "__main__":
    main()
