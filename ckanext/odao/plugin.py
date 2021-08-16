from flask import Blueprint, make_response, jsonify

from ckan import plugins as p
from ckan.lib.authenticator import UsernamePasswordAuthenticator
from ckan.logic import NotAuthorized

toolkit = p.toolkit

blueprint = Blueprint(u'odao', __name__, url_prefix='/odao')

authenticator = UsernamePasswordAuthenticator()

def _login(): 
    try:
        credential = toolkit.request.json
        user = authenticator.authenticate(toolkit.request.environ, credential)
        if user is None:
            raise NotAuthorized('wrong id or password')
        
        tokens = toolkit.get_action('api_token_list')({ u'user': user }, { u'user': user })
        response = make_response(
            { u'success': True, u'result': tokens }
        )
        response.headers[u'Content-Type'] = u'application/json'
        return response
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