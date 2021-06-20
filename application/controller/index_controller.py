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
    id = len(tool_list) + 1
    name = request.form.get("name", None)
    link = request.form.get("link", None)
    description = request.form.get("description", None)
    tag = request.form.get("tag", None)
    tool = Tool(id, name, link, description, tag)
    ToolDAO().inserir(tool)
    tool_list.append(tool)
    return render_template("tool.html", tool_list= tool_list)

@app.route("/excluir/<int:id>", methods=['DELETE'])
def excluir(id: int):
    for tool in tool_list:
        if id == tool._id:
            ToolDAO().excluir(tool, tool._id)
            tool_list.remove(tool)
            return render_template("tool.html", tool_list = tool_list)
    return render_template("tool.html", tool_list = tool_list), 404

@app.route("/busca", methods=['GET'])
def busca():
    tool_list_pesquisa = []
    search = request.args.get('search')
    for tool in tool_list:
        if search in tool._name or search in tool._description:
            tool_list_pesquisa.append(tool)
    return render_template("tool.html", tool_list = tool_list_pesquisa)


@app.route("/buscar", methods=['GET'])
def buscar():
    tool_list_tag = []
    search_tag = request.args.get('search')
    for tool in tool_list:
        tag = tool._tag.replace('#', '')
        if search_tag == tag:
            tool_list_tag.append(tool)
    return render_template("tool.html", tool_list= tool_list_tag)