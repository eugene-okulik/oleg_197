import allure
import requests

from test_api_oleg_197.endpoints.endpoints import BaseAsserts


class DeleteObj:
    url = 'http://objapi.course.qa-practice.com/object/{}'

    @allure.step('Удаляем объект')
    def delete(self, post_id):
        self.response = requests.delete(self.url.format(post_id))
        BaseAsserts.assert_status_code(self.response)
        with allure.step(f'Объект {post_id} удален'):
            pass
