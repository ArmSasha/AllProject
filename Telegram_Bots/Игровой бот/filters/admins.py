from aiogram.dispatcher.filters import BoundFilter
#from aiogram.types import  ChatMemberRestricted
class IsBot(BoundFilter):
    async def check(self, message):
        return message.new_chat_members[-1].id == message.bot.id
"""class IsBot2(BoundFilter):
    async def check(self, message):
        bot_owner = await message.chat.get_member(user_id=message.bot.id)

        if not isinstance(bot_owner, (ChatMemberRestricted)):
            return await message.reply('👾 У бота нет админки в чате :(')
"""
class IsBot2(BoundFilter):
    async def check(self, message):
        if message.reply_to_message:
            if message.reply_to_message.from_user.id == message.bot.id:
                await message.reply(
                    f' Нельзя взаимодействовать с ботом !', parse_mode='html')
                return False
            else:
                return True
        else:
            return True
