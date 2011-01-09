from distutils.core import setup

setup(name='content_blocks',
      version='0.1',
      description='Blocks of content that can be placed into templates in areas specified by settings.py',
      author='Kevin Brolly',
      author_email='kevin.brolly@gmail.com',
      url='https://github.com/KevinBrolly/django-content-blocks/',
      packages=['content_blocks', 'content_blocks.templatetags'],
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )