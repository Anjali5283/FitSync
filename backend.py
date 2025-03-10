import google.generativeai as genai
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Replace with actual Gemini API key
GEMINI_API_KEY = 'AIzaSyClahyZpppiE3wfqC0Y-OQKWSKKzFQfwpA'
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('models/gemini-1.5-pro-latest')

reminders = []

def get_ai_response(user_input, health_details=""):
    try:
        prompt = f"""
        You are a fitness coach. Analyze the user's details below and provide personalized fitness advice.

        User's Workout Data:
        {user_input}

        Health Details:
        {health_details}
        """
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Failed to get response from AI: {str(e)}"
# Water Intake Tracker Class
class WaterIntakeTracker:
    def __init__(self):
        self.water_intake = 0
        self.DAILY_WATER_GOAL = 2000  # 2 liters in ml

    def log_water(self, amount):
        self.water_intake += amount

    def get_water_progress(self):
        return (self.water_intake / self.DAILY_WATER_GOAL) * 100

    def get_water_intake(self):
        return self.water_intake

# Create a global instance of WaterIntakeTracker
water_tracker = WaterIntakeTracker()

# Function to log water intake
def log_water(amount):
    water_tracker.log_water(amount)

# Function to get water progress
def get_water_progress():
    return water_tracker.get_water_progress()

# Function to get current water intake
def get_water_intake():
    return water_tracker.get_water_intake()


def add_reminder(user_id, reminder_time, frequency, message, email):
    reminders.append({'user_id': user_id, 'reminder_time': reminder_time, 'frequency': frequency, 'message': message, 'email': email})

def get_reminders(user_id):
    return [r for r in reminders if r['user_id'] == user_id]

def send_email(to_email, subject, body):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'your_email@gmail.com'
    sender_password = 'your_email_password'
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())
        return True
    except Exception as e:
        return False

def calculate_bmi(weight, height):
    return weight / ((height / 100) ** 2)

def calculate_calories(age, weight, height, gender, activity_level):
    return 2000  # Dummy value for now

def get_food_suggestion(bmi, calories, water_intake, workout_data, health_details):
    prompt = f"""
    You are a professional nutritionist. Create a **detailed** daily meal plan for the user based on their health details.

    **User's Health Profile:**
    - {health_details}
    - BMI: {bmi} ({interpret_bmi(bmi)})
    - Daily Calorie Needs: {calories:.2f} kcal
    - Water Intake: {water_intake} ml (Goal: 2000 ml)
    - Workout Data: {workout_data}

    **Guidelines for the meal plan:**
    - Provide meals for **breakfast, mid-morning snack, lunch, afternoon snack, and dinner**.
    - Ensure the meals meet the user's **caloric and nutritional needs**.
    - Consider any **dietary restrictions, allergies, or diseases**.
    - Use simple, accessible ingredients.

    **Example Output Format:**
    - **Breakfast**: [Meal with calories]
    - **Mid-Morning Snack**: [Snack with calories]
    - **Lunch**: [Meal with calories]
    - **Afternoon Snack**: [Snack with calories]
    - **Dinner**: [Meal with calories]

    Provide a structured response in a clean, easy-to-read format.
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Failed to get food suggestion: {str(e)}"


def get_exercise_video_id(exercise_name):
    # Example mapping of exercise names to YouTube video IDs
    exercise_to_video = {
        "push-ups": "qU_QESJ7zPs",
        "squats": "CsPAsICeRsM",  # Replace with actual video IDs
        "yoga": "dAqQqmaI9vY",
        "pull-ups": "G5YExSjm1bo",
        "running": "C5Zq-zb_hJA",  # Replace with actual video IDs
    }
    return exercise_to_video.get(exercise_name.lower(), None)  # Return None if exercise not found
# Function to interpret BMI category
def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

