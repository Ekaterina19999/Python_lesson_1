import requests


class YougileApi:
    def __init__(self, url, token) -> None:
        self.url = url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, title):
        project_data = {"title": title}
        url = f"{self.url}/api-v2/projects"
        resp = requests.post(url, json=project_data, headers=self.headers)
        return resp

    def update_project(self, project_id, title):
        project_data = {"title": title}
        url = f"{self.url}/api-v2/projects/{project_id}"
        resp = requests.put(url, json=project_data, headers=self.headers)
        return resp

    def get_project(self, project_id):
        url = f"{self.url}/api-v2/projects/{project_id}"
        resp = requests.get(url, headers=self.headers)
        return resp
