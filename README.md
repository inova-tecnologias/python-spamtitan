# Python Spamtitan

1. [Domains](#domains)
    1. [Create Domain](#create-domain)
    2. [Edit Domain](#edit-domain)
    3. [Delete Domain](#delete-domain)
1. [Policies](#policies)
    1. [Edit Policy](#edit-policy)


# Domains
Methods to manage Domains

## Create Domain
```python
from spamtitan import Spamtitan

st = Spamtitan(host='192.168.6.100')
r = st.edit_domain(domain_name='mock.com', relay='my-mail-server.com:25')

print r.text, r.status_code
```

## Edit Domain
```python
from spamtitan import Spamtitan

st = Spamtitan(host='192.168.6.100')
r = st.edit_domain(domain_name='mock.com',
                        server='my-mail-server.com:26,
                        rv='ldap',
                        ldap_server='ldap.local',
                        ldap_port=389,
                        ldap_search_dn='uid=admin,ou=people,dc=mock,dc=com'
                        ldap_password='supersecret',
                        ldap_filter='mail=%s',
                        ldap_searchbase='dc=mock,dc=com',
                        ldap_result_attribute='uid'
                        )

print r.text, r.status_code
```

## Delete Domain
```python
from spamtitan import Spamtitan

st = Spamtitan(host='192.168.6.100')
r = st.delete_domain(domain_name='mock.com')

print r.text, r.status_code
```

# Policies
Methods to manage policies

## Edit Policy
```python
from spamtitan import Spamtitan

st = Spamtitan(host='192.168.6.100')
r = st.edit_policy(user='mock.com',
                        spam_tag2_level=4.5,
                        spam_quarantine_to='',
                        spam_lover='Y',
                        virus_quarantine_to='',
                        digest='D', # quarantine report daily
                        report_type='Y', # new items since last report, except virus
                        digest_language='pt_BR'
                        )
```                        