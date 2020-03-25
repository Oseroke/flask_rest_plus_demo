from flask import request
from flask_restplus import Api, Resource, fields
#from flask_restplus import Resource

api = Api(version="0.1", title="My first API with Flask_restplus", description="A simple demonstration of a Flask RestPlus powered API")

ns = api.namespace('tasks', description='Operations related to tasks')

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

task = api.model('Tasks', {
    'title': fields.String(required=True, description='Task Title'),
    'description': fields.String(required=True, description='Task Description'),
    'done': fields.Boolean
})

@ns.route('/')
class TaskList(Resource):

    def get(self):
        """
        Returns list of tasks
        """
        return tasks

    @api.expect(task)
    @api.response(201, "Task list successfully created")
    def post(self):
        """
        create new task list
        """
        data = request.json
        title = data['title']
        desc = data.get('description', "")
        done = data['done']
        task = {
                "id": tasks[-1]['id']+1, 
                "title": title,
                "description": desc,
                "done": done 
                }
        tasks.append(task)
        return None, 201
    
@ns.route('/<int:id>')
@api.response(404, 'Task not found')
class Task(Resource):

    def get(self, id):
        """
        Returns task
        """
        task = tasks[id]
        return task
    
    # @api.response(201, "Task successfully added")
    # def post(self):
    #     """
    #     create new task
    #     """
    #     data = request.json
    #     tasks.append(data)
    #     return None, 201
    
    @api.response(204, "Task succesfully updated")
    def put(self, id):
        """
        Update existing task
        """
        data = request.json
        task = tasks[data.id]
        task.title = data.title
        task.description = data.description
        task.done = data.done
        tasks.append(task)
        return None, 204




