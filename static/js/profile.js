$(document).ready(function () {
//    formConfig();
//    modalConfig();
    $('#image-upload-btn').click(imageUploadFix);
    
//    $('#profile-save-btn').click(function() {
//    	console.log("update profile click");
//    	updateUser()
//    });

    $("#img-input").bind("change", function () {
        console.log($('#img-input').val().split('\\')[2]);
        $('#filepath').val($('#img-input').val().split('\\')[2]);
    });
});

//var updateUser = function (fields) {
//	fields = {'profile-description': "test desc."};
//    console.log(fields);
//     $.post( "/update-profile", fields ).done(function( json ) {
// //	    console.log("Response JSON: " + JSON.stringify(json));
// 	}).fail(function(jqxhr, textStatus, error) {
// 	    console.log("POST Request Failed: " + textStatus + ", " + error);
// 	});
//};

//var formConfig = function () {
//    $('#userSettingForm')
//        .form({
//            fields: {
//                // description: {
//                //     identifier: 'profile-description',
//                //     rules: [
//                //         {
//                //             type: 'empty',
//                //             prompt: 'Please enter some text for a body'
//                //         }
//                //     ]
//                // }
//            },
//            onSuccess: function (event, fields) {
////                submitNewReply(fields);
//            },
//            onFailure: function (formErrors, fields) {
//                //return;
//            },
//            keyboardShortcuts: false
//        });
//};

//var modalConfig = function () {
//    $('#userSettingsModal').modal({
//        closable: false,
//        onDeny: function () {
//            return true;
//        },
//        onApprove: function () {
//            $('#newReplyModalForm').form('validate form');
//            return $('#userSettingForm').form('is valid');
//        }
//    });
//};

var launchModal = function () {
    $('#userSettingsModal').modal('show');
    $('#userSettingForm').form('reset');
    $('#userSettingForm .error.message').empty();
};

var imageUploadFix = function (e) {
    //$('#img-input').val().split('\\')[2];
    e.preventDefault();
    $('#img-input').click();
};

