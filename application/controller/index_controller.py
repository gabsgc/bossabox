from application.model.dao.tool_dao import ToolDAO
from application import app
from flask import render_template, request
from application.model.entity.tool import Tool
import time

tool_list = ToolDAO().listarTodos()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', tool_list = tool_list)

@app.route('/list', methods=['GET'])
def listatool():
    return render_template('tool.html', tool_list = tool_list)

@app.route('/inserir', methods=['POST'])
def inserir():
    time.sleep(10)
    name = request.form.get('name', None)
    link = request.form.get('link', None)
    description = request.form.get('description', None)
    tag = request.form.get('tags', None)
    id = len(tool_list) + 1
    tool = Tool(id, name, link, description, tag)
    tool_list.append(tool)
    return render_template("tool.html", tool_list = tool_list)



