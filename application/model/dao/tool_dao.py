from application.model.entity.tool import Tool
import json
import os
from typing import List

class ToolDAO:
    def inserir(self, tool: Tool):
        tool_list = self.listarTodos()
        tool._id = len(tool_list) + 1
        tool_list.append(tool)
        tool_dictList = []
        for tool in tool_list:
            tool_dictList.append(tool.toDict())
        with open('tool.json', 'w') as file:
            json.dump(tool_dictList, file)

    def listarTodos(self) -> List[Tool]:
        resultado = []
        with open('tool.json', 'r') as file:
            tool_dict_list = json.load(file)
            for tool_dict in tool_dict_list:
                id = tool_dict.get("id", None)
                name = tool_dict.get("name", None)
                link = tool_dict.get("link", None)
                description = tool_dict.get("description", None)
                tag = tool_dict.get("tag", None)
                tool = Tool(id, name, link, description, tag)
                resultado.append(tool)
        return resultado

    def excluir(self, tool: Tool, id: int):
        file = json.load(open('tool.json'))
        for i in range(len(file)):
            if file[i]["id"] == tool._id:
                file.pop(i)
                break
        
        tempfile = 'update-file.json'
        open(tempfile, 'w').write(
            json.dumps(file, sort_keys=True, indent=4, separators=(',', ': '))
        )
        os.remove('tool.json')
        os.rename(tempfile, 'tool.json')