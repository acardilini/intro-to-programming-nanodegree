// Create object to store bio information
var bio = {
  "firstName": "Adam",
  "lastName": "Cardilini",
  "role": "Associate Lecturer",
  "contacts": {
    "mobile": "0431 566 340",
    "email": "a.cardilini@gmail.com",
    "github": "https://github.com/acardilini",
    "blog": "https://adamcardilini.wordpress.com/",
    "location": "Melbourne, Vic, Australia"
  },
  "bioPic": "images/my-photo_UnitStaff.jpg",
  "welcomeMsg": "I am an educator and scientist driven to help create a more equitable world.",
  "skills": ["Teaching", "Curriculum Development", "Learning Resource Creation", "Online Teaching and Learning Environment Design", "Scientific Research", "Data Analysis", "R Statistical Package", "Python", "HTML/CSS"],
};

// Add work information to the bio object. (shows use of dot notation)
var work = {
  "workEmployer": "Deakin University",
  "workTitle": "Associate Lecturer in Work Integrated Learning and Learning Support",
  "workDates": "2012-current",
  "workLocation": "Burwood, Victoria, Australia"
};

// Add education information to the bio object. (shows use of bracket notation)
var education = {
  "schools": [
    {
      "schoolName": "Deakin University",
      "schoolDegree": "PhD",
      "schoolDates": "03/2011 - 03/2016",
      "schoolLocation": "Geelong, Victoria, Australia",
      "schoolMajor": "Ecological Genetics"
    },
    {
      "schoolName": "Deakin University",
      "schoolDegree": "BEnv (Honours)",
      "schoolDates": "2010",
      "schoolLocation": "Burwood, Victoria, Australia",
      "schoolMajor": "Ecology"
    },
    {
      "schoolName": "Deakin University",
      "schoolDegree": "BSci",
      "schoolDates": "2006 - 2009",
      "schoolLocation": "Burwood, Victoria, Australia",
      "schoolMajor": "Biological Sciences"
    }
  ],
  "onlineCourses": [
    {
      "title": "Introduction to Programming Nanodegree",
      "school": "Udacity",
      "dates": "2016",
      "url": "https://www.udacity.com/course/intro-to-programming-nanodegree--nd000"
    }
  ]
};

// format existing variables to include appropriate data
// Generic information
var formattedName = HTMLheaderName.replace("%data%", bio.firstName + " " + bio.lastName);
var formattedRole = HTMLheaderRole.replace("%data%", bio.role);
var formattedMobile = HTMLmobile.replace("%data%", bio.contacts.mobile);
var formattedEmail = HTMLemail.replace("%data%", bio.contacts.email);
var formattedGithub = HTMLgithub.replace("%data%", bio.contacts.github);
var formattedBlog = HTMLblog.replace("%data%", bio.contacts.blog);
var formattedLocation = HTMLlocation.replace("%data%", bio.contacts.location);
var formattedBioPic = HTMLbioPic.replace("%data%", bio.bioPic);
var formattedWelcomeMsg = HTMLwelcomeMsg.replace("%data%", bio.welcomeMsg);
var formattedSkillsStart = HTMLskillsStart.replace("%data%", bio.skillsStart);
var formattedSkills = HTMLskills.replace("%data%", bio.skills);

// Work
var formattedWorkEmployer = HTMLworkEmployer.replace("%data%", bio.work.workEmployer);
var formattedWorkTitle = HTMLworkTitle.replace("%data%", bio.work.workTitle);
var formattedWorkDates = HTMLworkDates.replace("%data%", bio.work.workDates);
var formattedWorkLocation = HTMLworkLocation.replace("%data%", bio.work.workLocation);

// Education
var formattedSchoolName = HTMLschoolName.replace("%data%", bio.education.schoolName);
var formattedSchoolDegree = HTMLschoolDegree.replace("%data%", bio.education.schoolDegree);
var formattedSchoolDates = HTMLschoolDates.replace("%data%", bio.education.schoolDates);
var formattedSchoolLocation = HTMLschoolLocation.replace("%data%", bio.education.schoolLocation);
var formattedSchoolMajor = HTMLschoolMajor.replace("%data%", bio.education.schoolMajor);


// append variables to the correct location
$("#header").prepend(formattedRole);
$("#header").prepend(formattedName);
$("#header").append(formattedMobile);
$("#header").append(formattedEmail);
$("#header").append(formattedGithub);
$("#header").append(formattedBlog);
$("#header").append(formattedLocation);
$("#header").append(formattedBioPic);
$("#header").append(formattedWelcomeMsg);
$("#header").append(formattedSkillsStart);
$("#header").append(formattedSkills);

$("#workExperience").append(formattedWorkEmployer);
$("#workExperience").append(formattedWorkTitle);
$("#workExperience").append(formattedWorkDates);
$("#workExperience").append(formattedWorkLocation);

$("#education").append(formattedSchoolName);
$("#education").append(formattedSchoolDegree);
$("#education").append(formattedSchoolDates);
$("#education").append(formattedSchoolLocation);
$("#education").append(formattedSchoolMajor);
