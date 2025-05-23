#To install requirements run below command
pip install -r requirements.txt

#To check locust version
locust --version

#To upgrade pip run below command
python.exe -m pip install --upgrade pip

#To know some commands to be used in locust
locust --help

#To run the locust tests in ui run below command
locust -f .\locustfile.py --web-port 8090

#To run the locust tests in headless mode run below command
locust -f locustfile.py --headless -u 10 -r 1 --run-time 30s

#To ignore particular directory for commit
git rm -r  reports/   

#


**Locust Documentation**

**What is Locust?**
Locust is an open source performance/load testing tool for HTTP and other protocols. Its developer-friendly approach lets you define your tests in regular Python code.
Locust tests can be run from command line or using its web-based UI. Throughput, response times and errors can be viewed in real time and/or exported for later analysis.
You can import regular Python libraries into your tests, and with Locust’s pluggable architecture it is infinitely expandable. Unlike when using most other tools, your test design will never be limited by a GUI or domain-specific language.

**Features**

**Write test scenarios in plain old Python**
If you want your users to loop, perform some conditional behavior or do some calculations, you just use the regular programming constructs provided by Python. Locust runs every user inside its own greenlet (a lightweight process/coroutine). This enables you to write your tests like normal (blocking) Python code instead of having to use callbacks or some other mechanism. 
Distributed and scalable - supports hundreds of thousands of concurrent users
Locust makes it easy to run load tests distributed over multiple machines. It is event-based (using gevent), which makes it possible for a single process to handle many thousands concurrent users.

**Web-based UI**
Locust has a user friendly web interface that shows the progress of your test in real-time. You can even change the load while the test is running. It can also be run without the UI, making it easy to use for CI/CD testing.

**Can test any system**
Even though Locust primarily works with websites/services, it can be used to test almost any system or protocol. Just write a client for what you want to test, or explore some created by the community.

**Hackable**
Locust is small and very flexible and we intend to keep it that way. If you want to send reporting data to that database & graphing system you like, wrap calls to a REST API to handle the particulars of your system.

**Locust Classes**


1. ✅ User class
Base class for all user behavior in Locust.
Can be used for non-HTTP protocols (like gRPC, TCP, WebSocket).
from locust import User
class CustomUser(User):
    def run(self):
        # custom protocol simulation login
pass

2. ✅ HttpUser class
A subclass of User designed specifically for HTTP load testing.
Provides an HTTP client via self.client.
from locust import HttpUser, task, between
class WebUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_home(self):
        self.client.get("/")

3. ✅ TaskSet
A set of related tasks.
Allows grouping actions into reusable workflows.
from locust import TaskSet, task
class CommonActions(TaskSet):
    @task
    def get_about(self):
        self.client.get("/about")

4. ✅ SequentialTaskSet
Runs tasks in order, unlike TaskSet, which runs them randomly.

from locust import SequentialTaskSet, task
class LoginFlow(SequentialTaskSet):
    @task
    def open_login(self):
        self.client.get("/login")

    @task
    def do_login(self):
        self.client.post("/login", {"username": "admin", "password": "admin"})

5. ✅ HttpSession
The self.client in HttpUser is an HttpSession.
Maintains cookies and session state across requests.
response = self.client.get("/dashboard")

6. ✅ Response
Object returned by HTTP calls.
Contains status_code, text, json(), etc.
response = self.client.get("/api/users")
print(response.status_code, response.json())

7. ✅ Response Context Manager
Used for manual control over request success/failure.
with self.client.get("/login", catch_response=True) as response:
    if "Welcome" in response.text:
        response.success()
    else:
        response.failure("Login failed")

8. ✅ Environment
Holds Locust test environment: user classes, runner, stats, etc.
Used for programmatic test execution.
from locust.env import Environment
env = Environment(user_classes=[WebUser])

9. ✅ Runner
Responsible for starting/stopping users, collecting stats.
Accessible via env.runner.
runner = env.create_local_runner()
runner.start(user_count=10, spawn_rate=1)

10. ✅ Web UI
Locust’s optional web interface (usually runs on http://localhost:8089).
Can start tests, set user count, spawn rate, see charts/stats.
locust -f locustfile.py

**Project Structure:-**

orangehrm_locust_test/
│
├── locustfile.py               # Entry point for Locust tests
├── requirements.txt            # Project dependencies
├── README.md                   # Optional: project overview
│
├── config/
│   └── settings.py             # Configuration like host URL, wait times
│
├── locust_tasks/
│   └── orangehrm_tasks.py      # TaskSet logic for OrangeHRM
│
└── utils/
    └── helpers.py              # Future helper methods (e.g., token parsing)











