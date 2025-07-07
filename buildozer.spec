[app]

# (str) Title of your application
title = FaceApp

# (str) Package name
package.name = faceapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.kivy.faceapp

# (str) Source code directory. This is the directory where your main.py lives.
source.dir = .

# (list) Python files to exclude from the build (comma separated values)
source.exclude_exts = pyc,bif,bak,orig

# (list) Application requirements
# comma separated values. You MUST NOT use a space after a comma.
# Python version (e.g. 3.9) automatically added if not specified.
requirements = python3,kivy,opencv-python,numpy,flask,requests,Pillow,pyopenssl,certifi,charset-normalizer,idna,urllib3,Werkzeug,itsdangerous,Jinja2,MarkupSafe,click,colorama,importlib-metadata,zipp,setuptools,wheel,cryptography,cffi,pycparser,bcrypt,PyNaCl,paramiko,pynacl,pyasn1,pyasn1-modules,rsa,six,toml,watchdog,zope.interface,zope.event,zope.component,zope.deferredimport,zope.interface,zope.schema,zope.configuration,zope.hookable,zope.location,zope.proxy,zope.security,zope.sqlalchemy,zope.tales,zope.testing,zope.traversing,zope.viewlet,zope.app.publisher,zope.app.component,zope.app.container,zope.app.form,zope.app.pagetemplate,zope.app.publication,zope.app.securitypolicy,zope.app.zcml,zope.browser,zope.cachedescriptors,zope.component.testfiles,zope.contenttype,zope.datetime,zope.dublincore,zope.exceptions,zope.filerepresentation,zope.formlib,zope.globalrequest,zope.i18n,zope.i18nmessageid,zope.interface.testfiles,zope.lifecycle,zope.login,zope.mimetype,zope.minmax,zope.pagetemplate,zope.publisher,zope.ramcache,zope.rdb,zope.schema.testfiles,zope.sendmail,zope.session,zope.site,zope.size,zope.tal,zope.testing,zope.textresource,zope.traversing,zope.viewlet,zope.xmlpickle

# (str) Version of your application
version = 0.1

# (list) Permissions
android.permissions = INTERNET,CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Android SDK version to use. Use a recent API level.
android.api = 33

# (int) Minimum API level for your application (e.g., 21 for Android 5.0)
android.minapi = 21

# (bool) Enable or disable the Java compiler debug mode (True for development)
android.debug = True

# (str) The name of the main Python file to run.
main.py = app.py

# (list) Additional files or directories to include in the APK
# ONLY include the Haar cascade file here. known_faces/ will be created at runtime.
android.add_src = haarcascade_frontalface_default.xml

# (bool) Enable or disable the application's fullscreen mode
fullscreen = False

# (str) Orientation of the application (e.g., portrait, landscape)
orientation = portrait

# The following are often useful for debugging, uncomment if needed:
# logcat = 1
# python.logcat = 1
