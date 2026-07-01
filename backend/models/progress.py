"""progress.py
Model representing student's progress across lessons and quizzes. Fields: student_id, progress_data.
"""
#progress.py

class Progress:
    def __init__(self,student_id,lesson_id):
        self.student_id=student_id
        self.lesson_id=lesson_id
        self.completed=False
        self.score=0
        
    def mark_complete(self,score):
        self.completed=True
        self.score=score

    def progress_data(self):
        return{
            "student_id":self.student_id,
            "completed":self.completed,
            "score":self.score
        }        