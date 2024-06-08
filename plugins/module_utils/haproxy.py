from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import requests
from requests.auth import HTTPBasicAuth
from typing import List, Dict, Optional
from dataclasses import dataclass, field
from enum import Enum


# Definition of the enumeration EnableDisableEnum
class EnableDisableEnum(Enum):

    # The "enabled" status indicates that the feature is active
    ENABLED = "enabled"

    # The "disabled" status indicates that the feature is inactive
    DISABLED = "disabled"


# Definition of the enumeration Layer
class Layer(Enum):

    # Layer 4 (transport), typically for TCP/UDP
    LAYER4 = "layer4"

    # Layer 7 (application), typically for HTTP/HTTPS
    LAYER7 = "layer7"


# Definition of the enumeration SSLVersion
class SSLVersion(Enum):

    # SSLv3 (Secure Sockets Layer version 3)
    SSLv3 = "SSLv3"

    # TLSv1.0 (Transport Layer Security version 1.0)
    TLSv1_0 = "TLSv1.0"

    # TLSv1.1 (Transport Layer Security version 1.1)
    TLSv1_1 = "TLSv1.1"

    # TLSv1.2 (Transport Layer Security version 1.2)
    TLSv1_2 = "TLSv1.2"

    # TLSv1.3 (Transport Layer Security version 1.3)
    TLSv1_3 = "TLSv1.3"


# Definition of the enumeration ActionType
class ErrorActionType(Enum):

    # The "fastinter" action type
    FASTINTER = "fastinter"

    # The "fail-check" action type
    FAIL_CHECK = "fail-check"

    # The "sudden-death" action type
    SUDDEN_DEATH = "sudden-death"

    # The "mark-down" action type
    MARK_DOWN = "mark-down"


# Definition of the enumeration Requirement
class Requirement(Enum):

    # The "none" requirement indicates that no action is required
    NONE = "none"

    # The "required" requirement indicates that action is required
    REQUIRED = "required"


# Define an enumeration for load balancing algorithms
class LoadBalancingAlgorithm(Enum):

    # Round-robin algorithm
    ROUNDROBIN = "roundrobin"

    # Static round-robin algorithm
    STATIC_RR = "static-rr"

    # Least connections algorithm
    LEASTCONN = "leastconn"

    # First algorithm (first server available)
    FIRST = "first"

    # Source-based algorithm (based on client IP)
    SOURCE = "source"

    # URI-based algorithm
    URI = "uri"

    # URL parameter-based algorithm
    URL_PARAM = "url_param"

    # Header-based algorithm
    HDR = "hdr"

    # Random algorithm
    RANDOM = "random"

    # RDP cookie-based algorithm
    RDP_COOKIE = "rdp-cookie"

    # Hash-based algorithm
    HASH = "hash"


# Define an enumeration for cookie Type
class CookieType(Enum):

    # Rewrite the existing cookie
    REWRITE = "rewrite"

    # Insert a new cookie if it does not exist
    INSERT = "insert"

    # Prefix the cookie
    PREFIX = "prefix"


# Define an enumeration for Websocket Protocol
class WebSocketProtocol(Enum):
    """
    Represents WebSocket protocol types for the server configuration.

    Attributes:
        AUTO (str): Automatically select the WebSocket protocol.
        H1 (str): Use HTTP/1.1 protocol for WebSocket.
        H2 (str): Use HTTP/2 protocol for WebSocket.
    """
    AUTO = "auto"
    H1 = "h1"
    H2 = "h2"


# Define an enumeration for Proxy Backend/Frontend Protocol
class ProxyProtocol(Enum):
    """
    Represents protocol types for Proxy Backend and Frontend configurations.

    Attributes:
        HTTP (str): Use HTTP protocol.
        TCP (str): Use TCP protocol.
    """
    HTTP = "http"
    TCP = "tcp"


# Define an enumeration for Healtcheck Type Protocol
class HealthCheckType(Enum):
    """
    Represents health check types for HAProxy configurations.

    Attributes:
        COMMENT (str): Use comment health check.
        CONNECT (str): Use connect health check.
        DISABLE_ON_404 (str): Use disable-on-404 health check.
        EXPECT (str): Use expect health check.
        SEND (str): Use send health check.
        SEND_STATE (str): Use send-state health check.
        SET_VAR (str): Use set-var health check.
        SET_VAR_FMT (str): Use set-var-fmt health check.
        UNSET_VAR (str): Use unset-var health check.
    """
    COMMENT = "comment"
    CONNECT = "connect"
    DISABLE_ON_404 = "disable-on-404"
    EXPECT = "expect"
    SEND = "send"
    SEND_STATE = "send-state"
    SET_VAR = "set-var"
    SET_VAR_FMT = "set-var-fmt"
    UNSET_VAR = "unset-var"


# Define an enumeration for HttpMethod
class HttpMethod(Enum):
    """
    Represents HTTP check methods for HAProxy configurations.

    Attributes:
        HEAD (str): HEAD method.
        PUT (str): PUT method.
        POST (str): POST method.
        GET (str): GET method.
        TRACE (str): TRACE method.
        PATCH (str): PATCH method.
    """
    HEAD = "HEAD"
    PUT = "PUT"
    POST = "POST"
    GET = "GET"
    TRACE = "TRACE"
    PATCH = "PATCH"


# Define an enumeration for TimeoutStatus
class TimeoutStatus(Enum):
    """
    Represents timeout status for HAProxy health checks.

    Attributes:
        L7TOUT (str): Layer 7 timeout.
        L6TOUT (str): Layer 6 timeout.
        L4TOUT (str): Layer 4 timeout.
    """
    L7TOUT = "L7TOUT"
    L6TOUT = "L6TOUT"
    L4TOUT = "L4TOUT"


# Define an enumeration for MatchType
class MatchType(Enum):
    """
    Represents match types for HAProxy health checks.

    Attributes:
        STATUS (str): Match status.
        RSTATUS (str): Match regular expression status.
        HDR (str): Match header.
        FHDR (str): Match first header.
        STRING (str): Match string.
        RSTRING (str): Match regular expression string.
    """
    STATUS = "status"
    RSTATUS = "rstatus"
    HDR = "hdr"
    FHDR = "fhdr"
    STRING = "string"
    RSTRING = "rstring"


# Define an enumeration for ErrorStatus
class ErrorStatus(Enum):
    """
    Represents error status for HAProxy health checks.

    Attributes:
        L7OKC (str): Layer 7 OKC error.
        L7RSP (str): Layer 7 response error.
        L7STS (str): Layer 7 status error.
        L6RSP (str): Layer 6 response error.
        L4CON (str): Layer 4 connection error.
    """
    L7OKC = "L7OKC"
    L7RSP = "L7RSP"
    L7STS = "L7STS"
    L6RSP = "L6RSP"
    L4CON = "L4CON"


# Define an enumeration for OkStatus
class OkStatus(Enum):
    """
    Represents OK status for HAProxy health checks.

    Attributes:
        L7OK (str): Layer 7 OK.
        L7OKC (str): Layer 7 OKC.
        L6OK (str): Layer 6 OK.
        L4OK (str): Layer 4 OK.
    """
    L7OK = "L7OK"
    L7OKC = "L7OKC"
    L6OK = "L6OK"
    L4OK = "L4OK"


# Load Balancing Configuration
@dataclass
class Balance:
    """
    Represents a load balancing algorithm configuration.
    Refer at : `https://www.haproxy.com/documentation/dataplaneapi/community/#post-/services/haproxy/configuration`

    Attributes:
        algorithm (str): The balancing algorithm (e.g., "roundrobin", "leastconn", "static-rr", "first", "source", "uri", "url_param", "hdr", "random", etc...).
        hash_expression (str): The hash expression used for hash-based balancing.
        hdr_name (str): The header name for header-based balancing.
        hdr_use_domain_only (bool): Whether to use only the domain part of the header for header-based balancing.
        random_draws (int): The number of random draws for random-based balancing.
        rdp_cookie_name (str): The name of the cookie for RDP cookie-based balancing.
        uri_depth (int): The URI depth for URI-based balancing.
        uri_len (int): The URI length for URI-based balancing.
        uri_path_only (bool): Whether to use only the path part of the URI for URI-based balancing.
        uri_whole (bool): Whether to use the entire URI for URI-based balancing.
        url_param (str): The URL parameter name for URL parameter-based balancing.
        url_param_check_post (int): The number of URL parameters to consider from POST data for URL parameter-based balancing.
        url_param_max_wait (int): The maximum wait time for a URL parameter-based balancing response.
    """
    algorithm: LoadBalancingAlgorithm
    hash_expression: str
    hdr_name: str
    hdr_use_domain_only: bool
    random_draws: int
    rdp_cookie_name: str
    uri_depth: int
    uri_len: int
    uri_path_only: bool
    uri_whole: bool
    url_param: str
    url_param_check_post: int
    url_param_max_wait: int

    def __post_init__(self):

        # Check Algorithm
        if not self.algorithm:
            raise ValueError("The 'algorithm' field is required.")

    def __str__(self):
        """
        Returns a dictionary representation of the Balance object.
        """
        return str(self.__dict__)


# Backend Cookie Configuration
@dataclass
class Cookie:
    """
    Represents a session cookie configuration.
    Refer at : `https://www.haproxy.com/documentation/dataplaneapi/community/#post-/services/haproxy/configuration`

    Attributes:
        attr (List[Dict[str, str]], optional): List of attribute values for the cookie.
        domain (List[Dict[str, str]], optional): List of domain values for the cookie.
        dynamic (bool, optional): Whether the cookie is dynamic.
        httponly (bool, optional): Whether the cookie is HTTP-only.
        indirect (bool, optional): Whether the cookie is indirect.
        maxidle (int, optional): Maximum idle time for the cookie.
        maxlife (int, optional): Maximum life time for the cookie.
        name (str, required): The name of the cookie.
        nocache (bool, optional): Whether the cookie is no-cache.
        postonly (bool, optional): Whether the cookie is post-only.
        preserve (bool, optional): Whether the cookie is preserved.
        secure (bool, optional): Whether the cookie is secure.
        type (str, optional): The type of the cookie.
    """
    name: str
    attr: List[Dict[str, str]] = field(default_factory=list)
    domain: List[Dict[str, str]] = field(default_factory=list)
    dynamic: Optional[bool] = None
    httponly: Optional[bool] = None
    indirect: Optional[bool] = None
    maxidle: Optional[int] = None
    maxlife: Optional[int] = None
    nocache: Optional[bool] = None
    postonly: Optional[bool] = None
    preserve: Optional[bool] = None
    secure: Optional[bool] = None
    type: CookieType = CookieType.REWRITE

    def __post_init__(self):

        # Check Name
        if not self.name:
            raise ValueError("The 'name' field is required.")

    def __str__(self):
        """
        Returns a dictionary representation of the Cookie object.
        """
        return str(self.__dict__)


# Backend Configuration
@dataclass
class Server:
    """
    Represents a server configuration with various parameters.

    Attributes:
        name (str, required): The name of the server.
        address (str, required): The IP address or hostname of the server.
        port (int, required): The port number on which the server listens.
        status (EnableDisableEnum, required): The current status of the server (enabled/disabled).
        layer (Layer, required): The network layer the server operates on (Layer 4/Layer 7).
        ssl_version (SSLVersion, required): The SSL/TLS version used by the server.
        action (ActionType, required): The action type associated with the server.
        requirement (Requirement, required): The requirement level for the server.
        verify (str, optional): Additional verification parameter.
        verifyhost (str, optional): Parameter for verifying the host.
        weight (int, optional): The weight of the server for load balancing.
        track (str, optional): Tracking parameter for the server.
        ws (str, optional): Web socket related parameter.
        check (str, optional): Health check parameter.
        health_check_address (str, optional): The address used for health checks.
        health_check_port (int, optional): The port used for health checks.
        max_reuse (int, optional): Maximum number of reuses.
        maxconn (int, optional): Maximum number of connections.
        maxqueue (int, optional): Maximum number of queued connections.
        minconn (int, optional): Minimum number of connections.
    """
    name: str
    address: str
    port: int
    verify: Optional[Requirement] = None
    verifyhost: Optional[str] = None
    weight: Optional[int] = None
    track: Optional[str] = None
    ws: Optional[WebSocketProtocol] = None
    check: Optional[Requirement] = None
    health_check_address: Optional[str] = None
    health_check_port: Optional[int] = None
    max_reuse: Optional[int] = None
    maxconn: Optional[int] = None
    maxqueue: Optional[int] = None
    minconn: Optional[int] = None

    def __post_init__(self):

        # Ajoutez ici des validations si nécessaire
        if not self.name:
            raise ValueError("The 'name' field is required.")

        if not self.address:
            raise ValueError("The 'address' field is required.")

        if self.port is None or self.port < 0:
            raise ValueError("The 'port' field must be a positive integer.")


# HTTP HealthCheck Configuration
@dataclass
class HttpHealthCheck:
    """
    Represents a health check configuration in HAProxy.

    Attributes:
        type (HealthCheckType): The type of health check.
        method (Optional[str]): The method used for the health check.
        uri (Optional[str]): The URI used for the health check.
        uri_log_format (Optional[str]): The log format for the URI.
        var_expr (Optional[str]): The expression for the variable.
        var_format (Optional[str]): The format for the variable.
        var_name (Optional[str]): The name of the variable.
        var_scope (Optional[str]): The scope of the variable.
        version (Optional[str]): The version for the health check.
        via_socks4 (Optional[bool]): Whether to use SOCKS4.
        port (Optional[int]): The port number for the health check.
        port_string (Optional[str]): The port number as a string.
        proto (Optional[str]): The protocol used for the health check.
        send_proxy (Optional[bool]): Whether to send proxy protocol.
        sni (Optional[str]): The SNI for the health check.
        ssl (Optional[bool]): Whether to use SSL.
        status_code (Optional[str]): The status code for the health check.
        tout_status (Optional[TimeoutStatus]): The timeout status.
        match (Optional[MatchType]): The match type for the health check.
        headers (Optional[List[Dict[str, str]]]): The headers for the health check.
        body (Optional[str]): The body content for the health check.
        body_log_format (Optional[str]): The log format for the body.
        check_comment (Optional[str]): The comment for the health check.
        default (Optional[bool]): Whether this is the default health check.
        error_status (Optional[ErrorStatus]): The error status for the health check.
        addr (Optional[str]): The address for the health check.
        ok_status (Optional[OkStatus]): The OK status for the health check.
    """

    type: HealthCheckType
    method: Optional[str] = None
    uri: Optional[str] = None
    uri_log_format: Optional[str] = None
    var_expr: Optional[str] = None
    var_format: Optional[str] = None
    var_name: Optional[str] = None
    var_scope: Optional[str] = None
    version: Optional[str] = None
    via_socks4: Optional[bool] = None
    port: Optional[int] = None
    port_string: Optional[str] = None
    proto: Optional[str] = None
    send_proxy: Optional[bool] = None
    sni: Optional[str] = None
    ssl: Optional[bool] = None
    status_code: Optional[str] = None
    tout_status: Optional[TimeoutStatus] = None
    match: Optional[MatchType] = None
    headers: Optional[List[Dict[str, str]]] = None
    body: Optional[str] = None
    body_log_format: Optional[str] = None
    check_comment: Optional[str] = None
    default: Optional[bool] = None
    error_status: Optional[ErrorStatus] = None
    addr: Optional[str] = None
    ok_status: Optional[OkStatus] = None


# HTTP check parameters Configuration
@dataclass
class HttpCheckParams:
    """
    Represents the HTTP check parameters for a HAProxy backend.

    Attributes:
        method (Optional[HttpCheckMethod]): The HTTP method used for the health check.
        uri (str): The URI used for the health check.
        version (str): The HTTP version.
    """
    method: HttpMethod
    uri: str
    version: str = "HTTP/1.1"

    def __post_init__(self):

        # Ajoutez ici des validations si nécessaire
        if not self.method:
            raise ValueError("The 'method' field is required.")

        if not self.uri:
            raise ValueError("The 'uri' field is required.")


# Backend Configuration
@dataclass
class Backend:
    name: str
    mode: Optional[ProxyProtocol] = None
    balance: Optional[Balance] = None
    httpchk: Optional[HttpHealthCheck] = None
    httpchk_params: Optional[HttpCheckParams] = None


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


# Build and Return HA Proxy Client from Module Informations
def haproxy_client(module):

    # Required Module Keys
    credential_keys = [
        'base_url',
        'api_version',
        'username',
        'password'
    ]

    # Match Required Keys with Module Parameters
    # Find each credential_keys entry in module.params (Build Boolean array)
    credential_parameters = [cred_key in module.params for cred_key in credential_keys]

    # If All Credentials keyx are present in Module Parameters
    if not all(credential_parameters):

        # Error Message for Module
        module.fail_json(msg="Missing Client API Parameter")

    # Build and Return Client
    return Client(**{ credential: module.params[credential] for credential in credential_keys })
