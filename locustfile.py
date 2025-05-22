from locust import HttpUser
from config.settings import BASE_URL, WAIT_TIME
from locust_tasks.orangehrm_tasks import OrangeHRMTasks

class OrangeHRMUser(HttpUser):
    wait_time = WAIT_TIME
    host = BASE_URL
    tasks = [OrangeHRMTasks]
