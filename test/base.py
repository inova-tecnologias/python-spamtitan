import yaml, requests
from spamtitan import Spamtitan

class BaseTest(object):
  def setUp(self):
    with open("properties.yaml") as f:
      self.cfg = yaml.safe_load(f)
    
    print 'creating domain %s' % self.cfg['domain']
    self.st = Spamtitan(host=self.cfg['host'])
    self.st.create_domain(domain_name=self.cfg['domain'],
                          relay=self.cfg['relay'])
  def tearDown(self):
    print 'deleting domain %s' % self.cfg['domain']
    self.st.delete_domain(domain_name=self.cfg['domain'])