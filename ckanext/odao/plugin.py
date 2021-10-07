from flask import Blueprint, make_response, jsonify

from ckan import plugins as p
from ckan.lib.authenticator import UsernamePasswordAuthenticator
from ckan.logic import NotAuthorized
import ckan.lib.api_token as api_token
import ckan.model as model
from datetime import datetime
import logging 

log = logging.getLogger(__name__)

toolkit = p.toolkit

blueprint = Blueprint(u'odao', __name__, url_prefix='/odao')

authenticator = UsernamePasswordAuthenticator()

def _login(): 
    try:
        credential = toolkit.request.json
        user = authenticator.authenticate(toolkit.request.environ, credential)
        if user is None:
            raise NotAuthorized('wrong id or password')
        
        user_obj = model.User.get(user)

        # token 
        tokens = toolkit.get_action('api_token_list')({ u'user': user }, { u'user': user })
        token = next((x for x in tokens if x[u'name'] == u'ODAO_API_TOKEN_APP_CLIENT'), None)
        if token:
            # decode api_token 
            dt = datetime.strptime(token[u'created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            data = {
                u'jti': token[u'id'],
                u'iat': api_token.into_seconds(dt)
            }
            token = api_token.encode(data)

            response = make_response(
                { 
                    u'success': True, 
                    u'result': {
                        u'id': user_obj.id,
                        u'name': user_obj.name,
                        u'fullname': user_obj.fullname,
                        u'image_url': user_obj.image_url,
                        u'sysadmin': user_obj.sysadmin,
                        u'token': token
                    }
                }
            )
            response.headers[u'Content-Type'] = u'application/json'
            return response

        else:
            response = make_response(
                { u'success': True, u'result': None }
            )
            return 
    except NotAuthorized as e:
        return {
            'success': False,
            'msg': format(e)
        }

blueprint.add_url_rule(u'/login', view_func=_login, methods=['POST'])

class OdaoPlugin(p.SingletonPlugin):

    p.implements(p.IBlueprint)

    # IBlueprint

    def get_blueprint(self):

        return [blueprint]