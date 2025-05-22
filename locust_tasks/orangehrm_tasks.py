from locust import SequentialTaskSet, task

class OrangeHRMTasks(SequentialTaskSet):
    def on_start(self):
        print("Starting login sequence...")
        self.login()

    def login(self):
        response = self.client.get("/web/index.php/auth/login", name="Open Login Page")
        payload = {
            "username": "Admin",
            "password": "admin123"
        }
        if response.status_code == 200:
            print("Login page loaded.")
        else:
            print("Failed to load login page.")
        self.client.get("/web/index.php/dashboard/index", name="Open Dashboard")

    @task
    def load_dashboard(self):
        with self.client.get("/web/index.php/dashboard/index", name="Load Dashboard", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
                print("Dashboard loaded successfully.")
            else:
                response.failure("Failed to load dashboard.")

    @task
    def view_admin_users(self):
        with self.client.get("/web/index.php/admin/viewSystemUsers", name="View Admin Users", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
                print("Admin > User Management page loaded.")
            else:
                response.failure("Failed to load Admin > User Management page.")

    def on_stop(self):
        print("Logging off the test ...")

