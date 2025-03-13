from locust import HttpUser, task, between 

class MonolithFailTest(HttpUser):
    wait_time = between(1, 3)

    @task
    def test_blocking(self):
        self.client.get("/block/")

    @task
    def test_external(self):
        self.client.get("/external/")

    @task
    def test_db(self):
        self.client.get("/db/")

    @task
    def test_memory(self):
        self.client.get("/memory-leak/")
