from bs4 import BeautifulSoup


from .web_utils import DOMAIN_NAME, get_url

ANSWER_FIRST_TEXT = "Your puzzle answer was"
BOTH_PARTS_TEXT = "Both parts of this puzzle are complete"


class Problem(dict):
    def __init__(self, year: int, day: int, data: dict = None):
        super().__init__()
        self.error = "no data"
        self.year = int(year)
        self.day = int(day)
        self.set_data(data)

    def solved(self) -> bool:
        return "solved" in self and self["solved"]

    def nb_stars(self) -> int:
        return 2 if self.solved() else len(self["answers"])

    def set_data(self, data: dict) -> None:
        self.clear()
        self.error = "no data" if data is None else None
        if self.error is None:
            for key, value in data.items():
                self[key] = value

    def download(self, cookies: str) -> None:
        self.clear()
        self.error = None

        puzzle_url = f"https://{DOMAIN_NAME}/{self.year}/day/{self.day}"
        input_url = puzzle_url + "/input"

        input_response = get_url(input_url, cookies=cookies, timeout=1.0)
        if input_response is None:
            self["aoc_personal_input"] = "Error: timeout"
        elif input_response.status_code == 200:
            self["aoc_personal_input"] = input_response.text
        else:
            self["aoc_personal_input"] = f"Error: {input_response.status_code}"

        self["answers"] = []
        problem_response = get_url(puzzle_url, cookies=cookies, timeout=1.0)
        if problem_response is None:
            self.error = "timeout"
        elif problem_response.status_code != 200:
            self.error = f"Error: {problem_response.status_code}"
        else:
            soup = BeautifulSoup(problem_response.text, "html.parser")
            main_content = soup.find("main")
            result = ['<div class="status">']
            self["solved"] = False
            for child in main_content.children:
                keep_child = False
                if child.name == "p":
                    text = child.get_text(strip=True)
                    both_parts = text.startswith(BOTH_PARTS_TEXT)
                    if both_parts:
                        self["solved"] = True
                    is_answer = text.startswith(ANSWER_FIRST_TEXT)
                    if is_answer:
                        grandchildren = [
                            grandchild.get_text(strip=True)
                            for grandchild in child.children
                        ]
                        if (
                            len(grandchildren) != 3
                            or grandchildren[0] != ANSWER_FIRST_TEXT
                            or grandchildren[2] != "."
                        ):
                            raise Exception(
                                f'cannot extract answer from string "{child}"'
                            )
                        self["answers"].append(grandchildren[1])
                    keep_child = both_parts or is_answer
                if keep_child or child.name == "article":
                    for a in child.find_all("a"):
                        a.unwrap()
                    result.append(str(child))
            if len(self["answers"]) == 0:
                result[0] += "Unsolved"
            else:
                result[0] += f'Part one: {self["answers"][0]}'
                if len(self["answers"]) > 1:
                    result[0] += f'<br>Part two: {self["answers"][1]}'
            result[0] += "</div>"
            self["html"] = "".join(result)
            self["aoc_example_inputs"] = []
            pre_content = soup.find_all("pre")
            if pre_content is not None:
                for input_example in [
                    content.get_text(strip=True) for content in pre_content
                ]:
                    if input_example not in self["aoc_example_inputs"]:
                        self["aoc_example_inputs"].append(input_example)

    def has_custom_input_with_name(self, name: str) -> bool:
        return "custom_inputs" in self and name in self["custom_inputs"]

    def add_custom_input(self, name: str, data: str) -> None:
        if self.has_custom_input_with_name(name):
            raise ValueError(f"problem already has a custom input with name '{name}'")
        if "custom_inputs" not in self:
            self["custom_inputs"] = {}
        self["custom_inputs"][name] = data

    def get_custom_input(self, name: str) -> str:
        if not self.has_custom_input_with_name(name):
            raise KeyError(f"problem doesn't have a custom input with name '{name}'")
        return self["custom_inputs"][name]
