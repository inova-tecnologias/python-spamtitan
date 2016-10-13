# Python Spamtitan

1. [Install](#Install)
2. [Domains](#domains)
    1. [Create Domain](#create-domain)
    2. [Edit Domain](#edit-domain)
    3. [Delete Domain](#delete-domain)
3. [Policies](#policies)
    1. [Edit Policy](#edit-policy)
4. [WhiteList](#whitelist)
    1. [List WhiteList](#list-whitelist)
    2. [Add WhiteList](#add-whitelist)
    3. [Remove WhiteList](#remove-whitelist)

# Install
```bash
$ git clone https://github.com/inova-tecnologias/python-spamtitan.git
$ python setup.py install 
```

Import and use it

```python
from spamtitan import Spamtitan
st = Spamtitan(host='192.168.6.100')
```

# Domains
Methods to manage Domains

## Create Domain
```python
r = st.edit_domain(domain_name='mock.com', relay='my-mail-server.com:25')
print r.text, r.status_code
```

## Edit Domain
```python
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
r = st.delete_domain(domain_name='mock.com')
print r.text, r.status_code
```

# Policies
Methods to manage policies

## Edit Policy
```python
r = st.edit_policy(user='mock.com',
                        spam_tag2_level=4.5,
                        spam_quarantine_to='',
                        spam_lover='Y',
                        virus_quarantine_to='',
                        digest='D', # quarantine report daily
                        report_type='Y', # new items since last report, except virus
                        digest_language='pt_BR'
                        )
print r.text, r.status_code                        
```

# WhiteList
Methods to manage WhiteList

## List WhiteList
```python
r = st.list_whitelist(user='mock.com')
print r.text, r.status_code
```

## Add WhiteList
```python
r = st.add_whitelist(user='mock.com',
                     sender='fernando.cainelli@inova.net')
print r.text, r.status_code
```

## Remove WhiteList
```python
r = st.remove_whitelist(user='mock.com',
                     sender='fernando.cainelli@inova.net')
print r.text, r.status_code
```