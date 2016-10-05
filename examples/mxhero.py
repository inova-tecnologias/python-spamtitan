import MySQLdb as mdb
from spamtitan import Spamtitan

''' mxHero Import
The following script import mxhero domains to SpamTitan Cluster.
'''
# Config
stcfg = {
  'host' : '192.168.99.102',
  'relay' : 'mxhero.server.com',
  'ldap_server' : 'ldap.local',
  'ldap_port' : 389,
  'ldap_search_dn' : 'uid=zimbra,cn=admins,cn=zimbra',
  'ldap_password' : 'supersecretpass',
  'ldap_filter' : 'mail=%s',
  'ldap_searchbase' : '',
  'ldap_result_attribute' : 'uid'
}
mxh = {
  'db_host' : '192.168.99.103',
  'db_user' : 'mxhusr',
  'db_pass' : 'passwordmx',
  'db_name' : 'mxhero',
  'db_port' : 3306
}

if __name__ == '__main__':
  st = Spamtitan(host=stcfg['host'])

  con = mdb.connect(user=mxh['db_user'], db=mxh['db_name'], passwd=mxh['db_pass'],
                    host=mxh['db_host'], port=mxh['db_port'])
  con = con.cursor(mdb.cursors.DictCursor)
  query = 'SELECT domain FROM domain'

  con.execute(query)
  res = con.fetchall()
  for row in res:
    try:
      print 'creating domain %s' % row['domain']
      st.create_domain(domain_name=row['domain'], relay=stcfg['relay'])
      r = st.edit_domain(domain_name=row['domain'],
                          rv='ldap',
                          ldap_server=stcfg['ldap_server'],
                          ldap_port=stcfg['ldap_port'],
                          ldap_search_dn=stcfg['ldap_search_dn'],
                          ldap_password=stcfg['ldap_password'],
                          ldap_filter=stcfg['ldap_filter'],
                          ldap_searchbase=stcfg['ldap_searchbase'],
                          ldap_result_attribute=stcfg['ldap_result_attribute']
                          )
      print r.status_code

      r = st.edit_policy(user=row['domain'],
                          spam_tag2_level=5,
                          spam_quarantine_to='',
                          spam_lover='Y',
                          virus_quarantine_to='',
                          digest='D', # quarantine report daily
                          report_type='Y', # new items since last report, except virus
                          digest_language='pt_BR'
                          )
      print r.status_code
    except Exception, e:
      print 'Error: %s' % e
      
  query = "SELECT domain_id, property_value FROM features_rules INNER JOIN features_rules_properties \
          ON features_rules.id = features_rules_properties.rule_id WHERE \
          features_rules.feature_id=15 AND property_key='email.list'"
  con.execute(query)
  res = con.fetchall()
  for row in res:
    try:
      print 'domain:%s whitelisting:%s' % (row['domain_id'], row['property_value'])
      st.add_whitelist(user=row['domain_id'], sender=row['property_value'])
    except Exception, e:
      print 'Error: %s' % e