from locust import HttpUser, task, between
import faker
import random


fake = faker.Faker()
sizes = ['XS', 'S', 'M', 'L', 'XL', 'AVERAGE', 'UNBELIEVABLE']


class ApiUser(HttpUser):
    host = 'http://objapi.course.qa-practice.com'
    wait_time = between(1, 3)

    def on_start(self):
        self.objects = []

    @task(3)
    def create_object(self):
        body = {
            'name': fake.name(),
            'data': {
                'color': fake.color_name(),
                'size': random.choice(sizes)
            }
        }

        with self.client.post('/object', json=body, catch_response=True) as response:
            if response.status_code == 200:
                object_id = response.json().get('id')
                if object_id:
                    self.objects.append(object_id)
                    response.success()
                else:
                    response.failure('Object ID not found in response')
            else:
                response.failure(f'Failed to create object: {response.status_code}')

    @task(2)
    def get_object(self):
        if self.objects:
            object_id = random.choice(self.objects)
            with self.client.get(f"/object/{object_id}", catch_response=True) as response:
                if response.status_code == 200:
                    response.success()
                elif response.status_code == 404:
                    self.objects.remove(object_id)
                    response.success()
                else:
                    response.failure(f'Failed to get object: {response.status_code}')

    @task(1)
    def update_object(self):
        if self.objects:
            object_id = random.choice(self.objects)

            update_name = random.choice([True, False])
            update_color = random.choice([True, False])
            update_size = random.choice([True, False])

            if not (update_name or update_color or update_size):
                update_name = True

            body = {}
            if update_name:
                body['name'] = fake.name()
            if update_color or update_size:
                body['data'] = {}

                if update_color:
                    body['data']['color'] = fake.color_name()
                if update_size:
                    body['data']['size'] = random.choice(sizes)

            with self.client.patch(f'/object/{object_id}', json=body, catch_response=True) as response:
                if response.status_code == 200:
                    response.success()
                elif response.status_code == 404:
                    self.objects.remove(object_id)
                    response.success()
                else:
                    response.failure(f'Failed to update object: {response.status_code}')

    @task(1)
    def delete_object(self):
        if self.objects:
            object_id = random.choice(self.objects)

            with self.client.delete(f"/object/{object_id}", catch_response=True) as response:
                if response.status_code == 200:
                    self.objects.remove(object_id)
                    response.success()
                elif response.status_code == 404:
                    self.objects.remove(object_id)
                    response.success()
                else:
                    response.failure(f'Failed to delete object: {response.status_code}')

    def on_stop(self):
        for object_id in self.objects[:]:
            self.client.delete(f'/object/{object_id}')
        self.objects.clear()