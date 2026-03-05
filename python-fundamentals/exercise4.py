class Deployment:
    """
    Manages the state and version history of a software deployment.
    """

    def __init__(self, service_name: str, environment: str):
        self.service_name = service_name
        self.environment = environment
        self.status = 'pending'
        self.current_version = None
        # history will store previous versions to allow rollbacks
        self.history = []

    def deploy(self, new_version: str):
        # If we have a current version, move it to history before updating
        if self.current_version is not None:
            self.history.append(self.current_version)
        
        self.current_version = new_version
        self.status = 'deployed'

    def rollback(self) -> bool:
        # Check if there is a version to roll back to
        if not self.history:
            return False
        
        # Pop the last version from history and make it current
        self.current_version = self.history.pop()
        self.status = 'rolled_back'
        return True

    def check_status(self) -> dict:
        return {
            'service_name': self.service_name,
            'environment': self.environment,
            'status': self.status,
            'version': self.current_version
        }