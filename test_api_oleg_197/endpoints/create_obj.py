import allure


from test_api_oleg_197.endpoints.endpoints import BaseApi


class CreateObj(BaseApi):
    url = 'http://objapi.course.qa-practice.com/object'

    @allure.step('Создаём объект')
    def create(self):
        return self.create_base()

    @allure.step('Создаём объект с именем {name}')
    def create_with_name(self, name):
        return self.create_base(name=name)
