# -*- coding: utf-8 -*-

"""common class for REST API"""

from .auth import token_authenticated, http_authenticated, session_authenticated, authenticated

from .base import (make_empty_response, Resource, TokenRequiredResource,
                   AdminRoleRequiredResource, jwt_authenticate, jwt_encode_payload,
                   jwt_decode_token, jwt_load_user, jwt_make_payload)

from .utils import marshal

from .decorators import (anonymous_required, token_auth_required, http_auth_required,
                         session_auth_required, auth_required, permissions_accepted,
                         permissions_required, roles_required, roles_accepted, one_of, paginated,
                         marshal_with, marshal_with_data_envelope, extract_args)
