from application.model.dao.tool_dao import ToolDAO
from application import app
from flask import render_template, request
from application.model.entity.tool import Tool

tool_list = ToolDAO().listarTodos()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', tool_list = tool_list)

@app.route('/list', methods=['GET'])
def listatool():
    return render_template('tool.html', tool_list = tool_list)

@app.route('/inserir', methods=['POST'])
def inserir():
    name = request.form.get('name')
    link = request.form.get('link')
    description = request.form.get('description')
    tag = request.form.get('tag')
    id = len(tool_list) + 1
    tool = Tool(id, name, link, description, tag)
    ToolDAO().inserir(tool)
    tool_list.append(tool)
    return render_template("tool.html", tool_list= tool_list)

@app.route("/excluir/<int:id>", methods=['DELETE'])
def excluir(id: int):
    for tool in tool_list:
        if tool._id == id:
            tool_list.remove(tool)
            return render_template("tool.html", tool_list = tool_list)
    return render_template("tool.html", tool_list = tool_list), 404