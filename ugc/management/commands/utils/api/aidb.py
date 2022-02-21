import sqlite3


class SQLestate:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def check_subscriber(self, tg_id):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `ugc_profile` WHERE `external_id` = ?', (tg_id,)).fetchall()
            return bool(len(result))

    #########
    def give_user_id(self, external_id):
        with self.connection:
            return self.cursor.execute('SELECT `id` FROM `ugc_profile` WHERE `external_id` = ?',
                                       (external_id,)).fetchone()

    #########

    def subscriber_exists(self):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `ugc_profile`', ).fetchall()
            return len(result)

    def add_subscriber(self, external_id):
        """Добавляем нового юзера"""
        with self.connection:
            return self.cursor.execute("INSERT INTO `ugc_profile` (`id`,`external_id`) VALUES(?,?)",
                                       (int(self.subscriber_exists()) + 1, external_id,))

    def show_all_my_station(self, external_id):
        with self.connection:
            result = self.cursor.execute('SELECT `transport_type`, `transport_number`, `station` FROM `ugc_selectedstation` WHERE `profile_id` = ?',
                                         (external_id,)).fetchall()
            return result

    def count_station(self, external_id):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `ugc_selectedstation` WHERE `profile_id` = ?',(external_id,)).fetchall()
            return len(result)

    def count_transp(self, external_id):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `ugc_selectedtransport` WHERE `profile_id` = ?',
                                         (external_id,)).fetchall()
            return len(result)


    def add_stats(self, transport_type, transport_number, station, external_id):

        with self.connection:
            return self.cursor.execute("INSERT INTO `ugc_selectedstation` (`transport_type`,`transport_number`,`station`,`profile_id`) VALUES(?, ?, ?,?)",
                                       (transport_type, transport_number, station, external_id,))

    def add_tran(self, transport_type, transport_number, external_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO `ugc_selectedtransport` (`transport_type`,`transport_number`,`profile_id`) VALUES(?,?,?)",
                                       (transport_type, transport_number, external_id,))

    def show_all_my_transport(self, external_id):
        with self.connection:
            result = self.cursor.execute('SELECT `transport_type`, `transport_number` FROM `ugc_selectedtransport` WHERE `profile_id` = ?',
                                         (external_id,)).fetchall()
            return result

    def dell_my_transport(self, external_id):
        with self.connection:
            return self.cursor.execute('DELETE FROM `ugc_selectedtransport` WHERE `profile_id` = ?',
                                       (external_id,))

    def dell_my_station(self, external_id):
        with self.connection:
            return self.cursor.execute('DELETE FROM `ugc_selectedstation` WHERE `profile_id` = ?',
                                       (external_id,))
