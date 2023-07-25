import os
import glob
import argparse


class CodeAnalyzer:
    def __init__(self, file):
        self.file = file
        self.content = self.get_lines()
        self.results = []
        self.ck_s001 = self.__IsLineTooLong(id="S001", message="Too Long", limit=79)
        self.ck_s002 = self.__IndentationIsNotFour(id="S002", message="Indentation is not a multiple of four", limit=4)
        self.ck_s003 = self.__EndingSemicolon(id="S003", message="Unnecessary semicolon after a statement")
        self.ck_s004 = self.__NoTwoSpaces(id="S004", message="Less than two spaces before inline comments")
        self.ck_s005 = self.__TODO(id="S005", message="TODO found")
        self.ck_s006 = self.__TwoBlankLines(id="S006", message="More than two blank lines preceding a code line")
        self.checklist = {k: v for k, v in self.__dict__.items() if k.startswith("ck_")}

    def get_lines(self):
        file_input = open(self.file, 'rt')
        with file_input:
            content = file_input.readlines()
        return content

    def analyze(self):
        for name, check_obj in self.checklist.items():
            if check_obj.by_line_check():
                for line_number, line_content in enumerate(self.content, start=1):
                    check_obj.run_check(line_number, str(line_content))
            else:
                check_obj.run_check(self.content)

    def __collect_results(self):
        for name, check_obj in self.checklist.items():
            self.results.append(check_obj.get_breaches())
        pass

    def show_results(self):
        self.__collect_results()
        result_output = []
        for check in self.results:
            for result in check:
                result_output.append(result)
        result_output.sort(key=lambda x: (x[0], x[1]))
        for line, check, message in result_output:
            print(f"{self.file}: Line {line}: {check} {message}")

    class Check:
        def __init__(self, id: str, message: str, check_by_line: bool):
            self.id = id
            self.message = message
            self.results = []
            self.check_by_line = check_by_line

        def add_breach(self, line_number: int, id: str, message: str):
            self.results.append([line_number, id, message])
            pass

        def get_breaches(self):
            return self.results

        def by_line_check(self):
            return self.check_by_line

        def is_comment_line(self, line_to_analyze):
            if "#" in line_to_analyze:
                return True
            return False

    class __IsLineTooLong(Check):
        def __init__(self, id, message, limit):
            self.limit = limit
            super().__init__(id, message, check_by_line=True)

        def run_check(self, line_number, line_to_analyze):
            if len(line_to_analyze) > self.limit:
                self.add_breach(line_number, self.id, self.message)
            pass

    class __IndentationIsNotFour(Check):
        def __init__(self, id, message, limit):
            self.limit = limit
            super().__init__(id, message, check_by_line=True)

        def run_check(self, line_number, line_to_analyze):
            if (line_to_analyze != "\n") \
                    and \
                    ((len(line_to_analyze) - len(line_to_analyze.lstrip())) % self.limit != 0):
                self.add_breach(line_number, self.id, self.message)
            pass

    class __EndingSemicolon(Check):
        def __init__(self, id, message):
            super().__init__(id, message, check_by_line=True)

        def run_check(self, line_number, line_to_analyze):
            if line_to_analyze != "\n":
                stripped_line_to_analyze = line_to_analyze.split('#')[0].rstrip()
                try:
                    if stripped_line_to_analyze[-1] == ";":
                        self.add_breach(line_number, self.id, self.message)
                except Exception as e:
                    pass
            pass

    class __NoTwoSpaces(Check):
        def __init__(self, id, message):
            super().__init__(id, message, check_by_line=True)

        def run_check(self, line_number, line_to_analyze):
            stripped_line_to_analyze = line_to_analyze.lstrip().rstrip()
            if stripped_line_to_analyze != "\n":
                if self.is_comment_line(stripped_line_to_analyze):
                    if (stripped_line_to_analyze[0] == "#") or ("  #" in stripped_line_to_analyze):
                        pass
                    else:
                        self.add_breach(line_number, self.id, self.message)
                else:
                    pass
            pass

    class __TODO(Check):
        def __init__(self, id, message):
            super().__init__(id, message, check_by_line=True)

        def run_check(self, line_number, line_to_analyze):
            if "# TODO" in line_to_analyze.upper():
                self.add_breach(line_number, self.id, self.message)
            else:
                pass

    class __TwoBlankLines(Check):
        def __init__(self, id, message):
            super().__init__(id, message, check_by_line=False)

        def run_check(self, content):
            count = 0
            for line_number, line_content in enumerate(content, start=1):
                if line_content == '\n':
                    count += 1
                else:
                    if count > 2:
                        self.add_breach(line_number, self.id, self.message)
                        count = 0
            pass


def set_argparse() -> argparse:
    parser = argparse.ArgumentParser(description="This program checks python codes.")
#    parser.add_argument("-f",
#                        "--filepath",
#                        help="enter a file or a path with python files"
#                        , default="C:\\Users\\Bernhard\\PycharmProjects\\Static Code Analyzer"
#                                "\\Static Code Analyzer\\task\\test"
#                       )
    parser.add_argument("filepath")
    return parser


def get_argparse():
    parser = set_argparse()
    args = parser.parse_args()
    return args.filepath


def get_files(filepath: str) -> list:
    py_files = []
    if filepath is not None:
        if os.path.isdir(filepath):
            # If filepath is a directory, find all '.py' files in this directory (recursively)
            py_files.extend(glob.glob(f"{filepath}/**/*.py", recursive=True))
        elif os.path.isfile(filepath) and filepath.endswith('.py'):
            # If filepath is a file ending with '.py', add it to the list
            py_files.append(filepath)
    else:
        py_files = None
    return py_files


def run_codeanalyzer(filepath: str):
    py_file_list = get_files(filepath)
    if py_file_list is not None:
        for py_file in py_file_list:
            ca = CodeAnalyzer(py_file)
            ca.analyze()
            ca.show_results()


if __name__ == "__main__":
    run_codeanalyzer(get_argparse())
