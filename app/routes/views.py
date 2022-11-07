import datetime

import aiohttp
from aiohttp import web
# создаем функцию, которая будет отдавать html-файл
from app.routes.models import Users

async def index(request):
    return {'title': 'Оно блять работает'}


class ListUsersView(web.View):
    async def get(self):
        messages = await Users.query.order_by(Users.name.desc()).gino.all()
        messages_data = []
        for message in messages:
            messages_data.append(
                {
                    "name": messages.name,
                    "surname": messages.tex,
                    "password": messages.password,
                    "phone_number":messages.phone_number,
                    "job_title":messages.job_title,
                    "text": message.text,

                    "created": str(message.created),
                }
            )
        return web.json_response(data={'messages': messages_data})

class CreateMessageView(web.View):
    async def post(self):
        data = await self.request.json()
        message = await self.request.app["db"].message.create(
            text=data['text'],
            created=datetime.now(),
        )
        return web.json_response(data={'message': {
            'id': message.id,
            'text': message.text,
            'created': str(message.created),
        }})
