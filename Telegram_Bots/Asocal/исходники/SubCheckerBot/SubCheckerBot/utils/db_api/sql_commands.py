from utils.db_api.schemas.user import Groups


async def add_group(chat_id: int, group_id: int, group_name: str, group_link: str):
    seller = Groups(
        chat_id=chat_id,
        group_id=group_id,
        group_name=group_name,
        group_link=group_link
    )
    await seller.create()


async def select_group(chat_id: int):
    groups = await Groups.query.where(Groups.chat_id == chat_id).gino.all()
    list_ = list()
    for group in groups:
        dict_ = {}
        dict_.update(
            {'chat_id': group.chat_id,
             'group_id': group.group_id,
             'group_name': group.group_name,
             'group_link': group.group_link}
        )
        list_.append(dict_)
    return list_


async def delete_all_groups(chat_id: int):
    for group in await Groups.query.where(Groups.chat_id == chat_id).gino.all():
        await group.delete()
