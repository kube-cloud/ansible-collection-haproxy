from __future__ import (absolute_import, division, print_function)
from typing import List, Dict, Optional
from dataclasses import dataclass, field
from enumeration import *

__metaclass__ = type


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


@dataclass
class HttpCheckParams:
    """
    Represents the HTTP check parameters for a HAProxy backend.

    Attributes:
        method (Optional[HttpCheckMethod]): The HTTP method used for the health check.
        uri (str): The URI used for the health check.
        version (str): The HTTP version.
    """
    method: Optional[HttpMethod] = HttpMethod.GET
    uri: str
    version: str

@dataclass
class Backend:
    name: str
    mode: Optional[ProxyProtocol] = None
    balance: Optional[Balance] = None
    httpchk: Optional[HttpHealthCheck] = None
    httpchk_params: Optional[HttpCheckParams] = None