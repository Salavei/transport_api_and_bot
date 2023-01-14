import os
import psycopg2


class SQLestate:

    def __init__(self):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = psycopg2.connect(host=os.environ.get('DB_HOST'), database=os.environ.get('DB_NAME'),
                                           user=os.environ.get('DB_USER'), password=os.environ.get('DB_PASS'))

        self.cursor = self.connection.cursor()

    def check_subscriber(self, tg_id):
        """Проверяем, есть ли уже юзер в базе"""
        self.cursor.execute("SELECT * FROM bot_app_profile WHERE external_id = %s", (tg_id,))
        result = self.cursor.fetchone()
        return result is not None

    def give_user_id(self, external_id):
        self.cursor.execute("SELECT id FROM bot_app_profile WHERE external_id = 815021893", (external_id,))
        return self.cursor.fetchone()

    def subscriber_exists(self):
        self.cursor.execute("SELECT * FROM bot_app_profile", )
        return len(self.cursor.fetchall())

    def add_subscriber(self, external_id):
        """Добавляем нового юзера"""
        with self.connection:
            self.cursor.execute("INSERT INTO bot_app_profile (id, external_id) VALUES(%s, %s)",
                                (int(self.subscriber_exists()) + 1, external_id,))
            return self.cursor

    def count_station(self, external_id):
        with self.connection:
            self.cursor.execute('SELECT * FROM bot_app_selectedstation WHERE profile_id = %s',(external_id,))
            return len(self.cursor.fetchall())

    def count_transp(self, external_id):
        with self.connection:
            self.cursor.execute('SELECT * FROM bot_app_selectedtransport WHERE profile_id = %s',
                                         (external_id,))
            return len(self.cursor.fetchall())

    def add_stats(self, transport_type, transport_number, station, external_id):
        with self.connection:
            return self.cursor.execute(
                "INSERT INTO bot_app_selectedstation (transport_type,transport_number, station, profile_id) VALUES(%s, %s, %s, %s)",
                (transport_type, transport_number, station, external_id,))

    def add_tran(self, transport_type, transport_number, external_id):
        with self.connection:
            return self.cursor.execute(
                "INSERT INTO bot_app_selectedtransport (transport_type, transport_number, profile_id) VALUES(%s, %s, %s)",
                (transport_type, transport_number, external_id,))

    def show_all_my_station(self, external_id):
        with self.connection:
            self.cursor.execute(
                'SELECT transport_type, transport_number, station FROM bot_app_selectedstation WHERE profile_id = %s',
                (external_id,))
            return self.cursor.fetchall()

    def show_all_my_transport(self, external_id):
        with self.connection:
            self.cursor.execute(
                'SELECT transport_type, transport_number FROM bot_app_selectedtransport WHERE profile_id = %s',
                (external_id,))
            return self.cursor.fetchall()

    def dell_my_transport(self, external_id):
        with self.connection:

            self.cursor.execute('SELECT id FROM bot_app_selectedtransport WHERE profile_id = %s ORDER BY id',
                                (external_id,))
            take_id = self.cursor.fetchone()[0]
            self.cursor.execute(
            'SELECT transport_type, transport_number FROM bot_app_selectedtransport WHERE id = %s',
            (take_id,))
            result = self.cursor.fetchall()
            self.cursor.execute('DELETE FROM bot_app_selectedtransport WHERE profile_id = %s and id  = %s',
                            (external_id, take_id,))
            return result

    def dell_my_station(self, external_id):
        with self.connection:
            self.cursor.execute('SELECT id FROM bot_app_selectedstation WHERE profile_id = %s ORDER BY id',
                                    (external_id,))

            take_id = self.cursor.fetchone()[0]
            self.cursor.execute(
                'SELECT transport_type, transport_number, station FROM bot_app_selectedstation WHERE id = %s',
                (take_id,))
            result = self.cursor.fetchall()
            self.cursor.execute('DELETE FROM bot_app_selectedstation WHERE profile_id = %s and id  = %s',
                                (external_id, take_id,))
            return result
