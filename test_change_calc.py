
from change_calc import change_calculater

def test_getchange():
   output=change_calculater.get_change()
   assert output=={}

