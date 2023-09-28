from locust import HttpUser, task, between, SequentialTaskSet


class FindSiteTest(SequentialTaskSet):

    def on_start(self):
        self.client.verify = False

    @task
    def start_page(self):
        self.client.get("/", name=self.start_page.__name__)

    @task
    def postcode_page(self):
        self.client.get("/PostcodeSearch", name=self.postcode_page.__name__)

    @task
    def search_results_page(self):
        self.client.get("/ServiceFilter?postcode=BS14%208AT&adminarea=E06000023&latitude=51.418842&longitude=-2.554312&frompostcodesearch=True",
                        name=self.search_results_page.__name__)


class LoadTestFindSite(HttpUser):
    host = "https://www.test.find-support-for-your-family.education.gov.uk/"
    tasks = [FindSiteTest]
    wait_time = between(1, 5)
