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

class DomainTest(TestCase, BaseTest):
  # ------------------------------------------------------------------ unbound
  def setUp(self):
    # BEFORE RUN TESTS
    BaseTest.setUp(self)

  def tearDown(self):
    # AFTER RUN TESTS
    BaseTest.tearDown(self)

  # -------------------------------------------------------------------- tests
  def test_modify_domain(self):
    print 'test_modify_domain'
    r = self.st.edit_domain(domain_name=self.cfg['domain'],
                        server=self.cfg['relay'],
                        rv='ldap',
                        ldap_server=self.cfg['ldap_server'],
                        ldap_port=self.cfg['ldap_port'],
                        ldap_search_dn=self.cfg['ldap_search_dn'],
                        ldap_password=self.cfg['ldap_password'],
                        ldap_filter=self.cfg['ldap_filter'],
                        ldap_searchbase=self.cfg['ldap_searchbase'],
                        ldap_result_attribute=self.cfg['ldap_result_attribute']
                        )
    if not r.status_code == 200:
      self.assertTrue(False)

if __name__ == "__main__":
  unittest.main()