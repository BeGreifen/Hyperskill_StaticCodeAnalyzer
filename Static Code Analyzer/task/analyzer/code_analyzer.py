class CodeAnalyzer:
    def __init__(self, file):
        self.file = file
        self.content = self.get_lines()
        self.results = []
        self.checklist = []
        self.ck_s001 = self.__IsLineTooLong(id="S001", message="Too Long", limit=79)
        self.ck_s002 = self.__IndentationIsNotFour(id="S002", message="Indentation is not a multiple of four", limit=4)
        self.checklist = self.init_checks()

    def get_lines(self):
        file_input = open(self.file, 'rt')
        with file_input:
            content = file_input.readlines()
        return content

    def init_checks(self):
        self.checklist = {k: v for k, v in self.__dict__.items() if k.startswith("ck_")}
        return self.checklist

    def analyze(self):
        for line_number, line_content in enumerate(self.content, start=1):
            for name, check_obj in self.checklist.items():
                check_obj.run_check(line_number, str(line_content))
        pass

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
            print(f"Line {line}: {check} {message}")

    class Check:
        def __init__(self, id: str, message: str):
            self.id = id
            self.message = message
            self.results = []

        def add_breach(self, line_number: int,  id: str, message: str):
            self.results.append([line_number, id, message])
            pass

        def get_breaches(self):
            return self.results

        def is_comment_line(self,line_to_analyze):
            if "#" in line_to_analyze:
                return True
            return False

    class __IsLineTooLong(Check):
        def __init__(self, id, message, limit):
            self.limit = limit
            super().__init__(id, message)

        def run_check(self,line_number,line_to_analyze):
            if len(line_to_analyze) >= self.limit:
                self.add_breach(line_number, self.id, self.message)
            pass

    class __IndentationIsNotFour(Check):
        def __init__(self, id, message, limit):
            self.limit = limit
            super().__init__(id, message)

        def run_check(self, line_number, line_to_analyze):
            if (len(line_to_analyze) - len(line_to_analyze.lstrip())) % self.limit != 0:
                self.add_breach(line_number, self.id, self.message)
            pass

def run_codeanalyzer():
    ca = CodeAnalyzer(input())
    #ca = CodeAnalyzer("test.txt")
    ca.analyze()
    ca.show_results()


if __name__ == "__main__":
    run_codeanalyzer()

