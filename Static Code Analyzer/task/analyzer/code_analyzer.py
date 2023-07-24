# write your code here
class CodeAnalyzer:
    def __init__(self, file):
        self.file = file
        self.content = self.get_lines()
        self.results = []
        self.checklist = []
        self.iltl = self.__IsLineTooLong(id="S001", message="Too Long", limit=79)
        self.checklist = self.init_checks()

    def get_lines(self):
        file_input = open(self.file, 'rt')
        with file_input:
            content = file_input.readlines()
        return content

    def init_checks(self):
        self.checklist.append(self.iltl)
        return self.checklist

    def analyze(self):
        for line_number, line_content in enumerate(self.content):
            for check in self.checklist:
                check.run_check(line_number, str(line_content))
        pass

    def __collect_results(self):
        for individual_check in self.checklist:
            self.results.append(individual_check.get_breaches())
        pass

    def show_results(self):
        self.__collect_results()
        for check in self.results:
            for result in check:
                print(f"Line {result[0]}: {result[1]} {result[2]}")

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

    class __IsLineTooLong(Check):
        def __init__(self, id, message, limit):
            self.limit = limit
            super().__init__(id, message)

        def run_check(self,line_number,line_to_analyze):
            if len(line_to_analyze) >= self.limit:
                self.add_breach(line_number, self.id, self.message)
            pass


def run_codeanalyzer():
    ca = CodeAnalyzer(input())
    #ca = CodeAnalyzer("test.txt")
    ca.analyze()
    ca.show_results()


if __name__ == "__main__":
    run_codeanalyzer()
    #  main()