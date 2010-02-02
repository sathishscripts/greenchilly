from django.conf.urls.defaults import *

urlpatterns = patterns('djangogolf.web.views',
#    (r'web^$', 'showarticle'),
    (r'^$', 'index'),
    (r'^home/$', 'index'),
    (r'^adduser/(?P<code>\d+)/$', 'adduser'),
    (r'^edituser/$', 'edituser'),
    (r'^register/$', 'register'),
    (r'^addcourse/((?P<id>\d+)/)?$', 'addcourse'),
    (r'^addtee/(?P<courseid>\d+)/((?P<id>\d+)/)?$', 'addtee'),
    (r'^addhole/(?P<teeid>\d+)/((?P<id>\d+)/)?$', 'addhole'),
    (r'^managecourses/$','managecourses'),
    (r'^manageplayers/$','manageplayers'),
    (r'^addplayer/((?P<id>\d+)/)?$', 'addplayer'),
    (r'^managehandicaps/$','managehandicaps'),
    (r'^addhandicap/((?P<id>\d+)/)?$', 'addhandicap'),
    (r'^addscores/((?P<matchentry>\d+)/)?$', 'addscores'),
    (r'^managetournaments/$','managetournaments'),
    (r'^addtournament/((?P<id>\d+)/)?$', 'addtournament'),
    (r'^manageentries/(?P<trn>\d+)/$','manageentries'),
    (r'^managescores/(?P<trn>\d+)/$','managescores'),
    (r'^managetrophies/(?P<trn>\d+)/$','managetrophies'),
    (r'^deletematchentry/(?P<id>\d+)/$','deletematchentry'),
    (r'^addmatchentry/(?P<tourn>\d+)/((?P<id>\d+)/)?$', 'addmatchentry'),
    (r'^addtrophy/(?P<trn>\d+)/((?P<id>\d+)/)?$', 'addtrophy'),
    (r'^showcourse/(?P<id>\d+)/$', 'showcourse'),
    (r'^showresults/(?P<trp>\d+)/$', 'showresults'),
    (r'^showtee/(?P<course>\d+)/(?P<id>\d+)/$', 'showtee'),
    (r'^showscores/(?P<matchentry>\d+)/$', 'showscores'),
    )
