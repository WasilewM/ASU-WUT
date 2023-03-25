from enum import Enum


class UserActionAnswerEnum(Enum):
    NO = 0
    YES = 1
    APPLY_TO_ALL = 2


class ActionBaseIO:
    def __init__(self) -> None:
        pass

    def _sugest_action_on_files(self, question: str, file_path: str) -> None:
        print(question)
        print(file_path)
        print("Y/N/ALL?")

    def _has_user_accepted_the_action(self) -> UserActionAnswerEnum:
        user_answer = input()
        print(user_answer)
        if user_answer.upper() == "N":
            return UserActionAnswerEnum.NO
        elif user_answer.upper() == "Y":
            return UserActionAnswerEnum.YES
        elif user_answer.upper() == "ALL":
            return UserActionAnswerEnum.APPLY_TO_ALL
        else:
            print("Invalid option. Aborting the script...")
            exit(1)
