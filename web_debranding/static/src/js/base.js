/*  Copyright 2015-2018 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
    Copyright 2017 ArtyomLosev <https://github.com/ArtyomLosev>
    License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html). */
odoo.define('web_debranding.base', function(require) {
    var WebClient = require('web.WebClient'),
    	AbstractField = require('web.AbstractField');
    	
    AbstractField.include({
    	setIDForLabel: function(id){
    		if (this.getFocusableElement()){
    			this.getFocusableElement().attr('id',id);
    		}
    	},
    	isFocusable: function(){
    		var $focusable = this.getFocusableElement(),
    			is_focusable = false;
    		if ($focusable){
    			is_focusable = $focusable.length && $focusable.is(':visible');
    		}
    		return is_focusable;
    	}
    }); 


    WebClient.include({
        init: function(parent) {
            this._super.apply(this, arguments);
            var self = this;
            this.set('title_part', {"zopenerp": ''});
            odoo.debranding_new_name = '';
            odoo.debranding_new_website = '';
            odoo.debranding_new_title = '';

            self._rpc({
                model: "ir.config_parameter",
                method: 'get_debranding_parameters',
            }, {
                shadow: true
            }).then(function(result){
                odoo.debranding_new_name = result['web_debranding.new_name'];
                odoo.debranding_new_website = result['web_debranding.new_website'];
                odoo.debranding_new_title = result['web_debranding.new_title'];
                self.set('title_part', {"zopenerp": odoo.debranding_new_title});

            });
        }
    });

});
