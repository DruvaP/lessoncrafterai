#!/usr/bin/env python
import sys
import warnings

from lessoncrafterai.crew import LessonCrafterCrew

warnings.filterwarnings("ignore", category=SyntaxWarning)

def run():
    """
    Run the LessonCrafter crew.
    """
    LessonCrafterCrew().crew().kickoff()


def train():
    """
    Train the LessonCrafter crew.
    """
    try:
        LessonCrafterCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2])
    except Exception as e:
        raise Exception(f"An error occurred during training: {e}")


def test():
    """
    Test the LessonCrafter crew.
    """
    try:
        LessonCrafterCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2])
    except Exception as e:
        raise Exception(f"An error occurred during testing: {e}")


def replay():
    """
    Replay a previous task execution.
    """
    try:
        LessonCrafterCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred during replay: {e}")


if __name__ == "__main__":
    run()
