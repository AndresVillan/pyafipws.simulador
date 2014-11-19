# coding: utf8

db.define_table('request',
    Field('method'),
    Field('args', 'text'),
    Field('created_by_ip',readable=False,writable=False,default=request.client),
    Field('created_on','datetime',readable=False,writable=False,default=request.now),
)
