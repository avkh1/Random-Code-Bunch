import tkinter as tk

class QuizApp:
    def __init__(self, root, filename):
        self.root = root
        self.root.title("Test")
        self.root.geometry("1400x320")

        # Initialize variables
        self.questions = []
        self.answers = []
        self.options = []
        self.current_question = 0
        self.correct_on_first_try = set()
        self.attempted_questions = set()
        self.check_vars = []
        self.check_buttons = []
        self.load_questions(filename)
        
        # Set up question display
        self.question_label = tk.Label(root, text="", wraplength=1200, font=("Arial", 14))
        self.question_label.pack(pady=10)
        
        # Set up checkbuttons frame
        self.check_frame = tk.Frame(root)
        self.check_frame.pack()
        
        # Set up navigation buttons
        self.nav_frame = tk.Frame(root)
        self.nav_frame.pack(side=tk.BOTTOM, pady=10)
        
        self.btn_back = tk.Button(self.nav_frame, text="Zurück", command=self.prev_question)
        self.btn_back.grid(row=0, column=0, padx=5)
        
        self.btn_check = tk.Button(self.nav_frame, text="Überprüfen", command=self.check_answer)
        self.btn_check.grid(row=0, column=1, padx=5)
        
        self.btn_next = tk.Button(self.nav_frame, text="Weiter", command=self.next_question)
        self.btn_next.grid(row=0, column=2, padx=5)
        
        # Set up score and status display
        self.status_frame = tk.Frame(root)
        self.status_frame.pack(pady=5)
        
        self.status_label = tk.Label(self.status_frame, text="", font=("Arial", 12))
        self.status_label.pack(side=tk.LEFT)
        
        self.score_label = tk.Label(self.status_frame, text="", font=("Arial", 12))
        self.score_label.pack(side=tk.LEFT, padx=20)
        
        # Display first question
        self.display_question()

        # Bind keys to navigation
        self.root.bind("<Left>", self.prev_question_key)
        self.root.bind("<Right>", self.next_question_key)
        self.root.bind("<Return>", self.check_answer_key)
        self.root.bind("<space>", self.check_answer_key)

    def load_questions(self, filename):
        try:
            # Load questions from file
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read().strip().split("\n\n")

                for block in content:
                    lines = block.strip().split("\n")

                    if not lines[0].startswith("#"):
                        continue

                    question_line = lines[1]
                    question = question_line.split(" ", 2)[2].strip()

                    mask = lines[2].strip()

                    options = []
                    answers = []

                    # Collect options and answers
                    for line in lines[3:]:
                        parts = line.split(" ", 1)
                        if len(parts) < 2:
                            continue
                        option = parts[1].strip()
                        options.append(option)

                    for i, answer in enumerate(mask):
                        if answer == "+":
                            answers.append("R")  # Correct
                        else:
                            answers.append("F")  # Incorrect

                    # Append question data
                    self.questions.append(question)
                    self.options.append(options)
                    self.answers.append(answers)

        except Exception as e:
            print(f"Error loading questions: {e}")

    def display_question(self):
        if not self.questions:
            print("No questions loaded.")
            return
        
        # Update question display
        self.question_label.config(text=self.questions[self.current_question])

        # Clear previous checkbuttons
        for cb in self.check_buttons:
            cb.destroy()
        self.check_buttons.clear()
        self.check_vars.clear()

        # Create checkbuttons for options
        for i, option in enumerate(self.options[self.current_question]):
            var = tk.IntVar()
            cb = tk.Checkbutton(self.check_frame, text=option, variable=var, font=("Arial", 12))
            cb.pack(anchor='w')
            self.check_vars.append(var)
            self.check_buttons.append(cb)
        
        # Update status label
        self.status_label.config(text=f"{self.current_question} / {len(self.questions)}")
        self.update_score()

    def check_answer(self):
        correct_answer = self.answers[self.current_question]
        correct = True
        
        # Check selected answers against the correct ones
        for i, cb in enumerate(self.check_buttons):
            if correct_answer[i] == 'R' and self.check_vars[i].get():
                cb.config(bg='lightgreen')
            elif correct_answer[i] == 'R' and not self.check_vars[i].get():
                cb.config(bg='cyan')
                correct = False
            elif correct_answer[i] == 'F' and self.check_vars[i].get():
                cb.config(bg='red')
                correct = False
            else:
                cb.config(bg='SystemButtonFace')
        
        # Track attempted questions
        if self.current_question not in self.attempted_questions:
            self.attempted_questions.add(self.current_question)
            if correct:
                self.correct_on_first_try.add(self.current_question)
        
        self.update_score()
    
    def update_score(self):
        total_attempted = len(self.attempted_questions)
        if total_attempted == 0:
            percentage = 0
        else:
            percentage = (len(self.correct_on_first_try) / total_attempted) * 100
        
        # Update score label
        self.score_label.config(text=f"{percentage:.2f}%")
        
        # Change score label color based on performance
        if percentage > 70:
            self.score_label.config(bg='lightgreen')
        else:
            self.score_label.config(bg='SystemButtonFace')
    
    def next_question(self):
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.display_question()
    
    def prev_question(self):
        if self.current_question > 0:
            self.current_question -= 1
            self.display_question()

    def prev_question_key(self, event):
        self.prev_question()

    def next_question_key(self, event):
        self.next_question()

    def check_answer_key(self, event):
        self.check_answer()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root, "questions.txt")
    root.mainloop()
