from application.model.entity.tool import Tool

class ToolDAO:
    def __init__(self):
        tool1 = Tool(1, 'Notion', 'www.notion.so', "All in one tool to organize teams and ideas. Write, plan, collaborate, and get organized.", '#organization #planning #collaboration #writing #callendar')

        self._tools = [tool1]

    def listarTodos(self):
        return self._tools