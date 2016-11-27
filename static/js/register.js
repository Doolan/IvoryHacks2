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
            role: 'empty',
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
    })
};

var FormModel = function (user) {
    var self = this;
    self.role = ko.observable();
    self.tshirt_size = ko.observable();
    self.hacktype = ko.observable();
    self.dietaryRestrictions = ko.observable();
    self.gradYear = ko.observable();
    self.primaryMajor = ko.observable();
    self.secondaryMajor = ko.observable();
    self.employmentStatus = ko.observable();
    self.resume_attachment = ko.observable();

    self.majorOptions = ["", "Biochemistry", "Biomedical Engineering", "Biology", "Chemical Engineering", "Chemistry", "Civil Engineering", "Computer Engineering", "Software Engineering", "Electrical Engineering", "Mechanical Engineering", "Engineering Physics", "Physics"];
    self.majorOptions.sort();

    self.secondaryOptions = [" N/A", "Robotics", "Computational Science", "Data Science", "Statistics"];
    self.secondaryOptions = self.secondaryOptions.concat(self.majorOptions);
    self.secondaryOptions.sort().push('Not Listed');
};
