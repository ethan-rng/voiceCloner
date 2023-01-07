from resemble import Resemble

class Session:
    def __init__(self, API_KEY="ZKWFtyOSnbpvaAi0YKQ2rgtt"):
        self.Resemble = Resemble.api_key(API_KEY)
        self.project = None

    def createProject(self, name, description="My Project"):
        is_public = False
        is_archived = False
        is_collaborative = False

        response = Resemble.v2.projects.create(name, description, is_public, is_collaborative, is_archived)
        self.project = response['item']

    def createNewVoice(self):


# https://stackoverflow.com/questions/50071841/how-to-push-local-files-to-github-using-python-or-post-a-commit-via-python
# to automate uploading to GitHub

