from __future__ import (absolute_import, division, print_function)
from enum import Enum

__metaclass__ = type


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
