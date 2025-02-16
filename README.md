# 🏋️‍♂️ Workout-tracker 💪
A Python-based workout tracking script that integrates Nutritionix API and Sheety API to log exercise data and calorie burn automatically.

# ✨ Features
- Track Exercises – Input your workout, and the script fetches details (duration, calories burned, etc.) from Nutritionix 🏃‍♂️🔥
-  Log Workouts to Google Sheets – Uses Sheety API 📑 to store workout data in an online spreadsheet.
-   Automatic Date & Time Logging – Records workouts with the current date & time ⏰

# 🤖 Behind the Scenes
The Workout Tracker uses two key APIs:
- Nutritionix API 🥗 – Uses NLP (Natural Language Processing) to analyze user input and extract structured exercise data.
- Sheety API 📊 – Connects to Google Sheets and stores the exercise data automatically.
### 1️⃣ You Enter Your Workout
💬 Example:
"I ran 5 km and did 20 pushups."

### 2️⃣ Nutritionix API Understands Your Workout
NLP Model:
- Breaks the input into meaningful chunks.
- Identifies different exercises from a pre-trained exercise database.
- Estimates calories burned based on weight, height, age, and gender

### 3️⃣ 📡 Request Sent to Nutritionix
### 4️⃣ Storing Data in Google Sheets via Sheety API
📥 Workout Data Received from Nutritionix
- Once the API extracts exercise details, the script formats them and sends them to Sheety API, which updates Google Sheets.
 ![image](https://github.com/user-attachments/assets/6046a7da-2a1b-45e8-b76f-ffc5916f2109)




