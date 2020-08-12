from webapp.viewset import EmployeeViewset,showdataViewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register('employee',EmployeeViewset)
router.register('showdata',showdataViewset)

