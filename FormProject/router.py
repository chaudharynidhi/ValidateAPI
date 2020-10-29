from FormAPP import viewset
from rest_framework import routers
# Rest Framework adds support for automatic URL routing to django and provides with simple way of writing the viewsets logic to urls
router = routers.DefaultRouter()
router.register('id', viewset.IDViewSets)
router.register('age', viewset.AgeViewSets)