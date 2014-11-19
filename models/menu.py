# -*- coding: utf-8 -*- 

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = request.application
response.subtitle = T('customize me!')

##########################################
## this is the main application menu
## add/remove items as required
##########################################

response.menu = [
    ['Principal', False, 
     URL("welcome",'default','index'), []],
    ['Inicio', False, 
     URL(request.application,'default','index'), []],
    ['WSFEv1', False, 
     URL(request.application,'wsfev1','call/soap'), [
        
        [T('FEDummy'), False, 
         URL(request.application,'wsfev1','call/soap?op=FEDummy'), []],
        [T('FECAESolicitar'), False, 
         URL(request.application,'wsfev1','call/soap?op=FECAESolicitar'), []],
        
        
        ],
    ],

]

##########################################
## this is here to provide shortcuts
## during development. remove in production 
##########################################

response.menu_edit=[
  [T('Edit'), False, URL('admin', 'default', 'design/%s' % request.application),
   [
            [T('Controller'), False, 
             URL('admin', 'default', 'edit/%s/controllers/%s.py' \
                     % (request.application,request.controller=='appadmin' and
                        'default' or request.controller))], 
            [T('View'), False, 
             URL('admin', 'default', 'edit/%s/views/%s' \
                     % (request.application,response.view))],
            [T('Layout'), False, 
             URL('admin', 'default', 'edit/%s/views/layout.html' \
                     % request.application)],
            [T('Stylesheet'), False, 
             URL('admin', 'default', 'edit/%s/static/base.css' \
                     % request.application)],
            [T('DB Model'), False, 
             URL('admin', 'default', 'edit/%s/models/db.py' \
                     % request.application)],
            [T('Menu Model'), False, 
             URL('admin', 'default', 'edit/%s/models/menu.py' \
                     % request.application)],
            [T('Database'), False, 
             URL(request.application, 'appadmin', 'index')],
            ]
   ],
  ]
