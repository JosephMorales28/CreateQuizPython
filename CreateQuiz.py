# Define a list of questions and their corresponding correct answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which programming language is this quiz written in?",
        "options": ["Java", "Python", "C++", "JavaScript"],
        "answer": "Python"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    }
]

# Initialize a variable to keep track of the score
score = 0

# Iterate through the questions and present them to the user
for question in questions:
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i + 1}. {option}")
    
    # Get user input
    user_answer = input("Enter the number of your answer: ")
    
    # Check if the user's answer is correct
    if question["options"][int(user_answer) - 1] == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {question['answer']}")

# Calculate and display the final score
total_questions = len(questions)
percentage_score = (score / total_questions) * 100
print(f"You got {score} out of {total_questions} questions correct, which is {percentage_score}%.")
