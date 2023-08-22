from core import Core


class Author:
    patch = "author/"
    file_patch = "author/files"
    terminal_session = None

    def __init__(self, terminal_session):
        self.terminal_session = terminal_session
        pass

    def run_author_settings_pack(self):
        core = Core(self.terminal_session, self.patch)
        core.work_with_package()
        core.work_with_command((self.patch + "/command_list_after_copy.txt"))


class Minimal:
    patch = "minimal/"
    file_patch = None
    terminal_session = None

    def __init__(self, terminal_session):
        self.terminal_session = terminal_session
        pass

    def run_minimal_settings_pack(self):
        core = Core(self.terminal_session, self.patch)
        core.work_with_package()
        core.work_with_command((self.patch + "/command_list.txt"))




