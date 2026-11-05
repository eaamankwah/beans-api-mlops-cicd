from locust import HttpUser, task, between

class BeansUser(HttpUser):
    wait_time = between(0.1, 0.5)

    @task
    def predict(self):
        with open("test.jpg", "rb") as f:
            self.client.post(
                "/predict",
                files={"file": ("test-image.jpg", f, "image/jpeg")},
            )