import os
import time
from tempfile import gettempdir

from selenium.common.exceptions import NoSuchElementException

from instapy import InstaPy
"""----------------------------"""
"""ignore everything above here"""
"""----------------------------"""




insta_username = ''
insta_password = ''

# set headless_browser=True if you want to run InstaPy without a browser opening
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False,
                  multi_logs=True)

try:
    session.login()


    """SETTINGS"""
    # all the set_.... belong below
    session.set_relationship_bounds(enabled=True,
				   max_followers=4590,
				    max_following=5555,
				     min_followers=45,
				      min_following=77)
    session.set_do_comment(True, percentage=10)
    session.set_comments(['aMEIzing!', 'So much fun!!', 'Nicey!'])
    session.set_dont_include(['friend1', 'friend2', 'friend3'])
    session.set_dont_like(['pizza', 'girl'])


    """ACTIONS"""
    # like_by_..., comment_by_..., follow_by_..., interact_user_..., follow_user_... all belong below
    session.like_by_tags(['natgeo'], amount=1)




    """----------------------------"""
    """ignore everything below here"""
    """----------------------------"""
except Exception as exc:
    # if changes to IG layout, upload the file to help us locate the change
    if isinstance(exc, NoSuchElementException):
        file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
        with open(file_path, 'wb') as fp:
            fp.write(session.browser.page_source.encode('utf8'))
        print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
            '*' * 70, file_path))
    # full stacktrace when raising Github issue
    raise

finally:
    # end the bot session
    session.end()
