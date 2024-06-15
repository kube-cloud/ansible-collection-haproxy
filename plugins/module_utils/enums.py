from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from enum import Enum


# Base Enumeration
class BaseEnum(Enum):

    # Create Instance
    @classmethod
    def create(cls, value: str):

        # Inf Value is None
        if value is None:

            # Return None
            return None

        # Iterate on Enum members
        for member in cls:

            # If member match on value
            if member.name == value.upper() or member.value.upper == value.upper:

                # Return the Member
                return member

        # Return None
        return None


# Definition of the enumeration EnableDisableEnum
class EnableDisableEnum(BaseEnum):

    # The "enabled" status indicates that the feature is active
    ENABLED = "enabled"

    # The "disabled" status indicates that the feature is inactive
    DISABLED = "disabled"


# Definition of the enumeration Layer
class Layer(BaseEnum):

    # Layer 4 (transport), typically for TCP/UDP
    LAYER4 = "layer4"

    # Layer 7 (application), typically for HTTP/HTTPS
    LAYER7 = "layer7"


# Definition of the enumeration SSLVersion
class SSLVersion(BaseEnum):

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


# Definition of the enumeration FrontendLevel
class FrontendLevel(BaseEnum):

    # Level USER
    USER = "user"

    # Level OPERATOR
    OPERATOR = "operator"

    # Level ADMINISTRATOR
    ADMIN = "admin"


# Definition of the enumeration ActionType
class ErrorActionType(BaseEnum):

    # The "fastinter" action type
    FASTINTER = "fastinter"

    # The "fail-check" action type
    FAIL_CHECK = "fail-check"

    # The "sudden-death" action type
    SUDDEN_DEATH = "sudden-death"

    # The "mark-down" action type
    MARK_DOWN = "mark-down"


# Definition of the enumeration Requirement
class Requirement(BaseEnum):

    # The "none" requirement indicates that no action is required
    NONE = "none"

    # The "required" requirement indicates that action is required
    REQUIRED = "required"

    # The "optional" requirement indicates that action is required
    OPTIONAL = "optional"


# Define an enumeration for load balancing algorithms
class LoadBalancingAlgorithm(BaseEnum):

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
class CookieType(BaseEnum):

    # Rewrite the existing cookie
    REWRITE = "rewrite"

    # Insert a new cookie if it does not exist
    INSERT = "insert"

    # Prefix the cookie
    PREFIX = "prefix"


# Define an enumeration for Websocket Protocol
class WebSocketProtocol(BaseEnum):
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
class ProxyProtocol(BaseEnum):
    """
    Represents protocol types for Proxy Backend and Frontend configurations.

    Attributes:
        HTTP (str): Use HTTP protocol.
        TCP (str): Use TCP protocol.
    """
    HTTP = "http"
    TCP = "tcp"


# Define an enumeration for Healtcheck Type Protocol
class HealthCheckType(BaseEnum):
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


# Define an enumeration for Advanced Healtcheck Type Protocol
class AdvancedHealthCheckType(BaseEnum):
    """
    Represents various health check types for HAProxy.

    Attributes:
        SSL_HELLO_CHK (str): SSL hello health check.
        SMTPCHK (str): SMTP health check.
        LDAP_CHECK (str): LDAP health check.
        MYSQL_CHECK (str): MySQL health check.
        PGSQL_CHECK (str): PostgreSQL health check.
        TCP_CHECK (str): TCP health check.
        REDIS_CHECK (str): Redis health check.
        HTTPCHK (str): HTTP health check.
    """
    SSL_HELLO_CHK = "ssl-hello-chk"
    SMTPCHK = "smtpchk"
    LDAP_CHECK = "ldap-check"
    MYSQL_CHECK = "mysql-check"
    PGSQL_CHECK = "pgsql-check"
    TCP_CHECK = "tcp-check"
    REDIS_CHECK = "redis-check"
    HTTPCHK = "httpchk"


# MySQL Check Type Params
class MySqlVersionCheckType(BaseEnum):
    """
    Represents version check types.

    Attributes:
        PRE_41 (str): Version check for pre-41.
        POST_41 (str): Version check for post-41.
    """
    PRE_41 = "pre-41"
    POST_41 = "post-41"


# Define an enumeration for HttpMethod
class HttpMethod(BaseEnum):
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
class TimeoutStatus(BaseEnum):
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
class MatchType(BaseEnum):
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
class ErrorStatus(BaseEnum):
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
class OkStatus(BaseEnum):
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


# Define an enumeration for CompressionAlgorithm
class CompressionAlgorithm(BaseEnum):
    """
    Represents Compression Algorithm for HAProxy Front End.

    Attributes:
        IDENTITY (str): Identity.
        GZIP (str): Layer 7 OKC.
        DEFLATE (str): Deflate.
        RAW_DEFLATE (str): Raw Deflate.
    """
    IDENTITY = "identity"
    GZIP = "gzip"
    DEFLATE = "deflate"
    RAW_DEFLATE = "raw-deflate"


# Condition Type
class ConditionType(BaseEnum):
    """
    Represents Condition types.

    Attributes:
        IF (str): IF Condition.
        UNLESS (str): UNLESS Condition.
    """
    IF = "if"
    UNLESS = "unless"
