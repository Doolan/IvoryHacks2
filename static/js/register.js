/**
 * Created by Steven on 11/25/2016.
 */


$(document).ready(function () {
    window.KO_MODEL = FormModel();
    ko.applyBindings(window.KO_MODEL);
    setup();
    resumeUploadSetup();
});

var setup = function () {
    $('.ui.radio.checkbox').checkbox();
    $('.ui.dropdown').dropdown();
    formSetup();
};

var resumeUploadFix = function (e) {
    //$('#img-input').val().split('\\')[2];
    e.preventDefault();
    $('#resume-input').click();
};

var resumeUploadSetup = function () {
    $('#resume-upload-btn').click(resumeUploadFix);

    $("#resume-input").bind("change", function () {
        console.log($('#resume-input').val().split('\\')[2]);
        $('#filepath').val($('#resume-input').val().split('\\')[2]);
    });
};

var formSetup = function () {
    $('#hackathon-form').form({
        fields: {
            role: 'checked',
            tsize: 'empty',
            hacktype: 'empty',
            diet: 'empty'
        },
        onSuccess: function (event, fields) {
            console.log(fields);
        },
        onFailure: function (formErrors, fields) {
            console.log(fields);
            // return;
        },
        keyboardShortcuts: false
    });

    $('#employment-form').form({
        fields: {
            gradYear: 'empty',
            major: 'empty',
            secondary: 'empty',
            status: 'checked'
        },
        onSuccess: function (event, fields) {
            console.log(fields);
        },
        onFailure: function (formErrors, fields) {
            console.log(fields);
        },
        keyboardShortcuts: false
    })
};

var FormModel = function (user) {
    var self = this;
    // self.role = ko.observable();
    // self.tshirt_size = ko.observable();
    // self.hacktype = ko.observable();
    // self.dietaryRestrictions = ko.observable();
    // self.gradYear = ko.observable();
    // self.primaryMajor = ko.observable();
    // self.secondaryMajor = ko.observable();
    // self.employmentStatus = ko.observable();
    // self.resume_attachment = ko.observable();

    self.majorOptions = ["", "Biochemistry", "Biomedical Engineering", "Biology", "Chemical Engineering", "Chemistry", "Civil Engineering", "Computer Engineering", "Computer Science", "Software Engineering", "Electrical Engineering", "Mechanical Engineering", "Engineering Physics", "Physics", "Mathematics"];
    self.majorOptions.sort();

    self.secondaryOptions = [" N/A", "Robotics", "Computational Science", "Data Science", "Statistics"];
    self.secondaryOptions = self.secondaryOptions.concat(self.majorOptions);
    self.secondaryOptions.sort().push('Not Listed');

    self.hackathonValues = {};
    self.employmentValues = {};

    self.advanceToEmployment = function () {
        $('#hackathon-form').form('validate form');
        if ($('#hackathon-form').form('is valid')) {
            self.hackathonValues = $('#hackathon-form').form('get values');
            $('#hackathon-card').hide();
            $('#employment-card').show();
            $('#hackstep').removeClass('active').addClass('completed');
            $('#employmentstep').removeClass('disabled').removeClass('completed').addClass('active');
        }
    };

    $('#hackathon-card .extra.content .button').click(self.advanceToEmployment);
    self.advanceToResume = function () {
        $('#employment-form').form('validate form');
        if ($('#employment-form').form('is valid')) {
            self.employmentValues = $('#employment-form').form('get values');
            $('#employment-card').hide();
            $('#resume-card').show();
            $('#employmentstep').removeClass('active').addClass('completed');
            $('#resumestep').removeClass('disabled').removeClass('completed').addClass('active');
        }
    };
    $('#employment-card .extra.content .button').click(self.advanceToResume);
    self.advanceToConfirm = function () {
        // $('#employment-form').form('validate form');
        // if ($('#employment-form').form('is valid')) {
        //     self.employmentValues = $('#employment-form').form('get values');
        // $('#resume-card').hide();
        // $('#confirm-card').show();
        // $('#resumestep').removeClass('active').addClass('completed');
        // $('#confirmstep').removeClass('disabled').removeClass('completed').addClass('active');
        // // }
        self.updateUser();
        $('#resumeForm').submit();
        // console.log(self.hackathonValues, self.employmentValues);
    };
    $('#resume-card .extra.content .button').click(self.advanceToConfirm);


    self.updateUser = function(){
        var merged = {};
        Object.assign(merged, self.hackathonValues, self.employmentValues);
        console.log(merged, "merged object");
        $.post("/update-registration", merged).done(function (data) {
            console.log("Response JSON: " ,data);
        }).fail(function (jqxhr, textStatus, error) {
            console.log("POST Request Failed: " + textStatus + ", " + error);
        });
    }
};
