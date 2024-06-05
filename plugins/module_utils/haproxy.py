from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import requests
from requests.auth import HTTPBasicAuth


class Client:
    """
    Client for interacting with the HAProxy Data Plane API.

    Attributes:
        base_url (str): The base URL of the HAProxy Data Plane API.
        auth (HTTPBasicAuth): The HTTP basic authentication credentials.
    """

    # Backends URI
    CONFIG_VERSION_URI = "services/haproxy/configuration/version"

    # Backends URI
    BACKENDS_URI = "services/haproxy/configuration/backends"

    # Backend URI
    BACKEND_URI = "services/haproxy/configuration/backends/{name}"

    # Frontends URI
    FRONTENDS_URI = "services/haproxy/configuration/frontends"

    # Frontend URI
    FRONTEND_URI = "services/haproxy/configuration/frontends/{name}"

    # Servers URI
    SERVERS_URI = "services/haproxy/configuration/servers"

    # Create Transaction URI
    CREATE_TRANSACTION_URI = "services/haproxy/configuration/transactions?version={config_number}"

    # Validate Transaction URI
    VALIDATE_TRANSACTION_URI = "services/haproxy/configuration/transactions/{transaction_id}"

    # URL Format
    URL_TEMPLATE = "{base_url}/{version}/{uri}"

    def __init__(self, base_url, api_version, username, password):
        """
        Initializes the HAProxyClient with the given base URL and credentials.

        Args:
            base_url (str): The base URL (scheme://host:port) of the HAProxy Data Plane API.
            api_version (str): The HAProxy Data Plane API Version (v1 or v2)
            username (str): The username for HTTP basic authentication.
            password (str): The password for HTTP basic authentication.
        Raises:
            ValueError: If any of the required parameters are not provided.
        """

        # If Base URL is not Provided
        if not base_url:

            # Raise Value Exception
            raise ValueError("[HAProxyClient] - Initialization failed : 'base_url' is required")

        # If Username is not Provided
        if not username:

            # Raise Value Exception
            raise ValueError("[HAProxyClient] - Initialization failed : 'username' is required")

        # If Password is not Provided
        if not password:

            # Raise Value Exception
            raise ValueError("[HAProxyClient] - Initialization failed : 'password' is required")

        # Initialize Base URL
        self.base_url = base_url.rstrip('/')

        # Initialize Version
        self.api_version = api_version if api_version else "v2"

        # Initialize Basic Authentication
        self.auth = HTTPBasicAuth(username, password)

    def get_configuration_version(self):
        """
        Get HAProxy Configuration Version.

        Returns:
            integer: Configuration Version.

        Raises:
            requests.exceptions.HTTPError: If the API request fails.
        """

        # Build the Operation URL
        url = self.URL_TEMPLATE.format(
            base_url=self.base_url,
            uri=self.CONFIG_VERSION_URI,
            version=self.api_version
        )

        # Execute Request
        response = requests.get(url, auth=self.auth)

        # If Object Exists
        if response.status_code == 200:

            # Return JSON
            return response.json()

        else:

            # Raise Exception
            response.raise_for_status()

    def create_transaction(self):
        """
        Start HAProxy Data Plane API Transaction and Details.

        Returns:
            dict: Details of HAProxy Data Plane API Transaction in JSON format.

        Raises:
            requests.exceptions.HTTPError: If the API request fails.
        """

        # Get Configuration Version
        config_version = self.get_configuration_version()

        # Build the Operation URL
        url = self.URL_TEMPLATE.format(
            base_url=self.base_url,
            uri=self.CREATE_TRANSACTION_URI.format(config_version=config_version),
            version=self.api_version
        )

        # Execute Request
        response = requests.post(url, auth=self.auth)

        # If Object Exists
        if response.status_code == 200:

            # Return JSON
            return response.json()

        else:

            # Raise Exception
            response.raise_for_status()

    def validate_transaction(self, transaction_id):
        """
        Validate HAProxy Data Plane API Transaction and Details.

        Returns:
            dict: Details of Validated HAProxy Data Plane API Transaction in JSON format.

        Raises:
            requests.exceptions.HTTPError: If the API request fails.
        """

        # Build the Operation URL
        url = self.URL_TEMPLATE.format(
            base_url=self.base_url,
            uri=self.VALIDATE_TRANSACTION_URI.format(transaction_id=transaction_id),
            version=self.api_version
        )

        # Execute Request
        response = requests.put(url, auth=self.auth)

        # If Object Exists
        if response.status_code == 200:

            # Return JSON
            return response.json()

        else:

            # Raise Exception
            response.raise_for_status()

    def get_backends(self):
        """
        Retrieves the list of Backends from the HAProxy Data Plane API.

        Returns:
            list: A list of Backends in JSON format.

        Raises:
            requests.exceptions.HTTPError: If the API request fails.
        """

        # Build the Operation URL
        url = self.URL_TEMPLATE.format(
            base_url=self.base_url,
            uri=self.BACKENDS_URI,
            version=self.api_version
        )

        # Execute Request
        response = requests.get(url, auth=self.auth)

        # If Object Exists
        if response.status_code == 200:

            # Return JSON
            return response.json()

        else:

            # Raise Exception
            response.raise_for_status()

    def get_backend(self, name):
        """
        Retrieves the details of given Backend (name) from the HAProxy Data Plane API.

        Args:
            name (str): The name of the Backend to retrieve details for.

        Returns:
            dict: Details of Backend in JSON format.

        Raises:
            requests.exceptions.HTTPError: If the API request fails.
        """

        # Build the Operation URL
        url = self.URL_TEMPLATE.format(
            base_url=self.base_url,
            uri=self.BACKEND_URI.format(name=name),
            version=self.api_version
        )

        # Execute Request
        response = requests.get(url, auth=self.auth)

        # If Object Exists
        if response.status_code == 200:

            # Return JSON
            return response.json()

        else:

            # Raise Exception
            response.raise_for_status()

    def get_frontends(self):
        """
        Retrieves the list of Frontends from the HAProxy Data Plane API.

        Returns:
            list: A list of Frontends in JSON format.

        Raises:
            requests.exceptions.HTTPError: If the API request fails.
        """

        # Build the Operation URL
        url = self.URL_TEMPLATE.format(
            base_url=self.base_url,
            uri=self.FRONTENDS_URI,
            version=self.api_version
        )

        # Execute Request
        response = requests.get(url, auth=self.auth)

        # If Object Exists
        if response.status_code == 200:

            # Return JSON
            return response.json()

        else:

            # Raise Exception
            response.raise_for_status()

    def get_frontend(self, name):
        """
        Retrieves the details of given Frontend (name) from the HAProxy Data Plane API.

        Args:
            name (str): The name of the frontend to retrieve details for.

        Returns:
            dict: Details of Frontend in JSON format.

        Raises:
            requests.exceptions.HTTPError: If the API request fails.
        """

        # Build the Operation URL
        url = self.URL_TEMPLATE.format(
            base_url=self.base_url,
            uri=self.FRONTEND_URI.format(name=name),
            version=self.api_version
        )

        # Execute Request
        response = requests.get(url, auth=self.auth)

        # If Object Exists
        if response.status_code == 200:

            # Return JSON
            return response.json()

        else:

            # Raise Exception
            response.raise_for_status()

    def create_backend(self, backend, transaction_id):
        """
        Create a Backend on HAProxy API.

        Args:
            backend (str): The backend to create.
            servers (list): List of Servers to Add to Backend
            transaction_id (str): Started Transaction ID

        Returns:
            dict: Details of Created Backend in JSON format.

        Raises:
            requests.exceptions.HTTPError: If the API request fails.
        """

        # If Transaction IF is Provided
        if transaction_id and transaction_id.strip():

            # Initialize URI
            create_backend_uri = "{backend_uri}/{transaction_id}".format(
                backend_uri=self.BACKENDS_URI,
                transaction_id=transaction_id
            )

        else:

            # Get Configuration Version
            config_version = self.get_configuration_version()

            # Initialize URI
            create_backend_uri = "{be_uri}?version={config_version}".format(
                be_uri=self.BACKENDS_URI,
                config_version=config_version
            )

        # Build the Operation URL
        url = self.URL_TEMPLATE.format(
            base_url=self.base_url,
            uri=create_backend_uri,
            version=self.api_version
        )

        # Execute Request
        response = requests.post(
            url=url,
            json=backend,
            headers={
                "Content-Type": "application/json"
            },
            auth=self.auth
        )

        # If Object Exists
        if response.status_code == 200:

            # Return JSON
            return response.json()

        else:

            # Raise Exception
            response.raise_for_status()
