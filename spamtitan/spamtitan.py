import requests
from xml.etree import ElementTree

class Spamtitan(object):
  def __init__(self, host):
    self.base_url = 'http://%s' % host
  
  def edit_domain(self, domain_name, server=None, rv=None, dyn_server=None, ldap_server=None,
                  ldap_port=None, ldap_search_dn=None, ldap_password=None, ldap_filter=None,
                  ldap_searchbase=None, ldap_result_attribute=None, email=None, delemail=None, 
                  domaingroup=None):
    ''' Modify settings for a particular domain.
    :param domain_name: Required. The name of the Domain to add
    :param server: Optional. The new destination server IP address or FQDN for this domain
    :param rv: Optional. The recipient verification method to use for this server. Possible values are:
    "none", "dynamic", "ldap", "list"
    :param dyn_server: Optional. The recipient verification server to use if the recipient verification is
    "dynamic". This setting will have no effect if the recipient verification (rv) setting is not set to
    "dynamic"
    :param ldap_server: Required.
    :param ldap_port: Required.
    :param ldap_search_dn: Optional.
    :param ldap_password: Optional.
    :param ldap_filter: Optional.
    :param ldap_searchbase: Optional.
    :param ldap_result_attribute: Optional. Defaults to mail.
    :param email: Optional. If list based recipient verification is been used, then use this setting to add
    email addresses to the list. The API call needs to be called once for each email address
    added.
    :param email / delemail: add or remove entry from list based recipient verification. View page 15 for
    more information.
    :param domaingroup: Domain Group to add domain to.
    '''
    url = '%s/domain/edit?name=%s' % (self.base_url, domain_name)
    
    if server:
      url += '&server=%s' % server
    if rv:
      url += '&rv=%s' % rv
    if dyn_server:
      url += '&dyn_server=%s' % dyn_server
    if ldap_server:
      url += '&ldap_server=%s' % ldap_server
    if ldap_port:
      url += '&ldap_port=%s' % ldap_port
    if ldap_search_dn:
      url += '&ldap_search_dn=%s' % ldap_search_dn
    if ldap_password:
      url += '&ldap_password=%s' % ldap_password
    if ldap_filter:
      url += '&ldap_filter=%s' % ldap_filter
    if ldap_searchbase:
      url += '&ldap_searchbase=%s' % ldap_searchbase
    if ldap_result_attribute:
      url += '&ldap_result_attribute=%s' % ldap_result_attribute
    if email:
      url += '&email=%s' % email
    if delemail:
      url += '&delemail=%s' % delemail
    if domaingroup:
      url += '&domaingroup=%s' % domaingroup

    r = requests.get(url)
    if r.status_code == 200:
     Exception('Error %s:%s' % (url, r.text))

    return r

  def delete_domain(self, domain_name):
    ''' Deletes a Spamtitan domain_name
    :param domain_name:str The domain you want to delete.
    '''
    url = '%s/domain/delete?name=%s' % (self.base_url, domain_name)
     
    r = requests.get(url)
    if r.status_code == 200:
     Exception('Error %s:%s' % (url, r.text))

    return r

  def create_domain(self, domain_name, relay):
    ''' create a domain on spamtitan
    :param domain_name:str the domain name you want to create.
    :param ralay:str server: Required. The destination mail server for this domain. 
          To specify a non-default port (25) append ":8025".
          o To specify a fallback server enter a list of IP addresses/FQDNs separated by spaces.
          SpamTitan will attempt delivery in the order listed. E.g.: server=1.2.3.4 5.6.2.3
          o Specify a comma (,) separated list of IP addresses and/or FQDNs. In this
          case SpamTitan will attempt delivery in a round-robin fashion between the
          listed servers. E.g.:server=1.2.3.4,1.2.3.5 
    '''
    url = '%s/domain/add?name=%s&server=%s' % (self.base_url, domain_name, relay)
     
    r = requests.get(url)
    if r.status_code == 200:
     Exception('Error %s:%s' % (url, r.text))

    return r
 
  def domain_exist(self, domain_name):
    ''' check if a domain exist
    :param domain_name:str the domain name you want to validate if exist or not.
    '''
    url = '%s/domain/exists?name=%s' % (self.base_url, domain_name) 
    r = requests.get(url)
    if r.status_code != 200:
      Exception('Error connecting the server %s' % url)
    
    try:
      tree = ElementTree.fromstring(r.content)
      if tree[0].tag == 'success':
        return True
      else:
        return False
    except e:
      Exception('Error Parsing Server Response: %s' % e)