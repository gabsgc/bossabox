from os import name
from application.model.entity.tool import Tool
import json
from typing import List

class ToolDAO:
    def inserir(self, tool: Tool):
        tool_list = self.listarTodos()
        tool_list.append(tool)
        tool_dictList = []
        for tool in tool_list:
            tool_dictList.append(tool.toDict())
        with open('tool.json', 'w') as outfile:
            json.dump(tool_dictList, outfile)

    def listarTodos(self) -> List[Tool]:
        resultado = []
        with open('tool.json', 'r') as outfile:
            tool_dict_list = json.load(outfile)
            for tool_dict in tool_dict_list:
                id = tool_dict.get('id')
                name = tool_dict.get('name')
                link = tool_dict.get('link')
                description = tool_dict.get('description')
                tag = tool_dict.get('tag')
                tool = Tool(id, name, link, description, tag)
                resultado.append(tool)
        return resultado
        
