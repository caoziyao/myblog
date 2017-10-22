# coding: utf-8

from .db_manager import DBManager
from app.untils import log
from app.database.cache import redis_client


class BaseModel(object):
    def __init__(self, table_name):
        self._table_name = table_name
        self._members = {}
        self._column = []
        self._manager = DBManager()

    def load_members(self, except_column=None):
        """
        加载数据库字段
        except_column: 期望的字段
        :return:
        """
        manager = self._manager
        table_name = self._table_name
        sql = 'SHOW COLUMNS FROM {}'.format(table_name)

        columns = manager.query(sql)
        for col in columns:
            field = col['Field']
            if except_column is None or field not in except_column:
                default = col['Default']
                self._members[field] = default
        return True

    def add_data(self, keyword):
        """
        添加数据到数据库
        :param keyword:
        :return:
        """
        manager = self._manager
        members = self._members.copy()
        table = self._table_name

        self._members[keyword] = manager.insert(table, data=members)

        if self._members[keyword] is not None:
            return True
        else:
            return False

    def update_data(self):
        """
        更新数据库数据
        :return:
        """
        manager = self._manager
        table = self._table_name
        cond = {
            'id': self.members['id'],
        }
        result = manager.update(table, data=self.members, condition=cond)
        return True if result else False


    def load_data(self, fields=None, condition=None, order=None, limit=None, fetchone=True):
        """
        加载多条数据
        :param query: 不指定 query 字段, 将返回所有*字段
        :param condition: 不指定 condition 字段, 将条件 where = 1
        :param order_by: 不指定 order, 将不进行排序
        :param fetchone:  不指定 fetchone, 将返回多条数据
        :param limit:  不指定 limit, 返回全部数据
        :return:
        """
        # r = redis_client
        # if condition and 'id' in condition:
        #     log('load cached')
        #     _id = condition['id']
        #     key = '{}:{}'.format(self._table_name, _id)
        #     if r.exists(key):
        #         return r.get(key)

        manager = self._manager
        table = self._table_name
        column = manager.fetch_rows(table, fields=fields, condition=condition, order=order, limit=limit, fetchone=fetchone)
        if column:
            if fetchone:
                self._column.append(column)
                for key in column:
                    self._members[key] = column[key]
            else:
                self._column = column
            return True
        return False

    @property
    def column(self):
        """
        取得数据列表
        :return:
        """
        return self._column

    @property
    def members(self):
        """
        取得数据字典
        :return:
        """
        return self._members

    def __getattr__(self, item):
        """
        以类属性的方式访问数据字典
        :param item:
        :return:
        """
        if item in self._members:
            return self._members[item]
        return None
