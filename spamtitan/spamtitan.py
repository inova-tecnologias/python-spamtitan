import requests
from xml.etree import ElementTree

class Spamtitan(object):
  def __init__(self, host):
    self.base_url = 'http://%s' % host
  
  
  def list_whitelist(self, user=None):
    """ List Whitelisted Addresses and Domains
    param:user: Optional. The email address or domain name of the user/domain for which 
                to view the whitelist
    """
    url = '%s/whitelist/list' % (self.base_url)

    if user:
      url += '?user=%s' % user

    r = requests.get(url)
    if r.status_code == 200:
     Exception('Error %s:%s' % (url, r.text))
    
    return r

  def add_whitelist(self, sender, user=None):
    """ Whitelist a sender
    param:sender: Required. The email address or domain to add to the whitelist
    param:user: Optional. The email address or domain name of the whitelist entry to add. 
                If no user is specified, then the entry will be added to the global whitelist.
    """
    url = '%s/whitelist/add?sender=%s' % (self.base_url, sender)

    if user:
      url += '&user=%s' % user

    r = requests.get(url)
    if r.status_code == 200:
     Exception('Error %s:%s' % (url, r.text))

    return r
  
  def remove_whitelist(self, sender, user=None):
    """ Remove Whitelist sender
    param:sender: Required. The email address or domain to add to the whitelist
    param:user: Optional. The email address or domain name of the whitelist entry to add. 
                If no user is specified, then the entry will be added to the global whitelist.
    """
    url = '%s/whitelist/delete?sender=%s' % (self.base_url, sender)

    if user:
      url += '&user=%s' % user

    r = requests.get(url)
    if r.status_code == 200:
     Exception('Error %s:%s' % (url, r.text))

    return r

  def edit_policy(self, user, **kwargs):
    """ Edit user/domain policy
    param:user: Username or Domain to edit policy.
    param:virus_lover: Specifies if virus infected files should be passed for this user (Y/N). Default N.
    param:spam_lover: Specifies if messages exceeding the spam threshold should be passed for this
                        user (Y/N). Default N.
    param:banned_files_lover: Specifies if messages containing banned attachment should be passed
                              for this user (Y/N). Default N.
    param:bad_header_lover: Specifies if messages containing banned attachment should be passed
                            for this user (Y/N). Default N.
    param:bypass_virus_checks: Specifies if virus checking should be disabled for this user (Y/N).
                               Default N.
    param:bypass_spam_checks: Specifies if spam checking should be disabled for this user (Y/N).
                              Default N.
    param:bypass_banned_checks: Specifies if banned attachment checking should be disabled for this
                                user (Y/N). Default N.
    param:bypass_header_checks: Specifies if header checks are bypassed for this user (Y/N). Default
                                N.
    param:spam_modifies_subj: Specifies if the mail subject is changed when spam is detected for this
                              u ser (Y/N). Default N.
    param:spam_tag_level; Add spam score headers to mail when score is greater than or
                          equal. Default: 999. Type: float
    param:spam_tag2_level; Specifies the threshold over which messages will be considered spam.
                            Default: 5. Type: float
    param:spam_kill_level; Quarantine or discard spam when score is greater than or equal to.
                            Default: 5. Type: float
    param:report_kill_level; Specifies the threshold over which mail will be included in reports. Default:
                              999. Type: float
    param:spam_dsn_cutoff_level; Spam score at which not to generate delivery status notifications..
                                 Default: 0. Type: float
    param:spam_quarantine_cutoff_level; Score at which not to quarantine. Default: 999. Type: float
    param:spam_quarantine_to: Specifies how to deal with spam mail. (Default) spam-quarantine to
                                quarantine mail, set to **nothing** to reject. Set to *nothing* and set spam_lover to 
                                Y to Pass and Tag mail.
    param:virus_quarantine_to: Specifies how to deal with virus mail. (Default) virus-quarantine to
                                quarantine mail, set to *nothing* to reject. Set to *nothing* and set virus_lover 
                                to Y to Pass and Tag mail.
    param:banned_quarantine_to: Specifies how to deal with banned attachment mail. (Default)
                                banned-quarantine to quarantine mail, set to  to reject. Set to  and set
                                banned_files_lover to Y to Pass and Tag mail.
    param:locked: Specifies if the policy is locked. If a policy is locked, changes to the domain policy will
                  not be inherited by the locked user policy (Y/N). Default: N.
    param:digest: Specifies if this user should receive a quarantine report. N=Never, D=Daily,
                    WD=Week Days, M=Monthly. Default N.
    param:report_type: Specifies the type of quarantine report to send the user. Possible values are N
                        (New items since last report only) , A (all quarantine messages), X (All quarantined msgs,
                        except viruses), Y (New items since last report, except viruses). Default N.
    param:digest_language: Specifies the language that the report should be generated in
                            (cs_CZ/da_DK/de_DE/en_US/fr_FR/nl_NL/ja_JP/it_IT/pl_PL/es_ES). Default: en_US
    """
    url = '%s/policy/edit?user=%s' % (self.base_url, user)
    for attribute, value in kwargs.iteritems():
      aurl = '&attribute=%s&value=%s' % (attribute, value)
      r = requests.get(url+aurl)
      if r.status_code == 200:
        Exception('Error %s:%s' % (url, r.text))
    
    return r

  def edit_domain(self, domain_name, **kwargs):                  
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
    for attribute, value in kwargs.iteritems():
      url += '&%s=%s' % (attribute, value)
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