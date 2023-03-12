class ActionBaseIO:
    def __init__(self) -> None:
        pass

    def _sugest_action_on_files(self, question: str, files: list) -> None:
        print(question)
        for file in files:
            print(file.file_path)
        print("Y/N?")

    def _has_user_accepted_the_action(self) -> bool:
        user_answer = input()
        if user_answer in ("y", "Y"):
            return True
        elif user_answer in ("n", "N"):
            return False
        else:
            print("Invalid option. Aborting the script...")
            exit(1)
