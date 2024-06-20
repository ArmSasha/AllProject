
from main import dp
from filters.admins import IsBot

if __name__ == "filters":
    dp.filters_factory.bind(IsBot)
