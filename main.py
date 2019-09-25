from apidata import requester, cleaner
from dbmanagement import models, managers


def fetch_and_clean():
    apifetch = requester.RequestData
    dataclean = cleaner.Cleaner
    apifetch.fetch_category()
    apifetch.fetch_products()

    dataclean.filter_product()


