odoo.define('project_task_hierarchy.error_dialog_clipboard', function (require) {
    "use strict";
    var RPCErrorDialog = require('web.rpc_error').RPCErrorDialog;
    RPCErrorDialog.include({
        onClickClipboard: function () {
            var contents = this.$el.find('.o_debug_details').text().trim();
            if (navigator.clipboard && navigator.clipboard.writeText) {
                navigator.clipboard.writeText(contents);
            } else {
                window.prompt("Copy the error below:", contents);
            }
        },
    });
});
