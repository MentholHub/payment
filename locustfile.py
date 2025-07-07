from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    host = "http://localhost:8000/"  # Указываем адрес API
    wait_time = between(1, 3)  # Пауза между запросами

    @task
    def get_index(self):
        self.client.get("/")
