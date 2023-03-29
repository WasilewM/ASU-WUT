from enum import Enum
from .files_data_collector import FileData


class UserActionAnswerEnum(Enum):
    NO = 0
    YES = 1
    APPLY_TO_ALL = 2


class ActionBase:
    def __init__(self) -> None:
        self.apply_action_to_all = False

    def run(self, files: list) -> None:
        for file in files:
            if not self.apply_action_to_all:
                self._handle_individual_file(file)
            else:
                self._execute_action(file)

    def _handle_individual_file(self, file: FileData):
        self._ask_for_user_decision(file)
        user_answer = self._has_user_accepted_the_action()
        if user_answer == UserActionAnswerEnum.YES:
            self._execute_action(file)
        elif user_answer == UserActionAnswerEnum.APPLY_TO_ALL:
            self.apply_action_to_all = True
            self._execute_action(file)

    def _ask_for_user_decision(self, file):
        print("Implement me!")
        exit(1)

    def _execute_action(self, file: FileData):
        print("Implement me!")
        exit(1)

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
