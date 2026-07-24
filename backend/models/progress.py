"""progress.py

Model representing student's progress across lessons and quizzes.
Fields: student_id, lesson_id, completed, score, completed_at.
"""

from datetime import datetime
from typing import Dict, Optional


class Progress:
    """Tracks a student's progress on a specific lesson or quiz.
    
    Attributes:
        student_id (int): Unique identifier for the student.
        lesson_id (int): Unique identifier for the lesson/quiz.
        completed (bool): Whether the student has completed this lesson/quiz.
        score (float): The student's score (0-100 scale).
        completed_at (Optional[datetime]): Timestamp when progress was marked complete.
    """
    
    def __init__(self, student_id: int, lesson_id: int) -> None:
        """Initialize a new Progress record.
        
        Args:
            student_id (int): Unique identifier for the student.
            lesson_id (int): Unique identifier for the lesson.
        """
        self.student_id: int = student_id
        self.lesson_id: int = lesson_id
        self.completed: bool = False
        self.score: float = 0.0
        self.completed_at: Optional[datetime] = None

    def mark_complete(self, score: float) -> None:
        """Mark the lesson/quiz as completed with a score.
        
        Args:
            score (float): The student's score.
        """
        self.completed = True
        self.score = score
        self.completed_at = datetime.now()

    def reset_progress(self) -> None:
        """Reset the progress record to incomplete state."""
        self.completed = False
        self.score = 0.0
        self.completed_at = None

    def progress_data(self) -> Dict[str, any]:
        """Export progress data as a dictionary.
        
        Returns:
            Dict[str, any]: Dictionary containing all progress information.
        """
        return {
            "student_id": self.student_id,
            "lesson_id": self.lesson_id,
            "completed": self.completed,
            "score": self.score,
            "completed_at": self.completed_at.isoformat() if self.completed_at else None
        }

    def __repr__(self) -> str:
        """Return string representation of Progress object."""
        return (f"Progress(student_id={self.student_id}, lesson_id={self.lesson_id}, "
                f"completed={self.completed}, score={self.score})")
