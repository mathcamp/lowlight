from pyramid.config import Configurator
import random

def _make_user(request, name, bio, photo):
    lat = 37.7774 + random.random()/100 - 0.005
    lon = -122.398 + random.random()/100 - 0.005
    return {
        'fullname': name,
        'bio': bio,
        'photo': request.static_url('lowlight:static/%s.png' % photo),
        'lat': lat,
        'lon': lon,
    }


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_request_method(_make_user, name='make_user')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('feed', '/feed')
    config.scan()
    return config.make_wsgi_app()
