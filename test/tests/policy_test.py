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

class PolicyTest(TestCase, BaseTest):
  # ------------------------------------------------------------------ unbound
  def setUp(self):
    # BEFORE RUN TESTS
    BaseTest.setUp(self)

  def tearDown(self):
    # AFTER RUN TESTS
    BaseTest.tearDown(self)

  # -------------------------------------------------------------------- tests
  def test_modify_policy(self):
    print 'test_modify_policy'
    r = self.st.edit_policy(user=self.cfg['domain'],
                        spam_tag2_level=4.5,
                        spam_quarantine_to='',
                        spam_lover='Y',
                        virus_quarantine_to='',
                        digest='D', # quarantine report daily
                        report_type='Y', # new items since last report, except virus
                        digest_language='pt_BR'
                        )
    if not r.status_code == 200:
      self.assertTrue(False)

if __name__ == "__main__":
  unittest.main()