class Deployment:
    """
    Manages the state and version history of a software deployment.
    """

    def __init__(self, service_name: str, environment: str):
        """
        Initializes a new Deployment instance with strict type and value checking.
        """
        # Validate service_name
        if not isinstance(service_name, str):
            raise TypeError(f"service_name must be a string, not {type(service_name).__name__}")
        if not service_name.strip():
            raise ValueError("service_name cannot be an empty string")

        # Validate environment
        if not isinstance(environment, str):
            raise TypeError(f"environment must be a string, not {type(environment).__name__}")
        if not environment.strip():
            raise ValueError("environment cannot be an empty string")

        self.service_name = service_name
        self.environment = environment
        self.status = 'pending'
        self._history = []

    def deploy(self, new_version: str):
        """
        Deploys a new version by adding it to the history after validation.
        """
        # Validate new_version
        if not isinstance(new_version, str):
            raise TypeError(f"new_version must be a string, not {type(new_version).__name__}")
        if not new_version.strip():
            raise ValueError("new_version cannot be an empty string")

        self._history.append(new_version)
        self.status = 'deployed'

    def rollback(self) -> bool:
        """
        Rolls back to the previous version by removing the current one from history.
        """
        if len(self._history) < 2:
            return False
        
        self._history.pop()
        self.status = 'rolled_back'
        return True

    def check_status(self) -> dict:
        """
        Returns a dictionary representing the current state of the deployment.
        """
        current_version = self._history[-1] if self._history else None
        return {
            'service_name': self.service_name,
            'environment': self.environment,
            'version': current_version,
            'status': self.status,
        }