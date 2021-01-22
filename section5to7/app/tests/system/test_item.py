from models.store import StoreModel
from models.user import UserModel
from models.item import ItemModel
from tests.base_test import BaseTest
import json


class TestItem(BaseTest):
    def test_get_item_no_auth(self):
        with self.app() as client:
            with self.app_context():
                response = client.get('/item/test')
                self.assertEqual(response.status_code, 401)


    def test_get_item_not_found(self):
        with self.app() as client:
            with self.app_context():
                UserModel('test', '1234').save_to_db()
                auth_request = client.post('/auth',
                                           data=json.dumps({'username': 'test', 'password': '1234'}),
                                           headers={'Content-Type': 'application/json'})
                auth_token = json.loads(auth_request.data)['access_token']
                header = {'Authorization': 'JWT ' + auth_token}

                response = client.get('/item/test', headers=header)
                self.assertEqual(response.status_code, 404)

    def test_get_item(self):
        pass

    def test_delete_item(self):
        pass

    def test_create_item(self):
        pass

    def test_create_duplicate_item(self):
        pass

    def test_put_item(self):
        pass

    def test_put_update_item_(self):
        pass

    def test_item_list(self):
        pass
