import time
from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1,5)

    @task
    def successful_user_journey(self):
        testName = "Successful user Journey:"
        self.client.get(url="", name=testName + "home")
        self.client.get(url="/PostcodeSearch", name=testName + "PostcodeSearch page") #Important, only perform a get against this endpoint. Posting to it will put a load on external postcode provider
        searchResponse = self.client.get(url="/ServiceFilter?postcode=M27%200AA&adminDistrict=E08000006&latitude=53.505234&longitude=-2.346582", name=testName + "ServiceFilter page (postcode results)")
        print(dict(searchResponse.cookies))

    def on_start(self):
        self.client.verify = False

    def verify_host_url(self):
        lastChar = self.client.user.client.base_url[-1]
        if lastChar != "/":
            self.client.user.client.base_url += "/" 
