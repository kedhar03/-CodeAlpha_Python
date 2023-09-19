class Quiz:
    def __init__(self):
        self.questions = []

    def add_question(self, question, options, correct_option):
        self.questions.append({
            "question": question,
            "options": options,
            "correct_option": correct_option
        })

    def take_quiz(self):
        score = 0
        for i, question_data in enumerate(self.questions, 1):
            print(f"Question {i}: {question_data['question']}")
            for j, option in enumerate(question_data['options'], 1):
                print(f"{j}. {option}")
            
            user_answer = input("Your answer (enter the option number): ")
            
            try:
                user_answer = int(user_answer)
                if 1 <= user_answer <= len(question_data['options']):
                    if user_answer == question_data['correct_option']:
                        print("Correct!\n")
                        score += 1
                    else:
                        print(f"Wrong! The correct answer is {question_data['correct_option']}\n")
                else:
                    print("Invalid option number. Try again.\n")
            except ValueError:
                print("Invalid input. Enter a valid option number.\n")
        
        print(f"Quiz completed. Your score: {score}/{len(self.questions)}")

def main():
    quiz = Quiz()
    
    # Add questions to the quiz
    quiz.add_question("What is the capital of France?", ["Paris", "London", "Berlin", "Madrid"], 1)
    quiz.add_question("Which planet is known as the Red Planet?", ["Earth", "Mars", "Venus", "Jupiter"], 2)
    quiz.add_question("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], 2)
    
    print("Welcome to the Quiz Application!")
    user_type = input("Are you an administrator (A) or a regular user (U)? ").strip().lower()
    
    if user_type == 'a':
        # Administrator mode: Add questions to the quiz
        while True:
            question = input("Enter the question: ")
            options = [input(f"Enter option {i}: ") for i in range(1, 5)]
            correct_option = int(input("Enter the correct option number: "))
            quiz.add_question(question, options, correct_option)
            
            another_question = input("Add another question (yes/no)? ").strip().lower()
            if another_question != 'yes':
                break
    elif user_type == 'u':
        # User mode: Take the quiz
        quiz.take_quiz()
    else:
        print("Invalid user type. Exiting.")

if __name__ == "__main__":
    main()
