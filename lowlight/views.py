from pyramid.view import view_config

@view_config(route_name='feed', renderer='json')
def get_feed(request):
    return [
        request.make_user('Dr. McNinja', 'Should you need the services of a '
                          'doctor or a ninja, my office is always open',
                          'drmcninja'),
        request.make_user('Black Hat Guy', 'I *like* my hat', 'blackhatguy'),
        request.make_user('Gabe', "There are a lot of things you can eat "
                          "that aren't food.", 'gabe'),
        request.make_user('Tycho', 'Some people play tennis, I erode the '
                          'human soul.', 'tycho'),
        request.make_user('Derp Fox', 'I will lead you to the golden '
                          'songbird!', 'derpfox'),
        request.make_user('Rex', 'Tee hee', 'rex'),
        request.make_user('Purple Shirted Eye Stabber', 'Who else loves '
                          'played-out recurring characters?', 'pses'),
        request.make_user('Seagull Man', 'Follow your dreams!', 'seagullman'),
    ]
