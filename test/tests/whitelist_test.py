import unittest, requests
from test.base import BaseTest
from unittest import TestCase

# supress ssl warnings.
requests.packages.urllib3.disable_warnings(
    requests
    .packages
    .urllib3
    .exceptions
    .InsecureRequestWarning)

class WhiteListTest(TestCase, BaseTest):
  # ------------------------------------------------------------------ unbound
  def setUp(self):
    # BEFORE RUN TESTS
    BaseTest.setUp(self)

  def tearDown(self):
    # AFTER RUN TESTS
    BaseTest.tearDown(self)

  #-------------------------------------------------------------------- tests
  def test_add_whitelist(self):
    print 'test_add_whitelist'
    r = self.st.add_whitelist(user=self.cfg['domain'],
                              sender='fernando.cainelli@inova.net'
                        )
    if not r.status_code == 200:
      self.assertTrue(False)
  
  def test_list_whitelist(self):
    print 'test_list_whitelist'
    r = self.st.list_whitelist(user=self.cfg['domain'])
    
    if not r.status_code == 200:
      self.assertTrue(False)

  def test_remove_whitelist(self):
    print 'test_remove_whitelist'
    r = self.st.remove_whitelist(user=self.cfg['domain'],
                              sender='fernando.cainelli@inova.net'
                        )
    if not r.status_code == 200:
      self.assertTrue(False)

if __name__ == "__main__":
  unittest.main()