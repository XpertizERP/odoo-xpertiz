odoo.define('chatter_attachment_portal.chatter', function(require) {
    'use strict';

    var ajax = require('web.ajax');
    var core = require('web.core');
    var qweb = core.qweb;
    var PortalChatter = require('portal.chatter').PortalChatter;

    PortalChatter.include({
        _loadTemplates: function() {
            return $.when(this._super(), ajax.loadXML('/chatter_attachment_portal/static/src/xml/chatter.xml', qweb));
        },
    });
});